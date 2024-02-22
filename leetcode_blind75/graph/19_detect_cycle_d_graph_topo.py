"""
Detect cycle using topological sort and Kahn's Algorithm.
"""

from collections import deque
from typing import Deque, List


class Solution:
    def __f(self, g: List[List[int]]) -> bool:
        """
        Detects a cycle in the directed graph using topological sort and Kahn's algorithm.

        Args:
        - g (List[List[int]]): The adjacency list representation of the directed graph.

        Returns:
        - bool: True if the graph contains a cycle, False otherwise.
        """
        # Get the number of nodes in the graph
        n: int = len(g)

        # Initialize a list to store the in-degree of each node
        indegree: List[int] = [0] * n

        # Calculate the in-degree of each node
        for node in range(n):
            for neighbor in g[node]:
                indegree[neighbor] += 1

        # Initialize a deque to perform BFS
        q: Deque = deque()

        # Enqueue nodes with in-degree zero
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)

        # Initialize a list to store the topological ordering
        topo: List[int] = []

        # Perform BFS-based topological sorting
        while q:
            # Dequeue a node
            node: int = q.popleft()

            # Append the dequeued node to the topological ordering
            topo.append(node)

            # Update the in-degree of its neighbors and enqueue them if their in-degree becomes zero
            for neighbor in g[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # If the length of the topological ordering is not equal to the number of nodes, there is a cycle
        return not len(topo) == n

    def is_cycle(self, g: List[List[int]]) -> bool:
        """
        Determines whether a directed graph contains a cycle.

        Args:
        - g (List[List[int]]): The adjacency list representation of the directed graph.

        Returns:
        - bool: True if the graph contains a cycle, False otherwise.
        """
        return self.__f(g=g)


if __name__ == "__main__":
    g: List[List[int]] = [
        [1],
        [2],
        [3, 4],
        [1],
        [0],
    ]
    solution: Solution = Solution()
    print(solution.is_cycle(g=g))
