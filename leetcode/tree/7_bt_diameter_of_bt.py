"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
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
    MAXI: int = 0

    def __height(self, node: Optional[TreeNode]) -> int:
        """
        Recursively compute the height of the subtree rooted at the given node.

        Args:
            node (TreeNode): The root of the subtree.

        Returns:
            int: The height of the subtree.
        """
        if node is None:
            return 0
        lh: int = self.__height(node=node.left)
        rh: int = self.__height(node=node.right)

        self.MAXI = max(self.MAXI, lh + rh)

        return 1 + max(lh, rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the diameter of the binary tree.

        Args:
            root (TreeNode): The root of the binary tree.

        Returns:
            int: The diameter of the binary tree.
        """
        self.__height(node=root)
        return self.MAXI


def build_tree() -> TreeNode:
    """
    Build a sample binary tree for testing purposes.

    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)

    return root


if __name__ == "__main__":
    root: TreeNode = build_tree()
    solution: Solution = Solution()
    print(solution.diameterOfBinaryTree(root=root))
