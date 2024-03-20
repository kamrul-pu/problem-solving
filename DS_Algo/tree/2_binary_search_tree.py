"""Binary Search Tree Left<Root<Right."""

from typing import Optional, List


class TreeNode:
    def __init__(self, val) -> None:
        """
        Initialize a TreeNode with a given value and left and right children.
        """
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Solution:
    def add_node(self, root: Optional[TreeNode], data) -> None:
        """
        Add a node with the given data to the binary search tree rooted at 'root'.

        Parameters:
            root (Optional[TreeNode]): The root of the binary search tree.
            data: The value to be added to the binary search tree.

        Returns:
            None
        """
        if root.val == data:
            return
        if root.val > data:
            # Add in the left subtree
            if root.left:
                self.add_node(root=root.left, data=data)
            else:
                root.left = TreeNode(val=data)
        else:
            # Add in the right subtree
            if root.right:
                self.add_node(root=root.right, data=data)
            else:
                root.right = TreeNode(val=data)

    def find_node(self, root: Optional[TreeNode], data: int) -> bool:
        """
        Search for a node with the given data in the binary search tree rooted at 'root'.

        Parameters:
            root (Optional[TreeNode]): The root of the binary search tree.
            data: The value to search for.

        Returns:
            bool: True if the node with the given data is found, False otherwise.
        """
        while root is not None and root.val != data:
            if root.val > data:
                root = root.left
            else:
                root = root.right

        if root and root.val == data:
            return True
        return False

    def pre_order(self, root: Optional[TreeNode]) -> None:
        """
        Perform preorder traversal of the binary search tree rooted at 'root' and print the values.

        Parameters:
            root (Optional[TreeNode]): The root of the binary search tree.

        Returns:
            None
        """
        if root is None:
            return
        print(root.val, end="->")
        self.pre_order(root=root.left)
        self.pre_order(root=root.right)

    def in_order(self, root: Optional[TreeNode]) -> None:
        """
        Perform inorder traversal of the binary search tree rooted at 'root' and print the values.

        Parameters:
            root (Optional[TreeNode]): The root of the binary search tree.

        Returns:
            None
        """
        if root is None:
            return
        self.in_order(root=root.left)
        print(root.val, end="->")
        self.in_order(root=root.right)

    def post_order(self, root: Optional[TreeNode]) -> None:
        """
        Perform postorder traversal of the binary search tree rooted at 'root' and print the values.

        Parameters:
            root (Optional[TreeNode]): The root of the binary search tree.

        Returns:
            None
        """
        if root is None:
            return
        self.post_order(root=root.left)
        self.post_order(root=root.right)
        print(root.val, end="->")


if __name__ == "__main__":
    nodes: List[int] = [35, 25, 15, 30, 5, 10]
    root: TreeNode = TreeNode(val=20)
    solution: Solution = Solution()
    for node in nodes:
        solution.add_node(root=root, data=node)
    print("Preorder: ", end="")
    solution.pre_order(root=root)
    print("\nInorder: ", end="")
    solution.in_order(root=root)
    print("\nPostorder: ", end="")
    solution.post_order(root=root)
    print()
    print(solution.find_node(root=root, data=10))
    print(solution.find_node(root=root, data=7))
