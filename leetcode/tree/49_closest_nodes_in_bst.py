"""
You are given the root of a binary search tree and an array queries of size n consisting of positive integers.

Find a 2D array answer of size n where answer[i] = [mini, maxi]:

mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.
Return the array answer.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Helper function to perform in-order traversal of the BST
    # and collect the values in a sorted list.
    def __in(self, node: Optional[TreeNode], vals: List[int]) -> None:
        if node is None:
            return

        # Traverse the left subtree
        self.__in(node.left, vals)

        # Visit the current node
        vals.append(node.val)

        # Traverse the right subtree
        self.__in(node.right, vals)

    # Helper function to perform binary search on the sorted list of values
    # to find the closest values relative to the given query.
    def __bs(self, vals: List[int], n: int, q: int) -> List[int]:
        ans: List[int] = [-1, -1]  # Initialize result list with -1
        lo, hi = 0, n - 1

        while lo <= hi:
            mid: int = (lo + hi) // 2  # Calculate the middle index

            if vals[mid] == q:
                # If the value at mid is exactly equal to the query, return it as both mini and maxi
                ans[0] = ans[1] = vals[mid]
                break
            elif vals[mid] > q:
                # If the value at mid is greater than the query, update maxi and search the left half
                ans[1] = vals[mid]
                hi = mid - 1
            else:
                # If the value at mid is less than the query, update mini and search the right half
                ans[0] = vals[mid]
                lo = mid + 1

        return ans

    # Main function to find closest nodes for each query.
    def closestNodes(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[List[int]]:
        vals: List[int] = []

        # Perform in-order traversal to get all values in sorted order
        self.__in(root, vals)

        n: int = len(vals)  # Get the number of elements in the sorted list
        result: List[List[int]] = []

        # For each query, find the closest nodes using binary search
        for q in queries:
            result.append(self.__bs(vals, n, q))

        return result


# Function to build a sample binary search tree
def build_tree() -> Optional[TreeNode]:
    root: TreeNode = TreeNode(
        6,
        left=TreeNode(2, left=TreeNode(1), right=TreeNode(4)),
        right=TreeNode(13, left=TreeNode(9), right=TreeNode(15, left=TreeNode(14))),
    )
    return root


# Main driver code
if __name__ == "__main__":
    root: TreeNode = build_tree()  # Build the binary search tree
    queries: List[int] = [2, 5, 16]  # List of queries to process
    solution: Solution = Solution()  # Create an instance of the Solution class
    result: List[int] = solution.closestNodes(
        root, queries
    )  # Get the result for the queries
    print(result)  # Print the result
