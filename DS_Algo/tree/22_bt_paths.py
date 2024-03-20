"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __is_leaf(self, node: Optional[TreeNode]) -> bool:
        """
        Check if the given node is a leaf node.

        Parameters:
            node (Optional[TreeNode]): The node to check.

        Returns:
            bool: True if the node is a leaf node, False otherwise.
        """
        return node.left == None and node.right == None

    def __f(self, node: Optional[TreeNode], ans: List[List[int]], path: str) -> None:
        """
        Perform DFS traversal to find all root-to-leaf paths.

        Parameters:
            node (Optional[TreeNode]): The current node in the traversal.
            ans (List[List[int]]): The list to store the found paths.
            path (str): The current path from root to the current node.

        Returns:
            None
        """
        if node is None:
            return
        path += str(node.val)
        if self.__is_leaf(node=node):
            ans.append(path)
        # Recursively call for left and right children with updated path
        self.__f(node=node.left, ans=ans, path=path + "->")
        self.__f(node=node.right, ans=ans, path=path + "->")

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Find all root-to-leaf paths in the binary tree.

        Parameters:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            List[str]: List of strings representing all root-to-leaf paths.
        """
        ans: List[str] = []
        if root is None:
            return ans
        # Call the private method to perform DFS traversal
        self.__f(node=root, ans=ans, path="")
        return ans


def build_tree() -> TreeNode:
    """
    Helper function to build a sample binary tree for testing.

    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    root: TreeNode = TreeNode(2)
    root.left = TreeNode(35)
    root.right = TreeNode(10)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(2)

    return root


if __name__ == "__main__":
    root: TreeNode = build_tree()
    solution: Solution = Solution()
    print(solution.binaryTreePaths(root=root))
