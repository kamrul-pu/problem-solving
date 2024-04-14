"""
Largest BST in a Binary Tree.
"""

from typing import Optional

# Set the maximum and minimum integer values
INT_MAX: int = float("inf")
INT_MIN: int = float("-inf")


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NodeValue:
    """
    Helper class to store information about the subtree rooted at a node.
    """

    def __init__(self, min_node, max_node, max_size) -> None:
        self.min_node = min_node
        self.max_node = max_node
        self.max_size = max_size


class Solution:
    def __helper(self, node: Optional[TreeNode]) -> NodeValue:
        """
        Recursive helper function to find the largest BST subtree rooted at a given node.

        Parameters:
            node (Optional[TreeNode]): The root of the subtree.

        Returns:
            NodeValue: Information about the subtree rooted at the given node.
        """
        if node is None:
            # Base case: Return [inf, -inf, 0] for null nodes
            return NodeValue(INT_MAX, INT_MIN, 0)

        # Recursively calculate information about the left and right subtrees
        left: NodeValue = self.__helper(node=node.left)
        right: NodeValue = self.__helper(node=node.right)

        # Check if the subtree rooted at the current node is a valid BST
        if left.max_node < node.val and node.val < right.min_node:
            # If valid, update the minimum and maximum values of the subtree
            # and calculate the size of the subtree
            return NodeValue(
                min(node.val, left.min_node),
                max(node.val, right.max_node),
                left.max_size + right.max_size + 1,
            )
        else:
            # If not valid, return [-inf, inf, max(left subtree size, right subtree size)]
            # to ensure that the parent node cannot form a valid BST
            return NodeValue(INT_MIN, INT_MAX, max(left.max_size, right.max_size))

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the size of the largest BST subtree in the given binary tree.

        Parameters:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            int: The size of the largest BST subtree.
        """
        # Call the helper function to find the largest BST subtree rooted at the root
        return self.__helper(node=root).max_size


def build_tree() -> TreeNode:
    """
    Helper function to build a sample binary tree for testing.

    Returns:
        TreeNode: The root node of the constructed binary tree.
    """
    root: TreeNode = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)
    root.right.right = TreeNode(7)
    return root


if __name__ == "__main__":
    # Build the binary tree
    root: TreeNode = build_tree()

    # Create an instance of Solution class
    solution: Solution = Solution()

    # Print the size of the largest BST subtree
    print(solution.largestBSTSubtree(root=root))
