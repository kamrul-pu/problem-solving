"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree.
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.
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
    def __add_node(self, root: Optional[TreeNode], data) -> None:
        """
        Add a node to the binary search tree.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary search tree.
            data (int): The value of the node to be added.

        Returns:
            None
        """
        if root.val == data:
            return
        if data > root.data:
            # Add in the right subtree
            if root.right:
                self.add_node(root=root.right, data=data)
            else:
                root.right = TreeNode(data)
        else:
            # Add in the left subtree
            if root.left:
                self.add_node(root=root.left, data=data)
            else:
                root.left = TreeNode(data)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Insert a value into the binary search tree and return the root of the updated tree.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary search tree.
            val (int): The value to be inserted into the binary search tree.

        Returns:
            Optional[TreeNode]: The root node of the updated binary search tree.
        """
        if root is None:
            root = TreeNode(val)
            return root
        self.__add_node(root=root, data=val)
        return root


def build_tree() -> TreeNode:
    """
    Helper method to build a sample binary search tree for testing.

    Returns:
        TreeNode: The root node of the constructed binary search tree.
    """
    root: TreeNode = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    return root


if __name__ == "__main__":
    root: TreeNode = build_tree()
    solution: Solution = Solution()
    solution.insertIntoBST(root=root, val=5)
