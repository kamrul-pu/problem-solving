"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes
p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a
descendant of itself).”
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __f(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Recursive helper function to find the lowest common ancestor (LCA) node of two given nodes in the binary search tree (BST).

        Parameters:
            node (TreeNode): The current node being processed.
            p (TreeNode): The first node.
            q (TreeNode): The second node.

        Returns:
            TreeNode: The lowest common ancestor node of the given nodes.
        """
        # Base case: if the node is None or equal to either p or q, return the node itself
        if node is None or node == p or node == q:
            return node

        # Recursively search in the left and right subtrees for the LCA node
        left: TreeNode = self.__f(node=node.left, p=p, q=q)
        right: TreeNode = self.__f(node=node.right, p=p, q=q)

        # If both p and q are found in different subtrees, then the current node is the LCA
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return node

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Method to find the lowest common ancestor (LCA) node of two given nodes in the binary search tree (BST).

        Parameters:
            root (TreeNode): The root of the binary search tree.
            p (TreeNode): The first node.
            q (TreeNode): The second node.

        Returns:
            TreeNode: The lowest common ancestor node of the given nodes.
        """
        # Call the helper function to find the LCA node
        return self.__f(node=root, p=p, q=q)


def build_tree() -> TreeNode:
    """
    Helper function to build a sample binary search tree (BST) for testing.

    Returns:
        TreeNode: The root of the constructed binary search tree.
    """
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.left.left = TreeNode(8)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(7)

    return root


if __name__ == "__main__":
    # Build the binary search tree
    root: TreeNode = build_tree()

    # Create an instance of Solution class
    solution: Solution = Solution()

    # Define the nodes for which LCA is to be found
    p: TreeNode = root.right.right.right
    q: TreeNode = root.right.left.left

    # Find and print the lowest common ancestor (LCA) node
    print(solution.lowestCommonAncestor(root=root, p=p, q=q))
