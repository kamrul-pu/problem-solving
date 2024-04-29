"""
Given the root of a binary tree, invert the tree, and return its root.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: If root is None, return None (empty tree case)
        if root is None:
            return None

        # Swap the left and right children of the current node
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Recursively invert the left subtree
        self.invertTree(root.left)
        # Recursively invert the right subtree
        self.invertTree(root.right)

        # Return the root of the inverted tree
        return root


def pre_order(root: TreeNode) -> None:
    """
    Perform pre-order traversal of the binary tree rooted at the given node.

    Parameters:
        root (TreeNode): The root node of the binary tree.
    """
    if root is None:
        return

    # Print the current node's value
    print(root.val, end="->")
    # Traverse the left subtree recursively
    pre_order(root.left)
    # Traverse the right subtree recursively
    pre_order(root.right)


if __name__ == "__main__":
    # Create a binary tree
    root: TreeNode = TreeNode(
        val=4,
        left=TreeNode(val=2, left=TreeNode(1), right=TreeNode(3)),
        right=TreeNode(val=7, left=TreeNode(val=6), right=TreeNode(val=9)),
    )

    # Print the original binary tree using pre-order traversal
    print("Original Tree:")
    pre_order(root=root)
    print()

    # Create an instance of the Solution class
    solution: Solution = Solution()
    # Invert the binary tree
    root: TreeNode = solution.invertTree(root=root)

    # Print the inverted binary tree using pre-order traversal
    print("\nInverted Tree:")
    pre_order(root=root)
