"""Binary tree root to a node path."""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __get_path(self, node: Optional[TreeNode], ans: List[int], x: int) -> bool:
        """
        Internal method to recursively find the path from the root to a given node in a binary tree.

        Parameters:
            node (Optional[TreeNode]): Current node being visited.
            ans (List[int]): Current path from root to the current node.
            x (int): Value of the target node.

        Returns:
            bool: True if the target node is found in the subtree rooted at the current node, False otherwise.
        """
        # Base case: if the node is None, return False indicating that the target node is not found
        if node is None:
            return False

        # Append the value of the current node to the path
        ans.append(node.val)

        # If the current node is the target node, return True
        if node.val == x:
            return True

        # Recursively search in the left subtree and right subtree
        # If the target node is found in either subtree, return True
        if self.__get_path(node=node.left, ans=ans, x=x) or self.__get_path(
            node=node.right, ans=ans, x=x
        ):
            return True

        # If the target node is not found in the current subtree, backtrack by removing the current node from the path
        ans.pop()
        return False

    def rootToNode(self, root: Optional[TreeNode], x: int) -> List[int]:
        """
        Method to find the path from the root to a given node in a binary tree.

        Parameters:
            root (Optional[TreeNode]): The root of the binary tree.
            x (int): Value of the target node.

        Returns:
            List[int]: The path from the root to the target node.
        """
        ans: List[int] = []
        self.__get_path(node=root, ans=ans, x=x)
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
    root.left.right.right = TreeNode(7)

    return root


if __name__ == "__main__":
    root: TreeNode = build_tree()
    x: int = 7
    solution: Solution = Solution()
    print(solution.rootToNode(root=root, x=x))
