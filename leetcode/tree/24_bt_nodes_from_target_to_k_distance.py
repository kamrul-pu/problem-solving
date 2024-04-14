"""
Given the root of a binary tree, the value of a target node target, and an integer k,
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
"""

from collections import deque, defaultdict
from typing import DefaultDict, Deque, List


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
    def __mark_parents(self, root: TreeNode, parent: DefaultDict) -> None:
        """
        Helper method to mark parents of all nodes in the binary tree.

        Parameters:
            root (TreeNode): The root of the binary tree.
            parent (DefaultDict): Dictionary to store the parent nodes.

        Returns:
            None
        """
        q: Deque = deque()
        q.append(root)

        # Traverse the binary tree in BFS manner to mark parents
        while q:
            node: TreeNode = q.popleft()
            if node.left:
                parent[node.left] = node
                q.append(node.left)
            if node.right:
                parent[node.right] = node
                q.append(node.right)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Find all nodes at distance k from the target node in the binary tree.

        Parameters:
            root (TreeNode): The root of the binary tree.
            target (TreeNode): The target node from which distance k nodes are to be found.
            k (int): The distance from the target node.

        Returns:
            List[int]: A list of values of nodes at distance k from the target node.
        """
        parent: DefaultDict = defaultdict()

        # Mark parents of all nodes in the binary tree
        self.__mark_parents(root=root, parent=parent)

        q: Deque = deque()
        q.append(target)
        visited: DefaultDict = defaultdict(bool)
        visited[target] = True
        level: int = 0

        # Perform BFS traversal starting from the target node to find nodes at distance k
        while q:
            size: int = len(q)
            if level == k:
                break
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

        # Retrieve values of nodes at distance k
        result: List[int] = []
        while q:
            node: TreeNode = q.popleft()
            result.append(node.val)

        return result


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
    k: int = 2
    # Create an instance of the solution class
    solution: Solution = Solution()
    # Find nodes at distance k from the target node
    result: List[int] = solution.distanceK(root=root, target=target, k=k)
    # Print the result
    print(result)
