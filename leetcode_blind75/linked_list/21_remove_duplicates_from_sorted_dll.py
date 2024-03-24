"""
Given the head of a sorted linked list, delete all duplicates such that
each element appears only once. Return the linked list sorted as well.
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


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
        head.prev = dummy
        node: ListNode = head

        # Iterate through the linked list
        while node:
            # If current node's value is equal to the previous node's value,
            # remove the current node by adjusting pointers
            if node.val == node.prev.val:
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
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


def create_doubly_linked_list(values: List[int]) -> Optional[ListNode]:
    """
    Create a doubly linked list from a list of values.

    Args:
        values (List[int]): The list of values to create the linked list from.

    Returns:
        Optional[ListNode]: The head of the created linked list.
    """
    if not values:
        return None
    head: ListNode = ListNode(val=values[0])
    prev: ListNode = head
    for val in values[1:]:
        new_node: ListNode = ListNode(val=val, prev=prev)
        prev.next = new_node
        prev = new_node

    return head


def print_list(head: Optional[ListNode]) -> None:
    """
    Print the linked list starting from the given head node.

    Args:
        head (Optional[ListNode]): The head node of the linked list.
    """
    current: Optional[ListNode] = head
    while current:
        print(current.val, end=" <-> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    # Test the deleteDuplicates method
    values: List[int] = [1, 1, 2, 2, 3, 4, 4, 5]
    head = create_doubly_linked_list(values=values)
    print_list(head=head)
    solution: Solution = Solution()
    head = solution.deleteDuplicates(head=head)
    print_list(head=head)
