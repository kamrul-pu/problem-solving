"""
Given the roots of two binary trees root and subRoot, return true if there is
a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all
of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __f(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        """
        Helper function to recursively check if two binary trees rooted at node1 and node2 are identical.

        Args:
            node1 (Optional[TreeNode]): Root node of the first binary tree.
            node2 (Optional[TreeNode]): Root node of the second binary tree.

        Returns:
            bool: True if the trees rooted at node1 and node2 are identical in structure and node values, False otherwise.
        """
        if node1 is None or node2 is None:
            # If both nodes are None, they are considered equal
            return node1 == node2

        # Check if node values are equal and recursively compare left and right subtrees
        return (
            node1.val == node2.val
            and self.__f(node1=node1.left, node2=node2.left)  # Compare left subtrees
            and self.__f(node1=node1.right, node2=node2.right)  # Compare right subtrees
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Check if there is a subtree of 'root' that has the same structure and node values as 'subRoot'.

        Args:
            root (Optional[TreeNode]): Root of the main binary tree.
            subRoot (Optional[TreeNode]): Root of the subtree to be searched in 'root'.

        Returns:
            bool: True if there exists a subtree in 'root' that matches 'subRoot', False otherwise.
        """
        if root is None:
            return False

        # Check if the current subtree rooted at 'root' is identical to 'subRoot'
        if self.__f(node1=root, node2=subRoot):
            return True

        # Recursively check in the left and right subtrees of 'root' for 'subRoot'
        # If either subtree contains 'subRoot', return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


if __name__ == "__main__":
    # Create a binary tree for testing
    root: TreeNode = TreeNode(
        val=3,
        left=TreeNode(val=4, left=TreeNode(1), right=TreeNode(2)),
        right=TreeNode(5),
    )

    solution: Solution = Solution()
    # Check if the left subtree of 'root' matches 'root.left'
    print(solution.isSubtree(root=root, subRoot=root.left))
