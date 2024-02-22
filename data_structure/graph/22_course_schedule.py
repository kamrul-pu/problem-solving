"""
Detect cycle using topological sort and Kahn's Algorithm.
"""

from collections import deque
from typing import Deque, List


def is_possible(n: int, prerequisities: List[List[int]]) -> bool:
    adj: List[List[int]] = [[] for _ in range(n)]
    for item in prerequisities:
        adj[item[0]].append(item[1])

    # Initialize indegree array for each vertex
    indegree: List[int] = [0] * n

    # Calculate indegree for each vertex
    for i in range(n):
        for item in adj[i]:
            indegree[item] += 1

    # Initialize a queue for BFS
    q: Deque = deque()

    # Enqueue vertices with indegree 0
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    # List to store the topological ordering
    topo: List[int] = []

    # BFS
    while q:
        node = q.popleft()
        topo.append(node)

        # Update indegree for adjacent vertices
        for it in adj[node]:
            indegree[it] -= 1
            if indegree[it] == 0:
                q.append(it)

    return len(topo) == n


if __name__ == "__main__":
    # Example usage:
    g: List[List[int]] = [[1, 0], [2, 1], [3, 2]]
    print(is_possible(n=4, prerequisities=g))
