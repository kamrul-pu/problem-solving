"""Flatten a Binary tree to a linked list."""


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_to_list(self, data: int) -> None:
        node: Node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def print_list(self) -> None:
        node = self.head
        while node is not None:
            print(node.data, end="->")
            node = node.next
        print("Null")


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    return root


def tree_to_linked_list(root: TreeNode, ls: LinkedList) -> None:
    if root is None:
        return None
    ls.add_to_list(root.data)
    tree_to_linked_list(root.left, ls)
    tree_to_linked_list(root.right, ls)


if __name__ == "__main__":
    root = build_tree()
    ls: LinkedList = LinkedList()
    ls.print_list()
    tree_to_linked_list(root=root, ls=ls)
    ls.print_list()
