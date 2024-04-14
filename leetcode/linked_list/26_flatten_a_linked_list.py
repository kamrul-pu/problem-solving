"""
Flatten a multi-level linked list.
"""

from typing import List, Optional


class Node:
    def __init__(self, d, next=None, bottom=None):
        self.data = d
        self.next = next
        self.bottom = bottom


def merge_2_list(list1: Optional[Node], list2: Optional[Node]) -> Node:
    """
    Merge two sorted linked lists into one sorted linked list.

    Args:
        list1 (Optional[Node]): The head of the first sorted linked list.
        list2 (Optional[Node]): The head of the second sorted linked list.

    Returns:
        Node: The head of the merged sorted linked list.
    """
    # Initialize a dummy node to store the merged list
    dummy = Node(d=-1)
    res = dummy

    # Merge the two lists while maintaining the order
    while list1 and list2:
        if list1.data < list2.data:
            res.bottom = list1
            list1 = list1.bottom
        else:
            res.bottom = list2
            list2 = list2.bottom
        res = res.bottom
        res.next = None

    # Attach the remaining nodes from list1 or list2
    if list1:
        res.bottom = list1
    else:
        res.bottom = list2

    # Return the merged list starting from the next of the dummy node
    return dummy.bottom


def flatten_optimal(root: Optional[Node]) -> Optional[Node]:
    """
    Flatten a multi-level linked list recursively.

    Args:
        root (Optional[Node]): The head node of the multi-level linked list.

    Returns:
        Optional[Node]: The head node of the flattened linked list.
    """
    # Base case: if the root is None or has no next node, return root
    if root is None or root.next is None:
        return root

    # Flatten the next node recursively
    root.next = flatten_optimal(root=root.next)

    # Merge the current node with the next flattened node
    root = merge_2_list(list1=root, list2=root.next)

    # Return the merged list
    return root


def flatten_brute(root: Optional[Node]) -> Optional[Node]:
    """
    Flatten a multi-level linked list using a brute-force approach.

    Args:
        root (Optional[Node]): The head node of the multi-level linked list.

    Returns:
        Optional[Node]: The head node of the flattened linked list.
    """
    # Traverse the multi-level linked list and collect all node values
    nodes = []
    temp = root
    while temp:
        nodes.append(temp.data)
        temp2 = temp.bottom
        while temp2:
            nodes.append(temp2.data)
            temp2 = temp2.bottom
        temp = temp.next

    # If the list is empty, return None
    if not nodes:
        return None

    # Sort the collected node values
    nodes.sort()

    # Create a new linked list using the sorted node values
    head = Node(d=nodes[0])
    temp = head
    for node in nodes[1:]:
        temp.next = Node(d=node)
        temp = temp.next

    # Return the head of the created linked list
    return head


def flatten(root: Optional[Node]) -> Optional[Node]:
    """
    Flatten a multi-level linked list.

    Args:
        root (Optional[Node]): The head node of the multi-level linked list.

    Returns:
        Optional[Node]: The head node of the flattened linked list.
    """
    # Uncomment one of the following methods to use
    # return flatten_brute(root=root)  # Brute-force approach
    return flatten_optimal(root=root)  # Recursive approach


def print_list(head: Node) -> None:
    """
    Print the linked list starting from the given head node.

    Args:
        head (Node): The head node of the linked list.
    """
    node: Node = head
    while node:
        print(node.data, end="->")
        node = node.bottom
    print("Null")


if __name__ == "__main__":
    # Creating a multi-level linked list
    level1: Node = Node(d=5, bottom=Node(d=7, bottom=Node(8, bottom=Node(30))))
    level2: Node = Node(10, bottom=Node(d=20))
    level3: Node = Node(19, bottom=Node(d=22, bottom=Node(50)))
    level4: Node = Node(d=28, bottom=Node(d=35, bottom=Node(d=40, bottom=Node(45))))
    level1.next = level2
    level2.next = level3
    level3.next = level4

    # Flatten the multi-level linked list
    head = flatten(root=level1)

    # Print the flattened linked list
    print_list(head=head)
