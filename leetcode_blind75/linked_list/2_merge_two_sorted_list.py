"""Merge two sorted list."""

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Public interface for merging two sorted linked lists.

        Args:
            list1 (Optional[ListNode]): Head of the first sorted linked list.
            list2 (Optional[ListNode]): Head of the second sorted linked list.

        Returns:
            Optional[ListNode]: Head of the merged sorted linked list.
        """
        return self.__merge_optimal(list1, list2)

    def print_list(self, head: Optional[ListNode]) -> None:
        cur: ListNode = head
        while cur:
            print(cur.val, end="->")
            cur = cur.next

        print("NUll")


if __name__ == "__main__":
    list1: ListNode = ListNode(val=1)
    node2: ListNode = ListNode(val=2)
    node3: ListNode = ListNode(val=4)
    list1.next = node2
    node2.next = node3

    list2: ListNode = ListNode(val=1)
    list2.next = ListNode(val=3)
    list2.next.next = ListNode(val=4)

    solution: Solution = Solution()
    solution.print_list(head=list1)
    solution.print_list(head=list2)
    n_head = solution.mergeTwoLists(list1=list1, list2=list2)
    solution.print_list(head=n_head)
