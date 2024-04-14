"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

"""

from collections import deque
from typing import Deque, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a TreeNode with a value and optional left and right children.

        Args:
            val (int, optional): Value of the node. Defaults to 0.
            left (TreeNode, optional): Left child of the node. Defaults to None.
            right (TreeNode, optional): Right child of the node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __f(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform zigzag level order traversal of the binary tree.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            List[List[int]]: The zigzag level order traversal of the binary tree.
        """
        ans: List[List[int]] = []  # Initialize the result list
        if root is None:
            return ans  # Return empty list if the tree is empty
        q: Deque = deque()  # Initialize a deque to perform level order traversal
        q.append(root)  # Add the root node to the deque
        flag: bool = (
            True  # Flag to alternate between left-to-right and right-to-left traversal
        )
        while q:
            cur_list: List[int] = []  # Initialize list to store current level nodes
            size: int = len(q)  # Get the current size of the deque
            while size > 0:  # Process all nodes at the current level
                size -= 1
                node: TreeNode = q.popleft()  # Pop the leftmost node from the deque
                cur_list.append(
                    node.val
                )  # Append the value of the node to the current level list
                if node.left:
                    q.append(node.left)  # Add the left child to the deque if it exists
                if node.right:
                    q.append(
                        node.right
                    )  # Add the right child to the deque if it exists
            if flag:
                ans.append(
                    cur_list
                )  # Append the current level list as is if flag is True
            else:
                ans.append(
                    cur_list[::-1]
                )  # Append the current level list in reverse order if flag is False
            flag = not flag  # Toggle the flag for the next level

        return ans

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Wrapper function to perform zigzag level order traversal of the binary tree.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            List[List[int]]: The zigzag level order traversal of the binary tree.
        """
        return self.__f(root=root)


def build_tree() -> TreeNode:
    """
    Build a sample binary tree for testing purposes.

    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    return root


if __name__ == "__main__":
    root: TreeNode = build_tree()
    solution: Solution = Solution()
    ans: List[List[int]] = solution.zigzagLevelOrder(root=root)
    print(ans)
