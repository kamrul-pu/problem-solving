"""Left Right View of a Binary Tree"""

from typing import Deque, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __right_view(
        self, node: Optional[TreeNode], level: int, ans: List[int]
    ) -> None:
        """
        Internal method to compute the right view of the binary tree recursively.

        Parameters:
            node (Optional[TreeNode]): The current node.
            level (int): The current level of the node.
            ans (List[int]): The list containing the right view values.
        """
        # Base case: if node is None, return
        if node is None:
            return

        # If the current level is equal to the length of the result list,
        # it means this is the first node encountered at this level, so append its value to the result list.
        if len(ans) == level:
            ans.append(node.val)

        # Recursively traverse the right subtree first, as we are computing the right view.
        # Increment the level for the next recursion.
        self.__right_view(node=node.right, level=level + 1, ans=ans)

        # Recursively traverse the left subtree.
        # Increment the level for the next recursion.
        self.__right_view(node=node.left, level=level + 1, ans=ans)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Method to compute the right view of the binary tree.

        Parameters:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            List[int]: The list containing the values of nodes in the right view.
        """
        ans: List[int] = []
        # Start the recursive traversal from the root node with level 0.
        self.__right_view(node=root, level=0, ans=ans)
        return ans

    def __left_view(self, node: Optional[TreeNode], level: int, ans: List[int]) -> None:
        """
        Internal method to compute the left view of the binary tree recursively.

        Parameters:
            node (Optional[TreeNode]): The current node.
            level (int): The current level of the node.
            ans (List[int]): The list containing the left view values.
        """
        # Base case: if node is None, return
        if node is None:
            return

        # If the current level is equal to the length of the result list,
        # it means this is the first node encountered at this level, so append its value to the result list.
        if len(ans) == level:
            ans.append(node.val)

        # Recursively traverse the left subtree first, as we are computing the left view.
        # Increment the level for the next recursion.
        self.__left_view(node=node.left, level=level + 1, ans=ans)

        # Recursively traverse the right subtree.
        # Increment the level for the next recursion.
        self.__left_view(node=node.right, level=level + 1, ans=ans)

    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Method to compute the left view of the binary tree.

        Parameters:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            List[int]: The list containing the values of nodes in the left view.
        """
        ans: List[int] = []
        # Start the recursive traversal from the root node with level 0.
        self.__left_view(node=root, level=0, ans=ans)
        return ans


def build_tree() -> TreeNode:
    """
    Helper function to build a sample binary tree for testing.

    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    return root


if __name__ == "__main__":
    root: TreeNode = build_tree()
    solution: Solution = Solution()

    # Compute and print the right and left side views of the binary tree
    print(solution.rightSideView(root=root))
    print(solution.leftSideView(root=root))
