"""Binary Tree data structure in python."""

from typing import List, Optional


class TreeNode:
    def __init__(self, val) -> None:
        """
        Initialize a TreeNode with a given value.
        """
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform inorder traversal on the binary tree and return the result.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: The list containing the inorder traversal of the binary tree.
        """
        result: List[int] = []
        self.__inorder(root, result)
        return result

    def __inorder(self, root: Optional[TreeNode], result: List[int]) -> None:
        """
        Helper function to perform inorder traversal recursively.

        Parameters:
            root (Optional[TreeNode]): The current node being visited.
            result (List[int]): The list to store the inorder traversal.

        Returns:
            None
        """
        if root is None:
            return
        self.__inorder(root.left, result)
        result.append(root.val)
        self.__inorder(root.right, result)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform preorder traversal on the binary tree and return the result.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: The list containing the preorder traversal of the binary tree.
        """
        result: List[int] = []
        self.__preorder(root, result)
        return result

    def __preorder(self, root: Optional[TreeNode], result: List[int]) -> None:
        """
        Helper function to perform preorder traversal recursively.

        Parameters:
            root (Optional[TreeNode]): The current node being visited.
            result (List[int]): The list to store the preorder traversal.

        Returns:
            None
        """
        if root is None:
            return
        result.append(root.val)
        self.__preorder(root.left, result)
        self.__preorder(root.right, result)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform postorder traversal on the binary tree and return the result.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: The list containing the postorder traversal of the binary tree.
        """
        result: List[int] = []
        self.__postorder(root, result)
        return result

    def __postorder(self, root: Optional[TreeNode], result: List[int]) -> None:
        """
        Helper function to perform postorder traversal recursively.

        Parameters:
            root (Optional[TreeNode]): The current node being visited.
            result (List[int]): The list to store the postorder traversal.

        Returns:
            None
        """
        if root is None:
            return
        self.__postorder(root.left, result)
        self.__postorder(root.right, result)
        result.append(root.val)


def build_tree() -> TreeNode:
    """
    Build a sample binary tree and return the root node.
    """
    root: TreeNode = TreeNode(val=10)
    n1: TreeNode = TreeNode(val=30)
    n2: TreeNode = TreeNode(val=20)
    n3: TreeNode = TreeNode(val=5)
    n4: TreeNode = TreeNode(val=15)
    n5: TreeNode = TreeNode(val=25)
    n6: TreeNode = TreeNode(val=35)
    root.left = n1
    root.right = n2
    root.left.left = n3
    root.left.right = n4
    root.right.left = n5
    root.right.right = n6

    return root


if __name__ == "__main__":
    root: TreeNode = build_tree()
    solution: Solution = Solution()
    inorder: List[int] = solution.inorderTraversal(root)
    print("Inorder Traversal:", inorder)
    preorder: List[int] = solution.preorderTraversal(root)
    print("Preorder Traversal:", preorder)
    postorder: List[int] = solution.postorderTraversal(root)
    print("Postorder Traversal:", postorder)
