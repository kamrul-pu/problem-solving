"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1)
and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting
from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column.
In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
"""

from collections import deque, defaultdict, Counter
from typing import Deque, DefaultDict, List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __f(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize an empty list to store the result
        ans: List[List[int]] = []
        if root is None:
            return ans

        # Initialize a defaultdict to store nodes by their vertical and horizontal positions
        nodes: DefaultDict = defaultdict(lambda: defaultdict(Counter))

        # Initialize a deque for BFS traversal, starting with the root at position (0, 0)
        q: Deque = deque()
        q.append((root, 0, 0))

        # Perform BFS traversal
        while q:
            # Dequeue the front element
            front: Tuple[TreeNode, int, int] = q.popleft()
            node, x, y = front

            # Store the node's value at its position in the defaultdict
            nodes[x][y][node.val] += 1

            # Enqueue left and right children with updated positions
            if node.left:
                q.append((node.left, x - 1, y + 1))
            if node.right:
                q.append((node.right, x + 1, y + 1))

        # Sort and append values from the defaultdict to the result list
        for x, cols in sorted(nodes.items()):
            col = []
            for y, vals in sorted(cols.items()):
                for val, count in sorted(vals.items()):
                    col.extend([val] * count)
            ans.append(col)

        return ans

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Call the private helper function to compute vertical traversal
        return self.__f(root=root)


# Helper function to build a sample binary tree for testing
def build_tree() -> TreeNode:
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.right = TreeNode(10)
    root.left.left = TreeNode(4)
    root.left.left.right = TreeNode(5)
    root.left.left.right.right = TreeNode(6)

    root.right.right = TreeNode(10)
    root.right.left = TreeNode(9)

    return root


# Main program to test the solution
if __name__ == "__main__":
    root: TreeNode = build_tree()
    solution: Solution = Solution()
    print(solution.verticalTraversal(root=root))
