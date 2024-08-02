"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

from collections import deque
from typing import Optional, List, Deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a TreeNode with a value and optional left and right children.

        Args:
            val (int, optional): Value of the node. Defaults to 0.
            left (TreeNode, optional): Left child of the node. Defaults to None.
            right (TreeNode, optional): Right child of the node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zig_zag(self, root: Optional["TreeNode"]) -> List[List[int]]:
        ans: List[List[int]] = []
        if root is None:
            return ans
        q: Deque[TreeNode] = deque()
        q.append(root)
        flag: bool = True
        while q:
            tmp: List[int] = []
            n: int = len(q)
            while n > 0:
                node: TreeNode = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                n -= 1
            if flag:
                ans.append(tmp)
                flag = False
            else:
                ans.append(list(reversed(tmp)))
                flag = True
        return ans


def build_tree():
    """
    Build a sample binary tree for testing purposes.

    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    return root


def build_tree2():
    """
    Build another sample binary tree for testing purposes.

    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    return root


if __name__ == "__main__":
    root1: TreeNode = build_tree()
    root2: TreeNode = build_tree2()
    solution: Solution = Solution()
    print(solution.zig_zag(root1))
