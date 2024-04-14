"""Widht of a Complete Binary Tree."""

from collections import deque
from typing import Deque, Optional


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"Node: {self.data} left: {self.left} right: {self.right}"


class Solution:
    def width_of_complete_bt(self, root: Optional[TreeNode]) -> int:
        # If the root is None, return 0 width.
        if root is None:
            return 0

        # Initialize a deque for level-order traversal and add the root to it.
        q: Deque = deque()
        q.append(root)

        # Initialize the level to -1 since we are counting levels from 0.
        level: int = -1

        # Perform level-order traversal.
        while q:
            # Increment the level count for each level.
            level += 1
            # Get the size of the queue, which represents the number of nodes at the current level.
            size: int = len(q)
            # Traverse all nodes at the current level.
            while size > 0:
                size -= 1
                # Pop the node from the left of the queue.
                node: TreeNode = q.popleft()
                # Add left and right children of the current node to the queue if they exist.
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        # The width of a complete binary tree at a given level is 2^level.
        return 2**level


def build_tree() -> TreeNode:
    # Build a sample complete binary tree for testing purposes.
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(10)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(11)
    root.left.left.right = TreeNode(10)
    root.left.right.left = TreeNode(9)
    root.left.right.right = TreeNode(6)
    root.right.left.left = TreeNode(1)
    root.right.left.right = TreeNode(7)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(10)

    return root


if __name__ == "__main__":
    # Build a sample binary tree.
    root: TreeNode = build_tree()
    # Initialize the solution object.
    solution: Solution = Solution()
    # Compute and print the width of the complete binary tree.
    print(solution.width_of_complete_bt(root=root))
