"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __f(self, node: TreeNode, max_val) -> int:
        # Recursive helper function to count good nodes
        if node is None:
            return 0

        # Check if the current node is a good node
        # A node is good if its value is greater than or equal to the maximum value
        # in the path from the root to this node
        res: int = 1 if node.val >= max_val else 0

        # Update the maximum value encountered so far in the path
        max_val = max(max_val, node.val)

        # Recursively count good nodes in the left subtree
        res += self.__f(node.left, max_val)

        # Recursively count good nodes in the right subtree
        res += self.__f(node.right, max_val)

        return res

    def goodNodes(self, root: TreeNode) -> int:
        # Main function to count good nodes in the binary tree
        # Start from the root node with an initial maximum value of negative infinity
        return self.__f(node=root, max_val=float("-inf"))


if __name__ == "__main__":
    # Example usage:
    # Create a binary tree
    root: TreeNode = TreeNode(
        val=3,
        left=TreeNode(1, TreeNode(3)),
        right=TreeNode(4, TreeNode(1), TreeNode(4)),
    )

    # Initialize the solution object
    solution: Solution = Solution()

    # Count the number of good nodes in the binary tree
    print(solution.goodNodes(root=root))
