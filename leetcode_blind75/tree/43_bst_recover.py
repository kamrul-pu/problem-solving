"""
You are given the root of a binary search tree (BST), where the values of exactly two nodes
of the tree were swapped by mistake. Recover the tree without changing its structure.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        # Initialize variables to keep track of the nodes involved in the incorrect swaps
        self.first: TreeNode = None
        self.prev: TreeNode = None
        self.middle: TreeNode = None
        self.last: TreeNode = None

    def __inorder(self, node: Optional[TreeNode]) -> None:
        # Perform in-order traversal of the BST to identify incorrectly swapped nodes
        if node is None:
            return
        self.__inorder(node=node.left)
        if self.prev and node.val < self.prev.val:
            # If current node is less than previous node, it indicates a violation
            if self.first is None:
                # For the first violation, mark the previous and current nodes
                self.first = self.prev
                self.middle = node
            else:
                # For the second violation, mark the current node as last
                self.last = node
        self.prev = node
        self.__inorder(node=node.right)

    def __recover(self, root: Optional[TreeNode]) -> None:
        # Method to recover the tree by swapping the incorrectly swapped nodes
        self.__inorder(node=root)
        if self.first and self.last:
            # If there are two nodes swapped, swap their values
            self.first.val, self.last.val = self.last.val, self.first.val
        elif self.first and self.middle:
            # If only one node is swapped with its adjacent node, swap their values
            self.first.val, self.middle.val = self.middle.val, self.first.val

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Modify the root in-place to recover the tree without changing its structure.
        """
        self.__recover(root=root)


def build_tree() -> TreeNode:
    """
    Helper method to build a sample binary tree for testing.

    Returns:
        TreeNode: The root node of the constructed binary tree.
    """
    root: TreeNode = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    return root


def in_order(root: TreeNode) -> None:
    # Helper function to print the in-order traversal of the binary tree
    if root is None:
        return
    in_order(root.left)
    print(root.val, end="->")
    in_order(root.right)


if __name__ == "__main__":
    root: TreeNode = build_tree()
    solution: Solution = Solution()
    in_order(root=root)
    print("Null")
    solution.recoverTree(root=root)
    in_order(root=root)
    print("Null")
