"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary
tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
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
        preorder: List[int],
        inorder: List[int],
        pre_start: int,
        pre_end: int,
        in_start: int,
        in_end: int,
        mp: DefaultDict,
    ) -> TreeNode:
        """
        Recursively constructs the binary tree using preorder and inorder traversal arrays.

        Parameters:
            preorder (List[int]): The preorder traversal array.
            inorder (List[int]): The inorder traversal array.
            pre_start (int): The start index of the current subtree in the preorder array.
            pre_end (int): The end index of the current subtree in the preorder array.
            in_start (int): The start index of the current subtree in the inorder array.
            in_end (int): The end index of the current subtree in the inorder array.
            mp (DefaultDict): A dictionary mapping values to their indices in the inorder array.

        Returns:
            TreeNode: The root node of the constructed binary tree.
        """
        # Base case: If either start index is greater than end index, return None
        if pre_start > pre_end or in_start > in_end:
            return None

        # Create the current node using the value from the preorder traversal
        node: TreeNode = TreeNode(preorder[pre_start])

        # Find the index of the current node's value in the inorder traversal
        in_root: int = mp[node.val]

        # Calculate the number of nodes in the left subtree
        nums_left: int = in_root - in_start

        # Recursively build the left subtree
        node.left = self.__build(
            preorder,
            inorder,
            pre_start + 1,
            pre_start + nums_left,
            in_start,
            in_root - 1,
            mp,
        )

        # Recursively build the right subtree
        node.right = self.__build(
            preorder,
            inorder,
            pre_start + nums_left + 1,
            pre_end,
            in_root + 1,
            in_end,
            mp,
        )

        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Constructs the binary tree using preorder and inorder traversal arrays.

        Parameters:
            preorder (List[int]): The preorder traversal array.
            inorder (List[int]): The inorder traversal array.

        Returns:
            Optional[TreeNode]: The root node of the constructed binary tree.
        """
        # Create a dictionary mapping values to their indices in the inorder array
        mp: DefaultDict = defaultdict(int)

        for i in range(len(inorder)):
            mp[inorder[i]] = i

        # Construct the binary tree recursively
        root: TreeNode = self.__build(
            preorder=preorder,
            inorder=inorder,
            pre_start=0,
            pre_end=len(preorder) - 1,
            in_start=0,
            in_end=len(inorder) - 1,
            mp=mp,
        )
        return root


if __name__ == "__main__":
    # Example usage
    preorder: List[int] = [3, 9, 20, 15, 7]
    inorder: List[int] = [9, 3, 15, 20, 7]
    solution: Solution = Solution()
    root: TreeNode = solution.buildTree(preorder=preorder, inorder=inorder)
    print(root.val)
