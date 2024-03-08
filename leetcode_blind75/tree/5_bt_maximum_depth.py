"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the farthest leaf node.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a TreeNode with a given value, left child, and right child.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __height(self, node: Optional[TreeNode]) -> int:
        """
        Helper function to calculate the height of a binary tree starting from a given node.

        Parameters:
            node (Optional[TreeNode]): The current node being considered.

        Returns:
            int: The height of the binary tree starting from the given node.
        """
        # Base case: if the node is None, the height is 0
        if node is None:
            return 0
        # Recursively calculate the height of the left and right subtrees
        lh: int = self.__height(node=node.left)
        rh: int = self.__height(node=node.right)

        # Return the height of the subtree rooted at the current node
        # which is 1 plus the maximum height between left and right subtrees
        return 1 + max(lh, rh)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the maximum depth of the binary tree.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The maximum depth of the binary tree.
        """
        # Call the helper function to calculate the height of the tree starting from the root
        return self.__height(node=root)


def build_tree():
    """
    Build a sample binary tree and return the root node.
    """
    # Create nodes and connect them to form a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)

    return root


if __name__ == "__main__":
    # Build a binary tree
    root = build_tree()
    # Create a Solution object
    solution: Solution = Solution()
    # Calculate and print the maximum depth of the binary tree
    print(solution.maxDepth(root=root))
