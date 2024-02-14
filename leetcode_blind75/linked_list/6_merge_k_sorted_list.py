"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head: Optional[ListNode]) -> None:
    cur: ListNode = head
    while cur:
        print(cur.val, end="->")
        cur = cur.next

    print("NUll")


def create_list(nums: List[int]) -> Optional[ListNode]:
    head: ListNode = ListNode(val=nums[0])
    tail: ListNode = head
    n: int = len(nums)
    for i in range(1, n):
        tail.next = ListNode(nums[i])
        tail = tail.next

    return head


class Solution:
    def __merge_optimal(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merges two sorted linked lists in an optimal way.

        Args:
            list1 (Optional[ListNode]): Head of the first sorted linked list.
            list2 (Optional[ListNode]): Head of the second sorted linked list.

        Returns:
            Optional[ListNode]: Head of the merged sorted linked list.
        """
        # If both lists are empty, return any of them (None in this case)
        if list1 is None and list2 is None:
            return list1
        # If one list is empty, return the other list
        if list1 is None or list2 is None:
            return list1 if list2 is None else list2

        # Determine the head of the merged list by selecting the smaller value
        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = seek

        # Merge the lists by iterating through the nodes
        while seek and target:
            # Move the seeker pointer until it's less than or equal to the target value
            while seek.next and seek.next.val < target.val:
                seek = seek.next

            # Swap pointers between seeker and target nodes
            seek.next, target = target, seek.next
            seek = seek.next

        return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists into one sorted linked list.

        Args:
            lists (List[Optional[ListNode]]): A list of k sorted linked lists.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.
        """
        # Get the number of lists
        n: int = len(lists)

        # If there are no lists or the input list is None, return None
        if n == 0 or lists is None:
            return None

        # Merge lists iteratively until only one list remains
        while len(lists) > 1:
            merged_list = []

            # Merge adjacent lists in pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_list.append(self.__merge_optimal(l1, l2))

            # Update the lists with the merged lists
            lists = merged_list

        # Return the head of the final merged list
        return lists[0]


if __name__ == "__main__":
    nums1: List[int] = [1, 4, 5]
    nums2: List[int] = [1, 3, 4]
    nums3: List[int] = [2, 6]

    list1: ListNode = create_list(nums=nums1)
    list2: ListNode = create_list(nums=nums2)
    list3: ListNode = create_list(nums=nums3)
    print_list(head=list1)
    print_list(head=list2)
    print_list(head=list3)
    solution: Solution = Solution()
    head = solution.mergeKLists(lists=[list1, list2, list3])
    print_list(head=head)
