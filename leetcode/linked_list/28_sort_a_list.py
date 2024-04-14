"""
Given the head of a linked list, return the list after sorting it in ascending order.
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __f(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur: ListNode = head
        elements: List[int] = []
        while cur:
            elements.append(cur.val)
            cur = cur.next
        elements.sort()
        cur = head
        i: int = 0
        while cur:
            cur.val = elements[i]
            cur = cur.next
            i += 1
        return head

    def __middle(self, head: Optional[ListNode]) -> ListNode:
        """
        Find the middle node of a linked list using the two-pointer technique.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            ListNode: The middle node of the linked list.
        """
        slow: ListNode = head
        fast: ListNode = head.next
        # Move the fast pointer by two steps and the slow pointer by one step until the fast pointer reaches the end
        # This ensures that the slow pointer will be at the middle node when the fast pointer reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def __merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Merge two sorted linked lists into one sorted linked list.

        Args:
            list1 (ListNode): The head of the first sorted linked list.
            list2 (ListNode): The head of the second sorted linked list.

        Returns:
            ListNode: The head of the merged sorted linked list.
        """
        dummy: ListNode = ListNode(-1)
        temp = dummy
        # Compare the values of the nodes in both lists and merge them in sorted order
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        # Attach the remaining nodes from either list1 or list2
        temp.next = list1 if list1 else list2
        return dummy.next

    def __merge_sort(self, head: ListNode) -> ListNode:
        """
        Sort a linked list using the merge sort algorithm.

        Args:
            head (ListNode): The head of the linked list.

        Returns:
            ListNode: The head of the sorted linked list.
        """
        # Base case: If the list is empty or contains only one node, it is already sorted
        if head is None or head.next is None:
            return head
        # Find the middle node of the list
        middle: ListNode = self.__middle(head=head)
        # Split the list into two halves and recursively sort each half
        right: ListNode = middle.next
        middle.next = None
        left: ListNode = head
        left = self.__merge_sort(head=left)
        right = self.__merge_sort(head=right)
        # Merge the sorted halves
        return self.__merge(list1=left, list2=right)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sort a linked list in ascending order using the merge sort algorithm.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            Optional[ListNode]: The head of the sorted linked list.
        """
        # Edge case: If the list is empty, return None
        if head is None:
            return head
        # Call the helper function to perform merge sort on the linked list
        return self.__merge_sort(head=head)


def print_list(head: ListNode) -> None:
    """
    Print the linked list starting from the given head node.

    Args:
        head (ListNode): The head node of the linked list.
    """
    node: ListNode = head
    while node:
        print(node.val, end="->")
        node = node.next
    print("Null")


if __name__ == "__main__":
    # Test the sortList method
    head: ListNode = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print_list(head=head)
    solution: Solution = Solution()
    head = solution.sortList(head=head)
    print_list(head=head)
