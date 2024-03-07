"""Widht of a Binary Tree."""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"Node: {self.data} left: {self.left} right: {self.right}"


def width_of_bt(root: TreeNode) -> int:
    if root is None:
        return 0
    q = deque()
    q.append(root)
    i: int = -1
    while q:
        cur_size: int = len(q)
        i += 1
        while cur_size > 0:
            node: TreeNode = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            cur_size -= 1

    return 2**i


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(10)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(11)
    root.left.left.right = TreeNode(10)
    root.left.right.left = TreeNode(9)
    root.left.right.right = TreeNode(6)
    root.right.left.left = TreeNode(1)
    root.right.left.right = TreeNode(7)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(10)

    return root


if __name__ == "__main__":
    root = build_tree()
    print(width_of_bt(root=root))
