from collections import deque
from typing import Deque, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __f(self, root: Optional[TreeNode]) -> int:
        # Initialize variables to store the maximum width and a deque to perform level-order traversal.
        result: int = 0
        q: Deque = deque()
        # Append the root node along with its position and level to the queue.
        q.append((root, 1, 0))  # (node, number, level)
        # Initialize variables to keep track of the previous level and its position.
        prev_level: int = 0
        prev_num: int = 1
        # Perform level-order traversal.
        while q:
            node, num, level = q.popleft()
            # If we move to the next level, update the previous level and its position.
            if level > prev_level:
                prev_level = level
                prev_num = num
            # Calculate the width at the current level and update the result if it's greater than the previous result.
            result = max(result, num - prev_num + 1)
            # Add the left child to the queue with a position twice that of its parent.
            if node.left:
                q.append((node.left, 2 * num, level + 1))
            # Add the right child to the queue with a position twice that of its parent plus one.
            if node.right:
                q.append((node.right, 2 * num + 1, level + 1))

        return result

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Call the helper function to compute the maximum width of the binary tree.
        return self.__f(root=root)


def build_tree() -> TreeNode:
    """
    Build a sample binary tree for testing purposes.

    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(9)

    return root


if __name__ == "__main__":
    # Build a sample binary tree.
    root: TreeNode = build_tree()
    # Initialize the solution object.
    solution: Solution = Solution()
    # Compute and print the maximum width of the binary tree.
    print(solution.widthOfBinaryTree(root=root))
