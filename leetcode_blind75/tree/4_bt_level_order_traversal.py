"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

from collections import deque
from typing import List, Optional, Deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize an empty list to store the result
        ans: List[List[int]] = []

        # If the root is None, return an empty list
        if root is None:
            return ans

        # Initialize a deque to perform BFS (breadth-first search)
        q: Deque = deque()
        # Add the root node to the queue
        q.append(root)

        # Perform BFS
        while q:
            # Get the number of nodes at the current level
            cur_size: int = len(q)
            # Initialize a list to store the values at the current level
            cur_list: List[int] = []

            # Traverse all nodes at the current level
            while cur_size > 0:
                # Pop the leftmost node from the queue
                node: TreeNode = q.popleft()
                # Append the value of the popped node to the current list
                cur_list.append(node.val)
                # Decrement the size of the current level
                cur_size -= 1

                # Add the left child of the popped node to the queue if exists
                if node.left:
                    q.append(node.left)
                # Add the right child of the popped node to the queue if exists
                if node.right:
                    q.append(node.right)

            # Append the list of values at the current level to the result list
            ans.append(cur_list)

        # Return the result list
        return ans


if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Create a Solution object
    solution: Solution = Solution()
    # Print the level order traversal of the binary tree
    print(solution.levelOrder(root=root))
