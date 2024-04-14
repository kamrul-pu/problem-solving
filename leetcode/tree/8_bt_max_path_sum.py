"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence
has an edge connecting them. A node can only appear in the sequence at most once. Note that the
path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
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
    MAXI: int = float("-inf")

    def __f(self, node: TreeNode) -> int:
        """
        Recursively calculate the maximum sum of any non-empty path starting from the given node.

        Args:
            node (TreeNode): The current node in the binary tree.

        Returns:
            int: The maximum sum of any non-empty path starting from the given node.
        """
        if node is None:
            return 0
        ls: int = max(0, self.__f(node=node.left))
        rs: int = max(0, self.__f(node=node.right))
        # Update MAXI with the maximum sum of paths involving the current node
        self.MAXI = max(self.MAXI, ls + rs + node.val)
        # Return the maximum sum of paths starting from the current node
        return node.val + max(ls, rs)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the maximum path sum of any non-empty path in the binary tree.

        Args:
            root (TreeNode): The root of the binary tree.

        Returns:
            int: The maximum path sum.
        """
        self.__f(node=root)
        return self.MAXI


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


if __name__ == "__main__":
    root: TreeNode = build_tree()
    solution: Solution = Solution()
    print(solution.maxPathSum(root=root))
