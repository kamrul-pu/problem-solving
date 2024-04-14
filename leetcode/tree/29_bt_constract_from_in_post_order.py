"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree
and postorder is the postorder traversal of the same tree, construct and return the binary tree.
"""

from collections import defaultdict
from typing import DefaultDict, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a tree node with the given value and optional left and right children.

        Parameters:
            val (int): The value of the node.
            left (Optional[TreeNode]): The left child node.
            right (Optional[TreeNode]): The right child node.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __build(
        self,
        inorder: List[int],
        in_start: int,
        in_end: int,
        postorder: List[int],
        p_start: int,
        p_end: int,
        mp: DefaultDict,
    ) -> TreeNode:
        """
        Recursively constructs the binary tree using inorder and postorder traversal arrays.

        Parameters:
            inorder (List[int]): The inorder traversal array.
            in_start (int): The start index of the current subtree in the inorder array.
            in_end (int): The end index of the current subtree in the inorder array.
            postorder (List[int]): The postorder traversal array.
            p_start (int): The start index of the current subtree in the postorder array.
            p_end (int): The end index of the current subtree in the postorder array.
            mp (DefaultDict): A dictionary mapping values to their indices in the inorder array.

        Returns:
            TreeNode: The root node of the constructed binary tree.
        """
        # Base case: If either start index is greater than end index, return None
        if p_start > p_end or in_start > in_end:
            return None

        # Create the current node using the value from the postorder traversal
        node: TreeNode = TreeNode(postorder[p_end])

        # Find the index of the current node's value in the inorder traversal
        index_root: int = mp[postorder[p_end]]

        # Calculate the number of nodes in the left subtree
        nums_left: int = index_root - in_start

        # Recursively build the left subtree
        node.left = self.__build(
            inorder,
            in_start,
            index_root - 1,
            postorder,
            p_start,
            p_start + nums_left - 1,
            mp,
        )

        # Recursively build the right subtree
        node.right = self.__build(
            inorder,
            index_root + 1,
            in_end,
            postorder,
            p_start + nums_left,
            p_end - 1,
            mp,
        )

        return node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Constructs the binary tree using inorder and postorder traversal arrays.

        Parameters:
            inorder (List[int]): The inorder traversal array.
            postorder (List[int]): The postorder traversal array.

        Returns:
            Optional[TreeNode]: The root node of the constructed binary tree.
        """
        # Check if the input lists are of the same length
        if len(inorder) != len(postorder):
            return None

        # Create a dictionary mapping values to their indices in the inorder array
        mp: DefaultDict = defaultdict(int)
        n: int = len(inorder)
        for i in range(n):
            mp[inorder[i]] = i

        # Construct the binary tree recursively
        root: TreeNode = self.__build(inorder, 0, n - 1, postorder, 0, n - 1, mp)
        return root


if __name__ == "__main__":
    # Example usage
    inorder: List[int] = [9, 3, 15, 20, 7]
    postorder: List[int] = [9, 15, 7, 20, 3]
    solution: Solution = Solution()
    root: TreeNode = solution.buildTree(inorder=inorder, postorder=postorder)
    print(root.val if root else None)
