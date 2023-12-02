"""
Children sum property of a Binary Tree.
Node.val = Left.val + right.val
"""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"{self.data}"

    def pre_order(self) -> None:
        print(self.data, end="->")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()


def children_sum(root: TreeNode) -> None:
    if root is None:
        return
    child: int = 0
    if root.left:
        child += root.left.data
    if root.right:
        child += root.right.data
    if child >= root.data:
        root.data = child
    else:
        if root.left:
            root.left.data = root.data
        elif root.right:
            root.right.data = root.data

    children_sum(root.left)
    children_sum(root.right)

    total: int = 0
    if root.left:
        total += root.left.data
    if root.right:
        total += root.right.data

    if root.left or root.right:
        root.data = total


def build_tree():
    root = TreeNode(2)
    root.left = TreeNode(35)
    root.right = TreeNode(10)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(2)

    return root


if __name__ == "__main__":
    root = build_tree()
    root.pre_order()
    children_sum(root)
    print()
    root.pre_order()
