"""
Flatten a multi-level linked list.
"""

from typing import List


class Node:
    def __init__(self, d, next=None, bottom=None):
        self.data = d
        self.next = next
        self.bottom = bottom


def flatten(root):
    # Your code here
    nodes = []
    temp = root
    while temp:
        nodes.append(temp.data)
        temp2 = temp.bottom
        while temp2:
            nodes.append(temp2.data)
            temp2 = temp2.bottom
        temp = temp.next

    if not nodes:
        return None
    nodes.sort()
    head = Node(d=nodes[0])
    temp = head
    for node in nodes[1:]:
        temp.next = Node(d=node)
        temp = temp.next

    return head


def print_list(head: Node) -> None:
    """
    Print the linked list starting from the given head node.

    Args:
        head (ListNode): The head node of the linked list.
    """
    node: Node = head
    while node:
        print(node.data, end="->")
        node = node.next
    print("Null")


if __name__ == "__main__":
    level1: Node = Node(d=5, bottom=Node(d=7, bottom=Node(8, bottom=Node(30))))
    level2: Node = Node(10, bottom=Node(d=20))
    level3: Node = Node(19, bottom=Node(d=22, bottom=Node(50)))
    level4: Node = Node(d=28, bottom=Node(d=35, bottom=Node(d=40, bottom=Node(45))))
    level1.next = level2
    level2.next = level3
    level3.next = level4
    head = flatten(root=level1)
    print_list(head=head)
