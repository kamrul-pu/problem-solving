"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer
points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a tree node with the given value and optional left and right children.

        Parameters:
            val (int): The value of the node.
            left (TreeNode): The left child node.
            right (TreeNode): The right child node.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev = None

    def __f(self, node: Optional[TreeNode]) -> None:
        """
        Helper method to flatten the binary tree into a linked list in-place.

        Parameters:
            node (TreeNode): The current node being processed.

        Returns:
            None
        """
        if node is None:
            return
        # Traverse right subtree first to ensure the correct order of flattened list
        self.__f(node=node.right)
        self.__f(node=node.left)
        # Update the current node's right child to the previously visited node
        node.right = self.prev
        # Set the left child of the current node to None
        node.left = None
        # Update the previous node to the current node
        self.prev = node

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flatten the binary tree into a linked list in-place.

        Parameters:
            root (TreeNode): The root of the binary tree.

        Returns:
            None
        """
        self.__f(node=root)


def build_tree() -> TreeNode:
    """
    Helper function to build a sample binary tree for testing.

    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    return root


if __name__ == "__main__":
    # Build the binary tree
    root: TreeNode = build_tree()
    # Create an instance of the Solution class
    solution: Solution = Solution()
    # Flatten the binary tree into a linked list
    solution.flatten(root=root)
