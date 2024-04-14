"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that have Node.val == val,
and return the new head.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __f(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Removes all nodes with the given value from the linked list.

        This method iterates through the linked list, removing all nodes with the given value.
        It uses a dummy node to handle the case where the head node itself needs to be removed.

        Parameters:
            head (ListNode): The head of the linked list.
            val (int): The value to be removed from the linked list.

        Returns:
            ListNode: The head of the modified linked list after removing nodes with the given value.
        """
        # Create a dummy node to handle cases where the head node needs to be removed
        dummy: ListNode = ListNode(-1, head)
        prev = dummy
        node: ListNode = head
        while node:
            if node.val == val:
                # Remove the node with the given value by adjusting the pointers
                prev.next = prev.next.next
                node = node.next
            else:
                # Move to the next node
                prev = node
                node = node.next

        return dummy.next

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Removes all nodes with the given value from the linked list.

        Parameters:
            head (ListNode): The head of the linked list.
            val (int): The value to be removed from the linked list.

        Returns:
            ListNode: The head of the modified linked list after removing nodes with the given value.
        """
        if head is None:
            return head
        return self.__f(head=head, val=val)


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
    head: ListNode = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(6)))))
    print_list(head=head)
    k: int = 6
    solution: Solution = Solution()
    head = solution.removeElements(head=head, val=k)
    print_list(head=head)
