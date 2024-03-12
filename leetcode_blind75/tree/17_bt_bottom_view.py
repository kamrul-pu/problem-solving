"""Bottom View of a Binary Tree."""

from collections import deque
from typing import Deque, Dict, List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __f(self, root: Optional[TreeNode]) -> List[int]:
        """
        Internal method to perform the actual bottom view traversal of the binary tree.

        Parameters:
            root (TreeNode): The root of the binary tree.

        Returns:
            List[int]: The list containing the values of nodes in the bottom view.
        """
        ans: List[int] = []
        if root is None:
            return ans

        # Dictionary to store the last encountered value for each vertical line
        mp: Dict[int, int] = dict()

        # Queue for level order traversal with the current vertical line
        q: Deque[Tuple[TreeNode, int]] = deque()
        q.append((root, 0))  # (node, line)

        # Perform level order traversal
        while q:
            front: Tuple[TreeNode, int] = q.popleft()
            node, line = front

            # Update the vertical line with the current node's value
            mp[line] = node.val

            # Enqueue left and right children with updated vertical lines
            if node.left:
                q.append((node.left, line - 1))
            if node.right:
                q.append((node.right, line + 1))

        # Append values from the dictionary to the result list, sorted by vertical lines
        for key in sorted(mp.keys()):
            ans.append(mp[key])
        return ans

    def bottom_view(self, root: Optional[TreeNode]) -> List[int]:
        """
        Method to compute the bottom view traversal of the binary tree.

        Parameters:
            root (TreeNode): The root of the binary tree.

        Returns:
            List[int]: The list containing the values of nodes in the bottom view.
        """
        return self.__f(root=root)


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
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.right.left = TreeNode(8)
    root.left.right.right = TreeNode(9)

    return root


if __name__ == "__main__":
    root: TreeNode = build_tree()
    solution: Solution = Solution()

    # Compute and print the bottom view of the binary tree
    print(solution.bottom_view(root=root))
