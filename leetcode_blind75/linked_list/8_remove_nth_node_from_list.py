"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __f(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Helper function to remove the nth node from the end of a linked list.

        Parameters:
            head (Optional[ListNode]): The head node of the linked list.
            n (int): The position of the node to be removed from the end.

        Returns:
            Optional[ListNode]: The head node of the modified linked list.
        """
        if head is None:
            return head

        # Count the number of nodes in the linked list
        cnt: int = 0
        cur: ListNode = head
        while cur:
            cnt += 1
            cur = cur.next

        # If the node to be removed is the first node, update head
        if cnt == n:
            head = head.next
            return head

        # If n is greater than the number of nodes, no changes needed
        if n > cnt:
            return head

        # Find the target node to be removed
        target: int = cnt - n - 1
        cur: ListNode = head
        while target:
            target -= 1
            cur = cur.next

        # Remove the target node
        cur.next = cur.next.next
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the linked list and return the head node.

        Parameters:
            head (Optional[ListNode]): The head node of the linked list.
            n (int): The position of the node to be removed from the end.

        Returns:
            Optional[ListNode]: The head node of the modified linked list.
        """
        return self.__f(head=head, n=n)


if __name__ == "__main__":
    head: ListNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution: Solution = Solution()
    n: int = 2
    head = solution.removeNthFromEnd(head=head, n=n)
