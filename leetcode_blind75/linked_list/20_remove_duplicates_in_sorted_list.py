"""
Given the head of a sorted linked list, delete all duplicates such that
each element appears only once. Return the linked list sorted as well.
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
        Remove duplicates from a sorted linked list.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            Optional[ListNode]: The head of the modified linked list with duplicates removed.
        """
        if head is None or head.next is None:
            return head

        # Create a dummy node to handle edge cases
        dummy: ListNode = ListNode(float("-inf"))
        dummy.next = head
        prev: ListNode = dummy
        node: ListNode = head

        # Iterate through the linked list
        while node:
            # If current node's value is equal to the previous node's value,
            # remove the current node by adjusting pointers
            if node.val == prev.val:
                prev.next = node.next
            else:
                prev = node
            node = node.next

        return dummy.next

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Public method to delete duplicates from a sorted linked list.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            Optional[ListNode]: The head of the modified linked list with duplicates removed.
        """
        return self.__f(head=head)


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
    # Test the deleteDuplicates method
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3)))))
    print_list(head=head)
    solution: Solution = Solution()
    head = solution.deleteDuplicates(head=head)
    print_list(head=head)
