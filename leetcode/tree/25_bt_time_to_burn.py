"""
You are given the root of a binary tree with unique values, and an integer start. At minute 0,
an infection starts from the node with value start.

Each minute, a node becomes infected if:
The node is currently uninfected.
The node is adjacent to an infected node.

Return the number of minutes needed for the entire tree to be infected.
"""

from collections import deque, defaultdict
from typing import DefaultDict, Deque, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        """
        Initialize a tree node with the given value.

        Parameters:
            x: The value of the node.
        """
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __mark_parents(
        self, root: TreeNode, parent: DefaultDict, start: int
    ) -> TreeNode:
        """
        Helper method to mark parents of all nodes in the binary tree and find the target node.

        Parameters:
            root (TreeNode): The root of the binary tree.
            parent (DefaultDict): Dictionary to store the parent nodes.
            start (int): The value of the node from which the infection starts.

        Returns:
            TreeNode: The target node where the infection starts.
        """
        q: Deque = deque()
        q.append(root)
        target: TreeNode = None

        # Traverse the binary tree in BFS manner to mark parents and find the target node
        while q:
            node: TreeNode = q.popleft()
            if node.val == start:
                target = node
            if node.left:
                parent[node.left] = node
                q.append(node.left)
            if node.right:
                parent[node.right] = node
                q.append(node.right)
        return target

    def __f(self, target: TreeNode, parent: DefaultDict) -> int:
        """
        Perform BFS traversal to calculate the number of minutes needed for the entire tree to be infected.

        Parameters:
            target (TreeNode): The target node where the infection starts.
            parent (DefaultDict): Dictionary containing parent nodes.

        Returns:
            int: The number of minutes needed for the entire tree to be infected.
        """
        q: Deque = deque()
        q.append(target)
        visited: DefaultDict = defaultdict(bool)
        visited[target] = True
        level: int = 0

        # Perform BFS traversal starting from the target node to find nodes at distance k
        while q:
            size: int = len(q)
            level += 1
            while size > 0:
                size -= 1
                node: TreeNode = q.popleft()

                # Enqueue left and right children if not visited
                if node.left and not visited[node.left]:
                    q.append(node.left)
                    visited[node.left] = True
                if node.right and not visited[node.right]:
                    q.append(node.right)
                    visited[node.right] = True

                # Enqueue parent node if not visited
                if node in parent and not visited[parent[node]]:
                    q.append(parent[node])
                    visited[parent[node]] = True
        return level - 1

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
        Calculate the number of minutes needed for the entire tree to be infected.

        Parameters:
            root (Optional[TreeNode]): The root of the binary tree.
            start (int): The value of the node from which the infection starts.

        Returns:
            int: The number of minutes needed for the entire tree to be infected.
        """
        parent: DefaultDict = defaultdict()
        target: TreeNode = self.__mark_parents(root=root, parent=parent, start=start)
        if target is None:
            return 0
        return self.__f(target=target, parent=parent)


def build_tree() -> TreeNode:
    """
    Helper function to build a sample binary tree for testing.

    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    root: TreeNode = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    return root


if __name__ == "__main__":
    # Build the binary tree
    root: TreeNode = build_tree()
    # Define the target node and distance
    target: TreeNode = root.left
    # Create an instance of the solution class
    solution: Solution = Solution()
    # Calculate the number of minutes needed for the entire tree to be infected
    print(solution.amountOfTime(root=root, start=3))
