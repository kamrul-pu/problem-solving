"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p
and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        """
        Initialize a tree node with the given value and optional left and right children.

        Parameters:
            x (int): The value of the node.
        """
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __f(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Helper method to find the lowest common ancestor (LCA) node of two given nodes in the BST.

        Parameters:
            node (TreeNode): The current node being processed.
            p (TreeNode): The first node whose LCA needs to be found.
            q (TreeNode): The second node whose LCA needs to be found.

        Returns:
            TreeNode: The lowest common ancestor (LCA) node of the given nodes.
        """
        if node is None:
            return None
        curr: int = node.val
        if curr < p.val and curr < q.val:
            return self.__f(node=node.right, p=p, q=q)
        if curr > p.val and curr > q.val:
            return self.__f(node=node.left, p=p, q=q)

        return node

    def __lca(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        """
        Helper method to find the lowest common ancestor (LCA) node of two given nodes in the BST iteratively.

        Parameters:
            root (TreeNode): The root node of the binary search tree.
            p (TreeNode): The first node whose LCA needs to be found.
            q (TreeNode): The second node whose LCA needs to be found.

        Returns:
            TreeNode: The lowest common ancestor (LCA) node of the given nodes.
        """
        curr: TreeNode = root
        while curr:
            # If both p and q are greater than the current node's value, move to the right subtree
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            # If both p and q are less than the current node's value, move to the left subtree
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            # If the current node's value falls between p and q, or one of them equals the current node's value,
            # it means that the current node is the lowest common ancestor (LCA), so return the current node
            else:
                return curr
        # If no LCA is found (e.g., if the tree is empty or the nodes p and q are not in the tree), return None
        return None

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Finds the lowest common ancestor (LCA) node of two given nodes in the BST.

        Parameters:
            root (TreeNode): The root node of the binary search tree.
            p (TreeNode): The first node whose LCA needs to be found.
            q (TreeNode): The second node whose LCA needs to be found.

        Returns:
            TreeNode: The lowest common ancestor (LCA) node of the given nodes.
        """
        return self.__f(node=root, p=p, q=q)


def build_tree() -> TreeNode:
    """
    Helper method to build a sample binary tree for testing.

    Returns:
        TreeNode: The root node of the constructed binary tree.
    """
    root: TreeNode = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    return root


if __name__ == "__main__":
    # Build the binary search tree
    root: TreeNode = build_tree()

    # Create an instance of Solution class
    solution: Solution = Solution()

    # Define the nodes for which LCA is to be found
    p: TreeNode = root.left.left
    q: TreeNode = root.left.right

    # Find and print the lowest common ancestor (LCA) node
    print(solution.lowestCommonAncestor(root=root, p=p, q=q).val)
