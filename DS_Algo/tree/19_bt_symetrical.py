"""
Given the root of a binary tree, check whether it is
a mirror of itself (i.e., symmetric around its center).
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __f(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """
        Internal method to recursively check if two subtrees are mirror images of each other.

        Parameters:
            left (Optional[TreeNode]): The left subtree.
            right (Optional[TreeNode]): The right subtree.

        Returns:
            bool: True if the subtrees are mirror images, False otherwise.
        """
        # If both subtrees are None, they are mirror images
        if left is None or right is None:
            return left == right
        # If the values at the current nodes are different, they are not mirror images
        if left.val != right.val:
            return False
        # Recursively check if the left subtree of left node is mirror image of right subtree of right node
        # and vice versa
        return self.__f(left=left.left, right=right.right) and self.__f(
            left=left.right, right=right.left
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Method to check if a binary tree is symmetric.

        Parameters:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            bool: True if the binary tree is symmetric, False otherwise.
        """
        # An empty tree is symmetric by definition
        return root is None or self.__f(left=root.left, right=root.right)


def build_tree() -> TreeNode:
    """
    Helper function to build a sample symmetric binary tree for testing.

    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    return root


if __name__ == "__main__":
    root: TreeNode = build_tree()
    solution: Solution = Solution()
    print(solution.isSymmetric(root=root))
