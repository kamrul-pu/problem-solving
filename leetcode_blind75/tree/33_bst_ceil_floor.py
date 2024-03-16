"""
Floor and ceil in BST
ceil: val>=key
floor: val<=key
"""

from typing import Optional


# Definition for a binary search tree node.
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
    def inorder(self, root: Optional[TreeNode]) -> None:
        """
        Perform an inorder traversal of the binary search tree.

        Parameters:
            root (Optional[TreeNode]): The root of the binary search tree.

        Returns:
            None
        """
        if root is None:
            return
        self.inorder(root.left)
        print(root.val, end="->")
        self.inorder(root.right)

    def find_ceil(self, root: Optional[TreeNode], key: int) -> int:
        """
        Find the smallest value in the BST greater than or equal to the given key.

        Parameters:
            root (Optional[TreeNode]): The root of the binary search tree.
            key (int): The key to find the ceil value for.

        Returns:
            int: The ceil value.
        """
        ceil: int = -1
        while root:
            if root.val == key:
                ceil = (
                    root.val
                )  # If the current node's value is equal to the key, it is the ceil value
                return ceil
            if root.val > key:
                # If the current node's value is greater than the key, update ceil and move to the left subtree
                ceil = root.val
                root = root.left
            else:
                # If the current node's value is less than the key, move to the right subtree
                root = root.right

        return ceil

    def find_floor(self, root: Optional[TreeNode], key: int) -> int:
        """
        Find the largest value in the BST less than or equal to the given key.

        Parameters:
            root (Optional[TreeNode]): The root of the binary search tree.
            key (int): The key to find the floor value for.

        Returns:
            int: The floor value.
        """
        floor: int = -1
        while root:
            if root.val == key:
                floor = (
                    root.val
                )  # If the current node's value is equal to the key, it is the floor value
                return floor
            if root.val > key:
                # If the current node's value is greater than the key, move to the left subtree
                root = root.left
            else:
                # If the current node's value is less than the key, update floor and move to the right subtree
                floor = root.val
                root = root.right
        return floor


def build_bst() -> TreeNode:
    """
    Helper method to build a binary search tree with 10 nodes.

    Returns:
        TreeNode: The root of the constructed binary search tree.
    """
    # Define the nodes of the binary search tree with hard-coded values
    root: TreeNode = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    root.left.left.left = TreeNode(1)
    root.right.right.left = TreeNode(9)
    root.right.right.right = TreeNode(10)

    return root


# Test the build_bst method
if __name__ == "__main__":
    root: TreeNode = build_bst()
    print(root.val)  # Print the value of the root node of the constructed BST
    solution: Solution = Solution()
    solution.inorder(root=root)
    print("Null")
    print(solution.find_ceil(root=root, key=2))
    print(solution.find_floor(root=root, key=12))
