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
    i: int = 0

    def __inorder(self, node: Optional[TreeNode], inorder: List[int]) -> None:
        # Perform in-order traversal of the BST to construct the list of values in sorted order
        if node is None:
            return
        self.__inorder(node=node.left, inorder=inorder)
        inorder.append(node.val)
        self.__inorder(node=node.right, inorder=inorder)

    def __f(self, node: Optional[TreeNode], inorder: List[int]) -> None:
        # Correct the misplaced nodes by comparing with the sorted list of values
        if node is None:
            return
        self.__f(node=node.left, inorder=inorder)
        if node.val != inorder[self.i]:
            node.val = inorder[self.i]
        self.i += 1
        self.__f(node=node.right, inorder=inorder)

    def __recover(self, root: Optional[TreeNode]) -> None:
        # Recover the tree by performing in-order traversal and correcting the misplaced nodes
        inorder: List[int] = []
        self.__inorder(node=root, inorder=inorder)
        inorder.sort()
        self.__f(node=root, inorder=inorder)

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
