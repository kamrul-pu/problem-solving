"""Count the number of nodes in a complete binary tree."""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def find_height_left(node: TreeNode) -> int:
    height: int = 0
    while node:
        height += 1
        node = node.left

    return height


def find_height_right(node: TreeNode) -> int:
    height: int = 0
    while node:
        height += 1
        node = node.right

    return height


def count_nodes(root: TreeNode) -> int:
    if root is None:
        return 0
    lh: int = find_height_left(root)
    rh: int = find_height_right(root)

    if lh == rh:
        return (1 << lh) - 1

    return 1 + count_nodes(root.left) + count_nodes(root.right)


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    return root


if __name__ == "__main__":
    root = build_tree()
    print(count_nodes(root=root))
