"""Binary Tree Traversal recursively."""

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
        return self.__inorder(root)

    def __inorder(self, root: Optional[TreeNode]) -> List[int]:
        """
        Helper function to perform inorder traversal recursively.

        Parameters:
            root (Optional[TreeNode]): The current node being visited.

        Returns:
            List[int]: The list to store the inorder traversal.
        """
        result: List[int] = []
        if root is None:
            return result

        current: TreeNode = root
        stack: List[TreeNode] = []
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                result.append(current.val)
                current = current.right
            else:
                break

        return result

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform preorder traversal on the binary tree and return the result.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: The list containing the preorder traversal of the binary tree.
        """
        return self.__preorder(root=root)

    def __preorder(self, root: Optional[TreeNode]) -> List[int]:
        """
        Helper function to perform preorder traversal iteratively.

        Parameters:
            root (Optional[TreeNode]): The current node being visited.

        Returns:
            List[int]: The list to store the preorder traversal.
        """
        result: List[int] = []
        if root is None:
            return result
        st: List[int] = []
        st.append(root)
        while st:
            top: TreeNode = st.pop()
            result.append(top.val)
            if top.right:
                st.append(top.right)
            if top.left:
                st.append(top.left)

        return result

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform postorder traversal on the binary tree and return the result.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: The list containing the postorder traversal of the binary tree.
        """
        # return self.__postorder(root=root)
        return self.__postorder_single(root=root)

    def __postorder_single(self, root: Optional[TreeNode]) -> List[int]:
        """
        Helper function to perform postorder traversal iteratively using a single stack.

        Parameters:
            root (Optional[TreeNode]): The current node being visited.

        Returns:
            List[int]: The list to store the postorder traversal.
        """
        result: List[int] = []
        if root is None:
            return result

        curr: TreeNode = root
        stack: List[TreeNode] = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                temp: TreeNode = stack[-1].right
                if temp is None:
                    temp = stack.pop()
                    result.append(temp.val)
                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        result.append(temp.val)
                else:
                    curr = temp

        return result

    def __postorder(self, root: Optional[TreeNode]) -> List[int]:
        """
        Helper function to perform postorder traversal recursively.

        Parameters:
            root (Optional[TreeNode]): The current node being visited.

        Returns:
            List[int]: The list to store the postorder traversal.
        """
        if root is None:
            return []

        stack1: List[TreeNode] = []
        stack2: List[int] = []
        stack1.append(root)
        while stack1:
            node: TreeNode = stack1.pop()
            stack2.append(node.val)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        return stack2[::-1]


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
    # Build a binary tree
    root: TreeNode = build_tree()
    # Create a Solution object
    solution: Solution = Solution()
    # Perform inorder traversal and print the result
    inorder: List[int] = solution.inorderTraversal(root)
    print("Inorder Traversal:", inorder)
    # Perform preorder traversal and print the result
    preorder: List[int] = solution.preorderTraversal(root)
    print("Preorder Traversal:", preorder)
    # Perform postorder traversal and print the result
    postorder: List[int] = solution.postorderTraversal(root)
    print("Postorder Traversal:", postorder)
