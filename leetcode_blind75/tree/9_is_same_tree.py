"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

from typing import Optional


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
    def __f(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        """
        Recursively compare two binary trees to check if they are the same.

        Args:
            node1 (Optional[TreeNode]): The root of the first binary tree.
            node2 (Optional[TreeNode]): The root of the second binary tree.

        Returns:
            bool: True if the trees are the same, False otherwise.
        """
        # Base case: if either node1 or node2 is None, check if they are both None
        if node1 is None or node2 is None:
            return node1 == node2

        # Check if the values of the current nodes are the same and recursively
        # check their left and right subtrees
        return (
            node1.val == node2.val
            and self.__f(node1=node1.left, node2=node2.left)
            and self.__f(node1=node1.right, node2=node2.right)
        )

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are the same.

        Args:
            p (Optional[TreeNode]): The root of the first binary tree.
            q (Optional[TreeNode]): The root of the second binary tree.

        Returns:
            bool: True if the trees are the same, False otherwise.
        """
        return self.__f(node1=p, node2=q)


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
    print(solution.isSameTree(p=root1, q=root2))
