"""Binary Tree Boundary Traversal Anti clock wise."""

from collections import deque


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def is_leaf_node(self, node) -> bool:
        return node.left is None and node.right is None

    def add_left_boundary(self, root, res: list[int]):
        curr: Node = root.left
        while curr:
            if not self.is_leaf_node(curr):
                res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    def add_right_boundary(self, root, res: list[int]):
        curr: Node = root
        tmp: list[int] = []
        while curr:
            if not self.is_leaf_node(curr):
                tmp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        while tmp:
            res.append(tmp.pop())

    def add_leaves(self, root, res: list[int]):
        if self.is_leaf_node(root):
            res.append(root.data)
            return
        if root.left:
            self.add_leaves(root.left, res)
        if root.right:
            self.add_leaves(root.right, res)

    def print_boundary_anti_clock(self, root) -> list[int]:
        res: list[int] = []
        if root is None:
            return res
        if not self.is_leaf_node(root):
            res.append(root.data)

        self.add_left_boundary(root, res)
        self.add_leaves(root, res)
        self.add_right_boundary(root, res)
        return res


def build_tree():
    root = Node(-10)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    return root


if __name__ == "__main__":
    root = build_tree()
    print(root.print_boundary_anti_clock(root))
