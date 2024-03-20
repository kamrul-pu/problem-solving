"""
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __helper(self, l: int, r: int, nums: List[int]) -> Optional[TreeNode]:
        """
        Helper function to convert a sorted array to a height-balanced binary search tree.

        Parameters:
            l (int): The left index of the array.
            r (int): The right index of the array.
            nums (List[int]): The sorted array.

        Returns:
            Optional[TreeNode]: The root node of the resulting binary search tree.
        """
        if l > r:
            return None
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = self.__helper(l, mid - 1, nums)
        root.right = self.__helper(mid + 1, r, nums)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Convert a sorted array to a height-balanced binary search tree.

        Parameters:
            nums (List[int]): The sorted array.

        Returns:
            Optional[TreeNode]: The root node of the resulting binary search tree.
        """
        return self.__helper(0, len(nums) - 1, nums)


def in_order(root: TreeNode) -> None:
    """
    Perform inorder traversal of a binary tree and print the values.

    Parameters:
        root (TreeNode): The root of the binary tree.

    Returns:
        None
    """
    if root is None:
        return
    in_order(root.left)
    print(root.val, end="->")
    in_order(root.right)


"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root
        return helper(0, len(nums) - 1)
"""


if __name__ == "__main__":
    nums: List[int] = [-10, -3, 0, 5, 9]
    solution: Solution = Solution()
    root: TreeNode = solution.sortedArrayToBST(nums=nums)
    in_order(root=root)
    print()
