"""Right left view of Binary Tree."""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def right_view(node: TreeNode, level: int, ans: list[int]) -> list[int]:
    if node is None:
        return
    if len(ans) == level:
        ans.append(node.data)
    right_view(node.right, level + 1, ans)
    right_view(node.left, level + 1, ans)


def left_view(node: TreeNode, level: int, left: list[int]) -> list[int]:
    if node is None:
        return
    if len(left) == level:
        left.append(node.data)
    left_view(node.left, level + 1, left)
    right_view(node.right, level + 1, left)


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    return root


if __name__ == "__main__":
    root = build_tree()
    right: list[int] = []
    right_view(root, 0, right)
    print(right)
    left: list[int] = []
    left_view(root, 0, left)
    print(left)
