"""Right left view of Binary Tree."""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def lowest_common_anchestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # base case
    if root is None or root == p or root == q:
        return root
    left: TreeNode = lowest_common_anchestor(root.left, p, q)
    right: TreeNode = lowest_common_anchestor(root.right, p, q)

    # result
    if left is None:
        return right
    elif right is None:
        return left
    else:
        # booth left and right are null, we found our result
        return root


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.left.left = TreeNode(8)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(7)

    return root


if __name__ == "__main__":
    root = build_tree()
    p: TreeNode = root.right.right.right
    q: TreeNode = root.right.left.left
    ans: TreeNode = lowest_common_anchestor(root, p, q)
    print(ans.data)
