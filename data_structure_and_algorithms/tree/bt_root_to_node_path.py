"""Right left view of Binary Tree."""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def get_path(root: TreeNode, ans: list[int], x: int) -> bool:
    if root is None:
        return False
    ans.append(root.data)
    if root.data == x:
        return True

    if get_path(root.left, ans, x) | get_path(root.right, ans, x):
        return True

    ans.pop()
    return False


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)

    return root


if __name__ == "__main__":
    root = build_tree()
    ans: list[int] = []
    if root is None:
        print("ans", ans)
    x: int = 7
    get_path(root, ans, x)
    print("ans", ans)
