"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing,
where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __f(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle node of a linked list and removes it.

        Parameters:
            head (ListNode): The head of the linked list.

        Returns:
            ListNode: The head of the modified linked list after removing the middle node.
        """
        slow: ListNode = head
        fast: ListNode = head
        prev: ListNode = None

        # Move slow pointer by one and fast pointer by two until fast pointer reaches the end
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Skip the middle node by modifying pointers
        prev.next = prev.next.next
        return head

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Deletes the middle node of a linked list.

        Parameters:
            head (ListNode): The head of the linked list.

        Returns:
            ListNode: The head of the modified linked list after removing the middle node.
        """
        if head is None or head.next is None:
            return None
        return self.__f(head=head)


def print_list(head: ListNode) -> None:
    """
    Prints the linked list starting from the given head node.

    Parameters:
        head (ListNode): The head node of the linked list.
    """
    node: ListNode = head
    while node:
        print(node.val, end="->")
        node = node.next
    print("Null")


if __name__ == "__main__":
    head: ListNode = ListNode(
        1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))
    )
    print_list(head=head)
    solution: Solution = Solution()
    head = solution.deleteMiddle(head=head)
    print_list(head=head)
