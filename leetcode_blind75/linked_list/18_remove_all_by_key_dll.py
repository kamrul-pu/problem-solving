"""
Given the head of a linked list and an integer val, remove all the nodes
of the linked list that have Node.val == val, and return the new head.
"""

from typing import Optional


class Node:
    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class Solution:
    def __f(self, head: Optional[Node], val: int) -> Optional[Node]:
        """
        Parameters:
            head (Node): The head of the linked list.
            val (int): The value to be removed from the linked list.

        Returns:
            Node: The head of the modified linked list after removing nodes with the given value.
        """
        # Create a dummy node to handle cases where the head node needs to be removed
        dummy: Node = Node(-1, head)
        prev = dummy
        node: Node = head
        while node:
            if node.val == val:
                # Remove the node with the given value by adjusting the pointers
                prev.next = node.next
                if node.next:
                    node.next.prev = prev
                node = node.next
            else:
                # Move to the next node
                prev = node
                node = node.next

        return dummy.next

    def removeElements(self, head: Optional[Node], val: int) -> Optional[Node]:
        """
        Parameters:
            head (Node): The head of the linked list.
            val (int): The value to be removed from the linked list.

        Returns:
            Node: The head of the modified linked list after removing nodes with the given value.
        """
        if head is None:
            return head
        return self.__f(head=head, val=val)


def print_list(head: Node) -> None:
    """
    Prints the linked list starting from the given head node.

    Parameters:
        head (Node): The head node of the linked list.
    """
    node: Node = head
    while node:
        print(node.val, end="->")
        node = node.next
    print("Null")


if __name__ == "__main__":
    one: Node = Node(10)
    two: Node = Node(3)
    three: Node = Node(10)
    head = one
    one.next = two
    two.prev = one
    two.next = three
    three.prev = two
    val: int = 10
    print_list(head=head)
    solution: Solution = Solution()
    head = solution.removeElements(head=head, val=val)
    print_list(head=head)
