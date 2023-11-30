"""Symetric Binary Tree."""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return self.data


def is_symetric_help(left: TreeNode, right: TreeNode) -> bool:
    if left is None or right is None:
        return left == right
    if left.data != right.data:
        return False

    return is_symetric_help(left.left, right.right) and is_symetric_help(
        left.right, right.left
    )


def is_symetric(root: TreeNode) -> bool:
    return root is None or is_symetric_help(root.left, root.right)


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    return root


if __name__ == "__main__":
    root = build_tree()
    print(is_symetric(root))
