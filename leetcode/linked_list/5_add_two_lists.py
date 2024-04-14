"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import Optional


class Node:
    def __init__(self, data: int, next=None) -> None:
        """
        Initialize a node with data and a reference to the next node.

        Parameters:
            data (int): The data value of the node.
        """
        self.data = data
        self.next: Optional[Node] = next


def add_list(head1: Node, head2: Node) -> Node:
    """
    Add two numbers represented by linked lists and return the sum as a linked list.

    Parameters:
        head1 (Node): The head of the first linked list.
        head2 (Node): The head of the second linked list.

    Returns:
        Node: The head of the resulting linked list representing the sum.
    """
    # Create a dummy node to simplify the logic
    dummy: Node = Node(data=-1)
    # Pointer to traverse the result list
    cur: Node = dummy
    # Initialize carry to 0
    carry: int = 0
    # Pointers to traverse the input lists
    l1: Node = head1
    l2: Node = head2

    # Traverse both lists until all nodes are processed
    while l1 or l2:
        # Initialize total to the current carry value
        total: int = carry
        # Add the current node values if available
        if l1:
            total += l1.data
            l1 = l1.next
        if l2:
            total += l2.data
            l2 = l2.next
        # Calculate the digit and carry for the current position
        data: int = total % 10
        carry = total // 10
        # Create a new node with the calculated digit and append it to the result list
        cur.next = Node(data=data)
        cur = cur.next

    # If there's a remaining carry after processing all nodes, append it as a new node
    if carry:
        cur.next = Node(data=carry)

    # Return the result list excluding the dummy node
    return dummy.next


def print_list(head: Node) -> None:
    """
    Print the linked list starting from the given head node.

    Parameters:
        head (Node): The head node of the linked list.
    """
    node: Node = head
    while node:
        print(node.data, end="->")
        node = node.next
    print("Null")


if __name__ == "__main__":
    # Example usage
    head1: Node = Node(data=2, next=Node(data=4, next=Node(data=6)))
    head2: Node = Node(data=3, next=Node(data=8, next=Node(data=7)))
    print_list(head=head1)
    print_list(head=head2)
    head3: Node = add_list(head1=head1, head2=head2)
    print_list(head=head3)
