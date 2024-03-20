"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

1. Search for a node to remove.
2. If the node is found, delete the node.
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
    def __find_last_left(self, node: TreeNode) -> TreeNode:
        """
        Helper method to find the last left node in the subtree rooted at the given node.

        Parameters:
            node (TreeNode): The root node of the subtree.

        Returns:
            TreeNode: The last left node in the subtree.
        """
        if node.left is None:
            return node
        return self.__find_last_left(node=node.left)

    def __find_last_right(self, node: TreeNode) -> TreeNode:
        """
        Helper method to find the last right node in the subtree rooted at the given node.

        Parameters:
            node (TreeNode): The root node of the subtree.

        Returns:
            TreeNode: The last right node in the subtree.
        """
        if node.right is None:
            return node
        return self.__find_last_right(node=node.right)

    def __helper(self, node: TreeNode) -> TreeNode:
        """
        Helper method to delete the given node and return the updated subtree.

        Parameters:
            node (TreeNode): The node to be deleted.

        Returns:
            TreeNode: The updated subtree after deletion.
        """
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        right_child: TreeNode = node.right
        last_right: TreeNode = self.__find_last_right(node=node.left)
        last_right.right = right_child
        return node.left

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Delete the node with the given key from the BST.

        Parameters:
            root (TreeNode): The root node of the BST.
            key (int): The value of the node to be deleted.

        Returns:
            Optional[TreeNode]: The root node of the updated BST after deletion.
        """
        if root is None:
            return None
        if root.val == key:
            return self.__helper(node=root)

        dummy: TreeNode = root
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = self.__helper(node=root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.__helper(node=root.right)
                    break
                else:
                    root = root.right

        return dummy

    def __in_order(self, root: TreeNode) -> None:
        """
        Perform in-order traversal of the binary tree rooted at the given node.

        Parameters:
            root (TreeNode): The root node of the binary tree.
        """
        if root is None:
            return
        self.__in_order(root.left)
        print(root.val, end="->")
        self.__in_order(root.right)

    def print_tree(self, root: TreeNode) -> None:
        """
        Print the binary tree rooted at the given node in in-order traversal.

        Parameters:
            root (TreeNode): The root node of the binary tree.
        """
        self.__in_order(root=root)
        print("Null")


def build_tree() -> TreeNode:
    """
    Helper method to build a sample binary search tree for testing.

    Returns:
        TreeNode: The root node of the constructed binary search tree.
    """
    root: TreeNode = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    return root


if __name__ == "__main__":
    root: TreeNode = build_tree()
    key: int = 3
    solution: Solution = Solution()
    solution.print_tree(root=root)
    print(solution.deleteNode(root=root, key=key))
    solution.print_tree(root=root)
