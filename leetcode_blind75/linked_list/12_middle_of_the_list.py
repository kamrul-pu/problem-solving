"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

from typing import Optional


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __f(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the middle node of a linked list.

        Parameters:
            head (ListNode): The head of the linked list.

        Returns:
            ListNode: The middle node of the linked list.
        """
        if head is None or head.next is None:
            return head

        # Initialize slow and fast pointers
        slow: ListNode = head
        fast: ListNode = head

        # Move slow pointer by one step and fast pointer by two steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the middle node of a linked list.

        Parameters:
            head (ListNode): The head of the linked list.

        Returns:
            ListNode: The middle node of the linked list.
        """
        return self.__f(head=head)


if __name__ == "__main__":
    head: ListNode = ListNode(
        1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))
    )
    solution: Solution = Solution()
    print(solution.middleNode(head=head).val)
