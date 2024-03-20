"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __f(self, node: Optional[TreeNode], mn: int, mx: int) -> bool:
        """
        Helper method to recursively determine if the binary tree is a valid BST.

        Parameters:
            node (Optional[TreeNode]): The current node being processed.
            mn (int): The minimum allowed value for nodes in the subtree.
            mx (int): The maximum allowed value for nodes in the subtree.

        Returns:
            bool: True if the subtree rooted at 'node' is a valid BST, False otherwise.
        """
        if node is None:
            return True
        if node.val >= mx or node.val <= mn:
            return False
        return self.__f(node=node.left, mn=mn, mx=node.val) and self.__f(
            node=node.right, mn=node.val, mx=mx
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if the given binary tree is a valid BST.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            bool: True if the binary tree is a valid BST, False otherwise.
        """
        INT_MIN: int = float("-inf")
        INT_MAX: int = float("inf")
        return self.__f(node=root, mn=INT_MIN, mx=INT_MAX)


def build_tree() -> TreeNode:
    """
    Helper method to build a sample binary tree for testing.

    Returns:
        TreeNode: The root node of the constructed binary tree.
    """
    root: TreeNode = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    return root


if __name__ == "__main__":
    root: TreeNode = build_tree()
    solution: Solution = Solution()
    print(solution.isValidBST(root=root))
