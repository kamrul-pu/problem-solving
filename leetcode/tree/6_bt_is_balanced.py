"""Given a binary tree, determine if it is  height-balanced."""

"""Given a binary tree, determine if it is height-balanced."""

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
    def __height(self, node: Optional[TreeNode]) -> int:
        """
        Recursively compute the height of the subtree rooted at the given node.

        Args:
            node (TreeNode): The root of the subtree.

        Returns:
            int: The height of the subtree, or -1 if the subtree is not height-balanced.
        """
        if node is None:
            return 0
        lh: int = self.__height(node=node.left)
        rh: int = self.__height(node=node.right)

        if lh == -1 or rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1

        return 1 + max(lh, rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Check if the given binary tree is height-balanced.

        Args:
            root (TreeNode): The root of the binary tree.

        Returns:
            bool: True if the tree is height-balanced, False otherwise.
        """
        return self.__height(node=root) != -1


def build_tree():
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
    root = build_tree()
    solution: Solution = Solution()
    print(solution.isBalanced(root=root))
