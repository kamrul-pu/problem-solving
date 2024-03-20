"""
Given the root of a binary search tree, and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.
"""

from typing import List, Optional


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
    def __in_order(self, node: Optional[TreeNode], vals: List[int]) -> None:
        """
        Perform an in-order traversal of the binary search tree and store node values in a list.

        Parameters:
            node (Optional[TreeNode]): The current node in the traversal.
            vals (List[int]): List to store the node values.

        Returns:
            None
        """
        if node is None:
            return
        self.__in_order(node=node.left, vals=vals)
        vals.append(node.val)
        self.__in_order(node=node.right, vals=vals)

    def __f(self, node: Optional[TreeNode], vals: List[int], k: int) -> None:
        """
        Helper method to find the kth smallest value in the binary search tree.

        Parameters:
            node (Optional[TreeNode]): The current node in the traversal.
            vals (List[int]): List to store traversal progress and result.
            k (int): The kth smallest value to find.

        Returns:
            None
        """
        if node is None:
            return
        self.__f(node=node.left, vals=vals, k=k)
        vals[0] += 1
        if vals[0] == k:
            vals.append(node.val)
        self.__f(node=node.right, vals=vals, k=k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Find the kth smallest value in the binary search tree.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary search tree.
            k (int): The kth smallest value to find.

        Returns:
            int: The kth smallest value.
        """
        vals: List[int] = [0]
        self.__f(node=root, vals=vals, k=k)
        return vals[1]

    def kth_largest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Find the kth largest value in the binary search tree.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary search tree.
            k (int): The kth largest value to find.

        Returns:
            int: The kth largest value.
        """
        vals: List[int] = []
        self.__in_order(node=root, vals=vals)
        n: int = len(vals)
        return vals[n - k]


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
    k: int = 3
    solution: Solution = Solution()
    print(solution.kthSmallest(root=root, k=k))
    print(solution.kth_largest(root=root, k=k))
