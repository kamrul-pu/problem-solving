"""
Given the root of a binary search tree and an integer k, return true if there exist
two elements in the BST such that their sum is equal to k, or false otherwise.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __inorder(self, node: TreeNode, inorder: List[int]) -> None:
        # Helper method to perform in-order traversal of the BST and store the values in a list.
        if node is None:
            return
        self.__inorder(node=node.left, inorder=inorder)
        inorder.append(node.val)
        self.__inorder(node=node.right, inorder=inorder)

    def __f(self, root: Optional[TreeNode], k: int) -> bool:
        # Helper method to find if there are two elements in the BST that sum up to k.
        inorder: List[int] = []
        # Store the in-order traversal of the BST in the list.
        self.__inorder(node=root, inorder=inorder)
        low: int = 0
        high: int = len(inorder) - 1
        # Use two pointers to find the pair of elements summing up to k.
        while low < high:
            s: int = inorder[low] + inorder[high]
            if s == k:
                return True
            elif s < k:
                low += 1
            else:
                high -= 1

        return False

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Main method to find if there exist two elements in the BST such that their sum is equal to k.
        return self.__f(root=root, k=k)


def build_tree() -> TreeNode:
    """
    Helper method to build a sample binary tree for testing.

    Returns:
        TreeNode: The root node of the constructed binary tree.
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
    solution: Solution = Solution()
    print(solution.findTarget(root=root, k=9))
