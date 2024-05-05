"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them
 A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize a list to store the result (maximum path sum)
        res: List[int] = [root.val]

        # Define a helper function `dfs` to perform depth-first search
        def dfs(root: Optional[TreeNode]) -> int:
            # Base case: If the current node is None (empty), return 0
            if not root:
                return 0

            # Recursive calls to compute the maximum path sum for left and right subtrees
            # If the result of the subtree path sum is negative, consider it as 0 (do not take negative path sums)
            left_max: int = max(dfs(root.left), 0)
            right_max: int = max(dfs(root.right), 0)

            # Calculate the maximum path sum that includes the current node
            # (root.val + left_max + right_max represents a path sum with a split at the current node)
            res[0] = max(res[0], root.val + left_max + right_max)

            # Return the maximum path sum ending at the current node (to be used by parent nodes)
            return root.val + max(left_max, right_max)

        # Start the DFS traversal from the root node
        dfs(root)

        # Return the maximum path sum found (stored in res[0])
        return res[0]


if __name__ == "__main__":
    # Example binary tree:
    #       -10
    #      /   \
    #     9     20
    #          /   \
    #        15     7
    root: TreeNode = TreeNode(
        val=-10,
        left=TreeNode(9),
        right=TreeNode(val=20, left=TreeNode(15), right=TreeNode(7)),
    )

    # Create an instance of the Solution class
    solution: Solution = Solution()

    # Call the maxPathSum function with the root of the binary tree
    print(solution.maxPathSum(root=root))
