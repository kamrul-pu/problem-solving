"""
Detect cycle using topological sort and Kahn's Algorithm.
"""

from collections import deque
from typing import Deque, List


def topo_sort(g: List[List[int]], v: int) -> bool:
    """
    Perform topological sorting on a Directed Acyclic Graph (DAG) using BFS Kahn's Algorithm.

    :param g: Adjacency List representing the directed acyclic graph.
    :param v: Number of vertices in the graph.
    :return: True if the graph contains a cycle, False otherwise.
    """
    # Initialize indegree array for each vertex
    indegree: List[int] = [0] * v

    # Calculate indegree for each vertex
    for i in range(v):
        for item in g[i]:
            indegree[item] += 1

    # Initialize a queue for BFS
    q: Deque[int] = deque()

    # Enqueue vertices with indegree 0
    for i in range(v):
        if indegree[i] == 0:
            q.append(i)

    # List to store the topological ordering
    topo: List[int] = []

    # BFS
    while q:
        node = q.popleft()
        topo.append(node)

        # Update indegree for adjacent vertices
        for it in g[node]:
            indegree[it] -= 1
            if indegree[it] == 0:
                q.append(it)

    # If the length of the topological ordering is not equal to the number of vertices, a cycle exists
    return not len(topo) == v


if __name__ == "__main__":
    # Example usage:
    g: List[List[int]] = [
        [1],
        [2],
        [3, 4],
        [1],
        [0],
    ]
    ans: bool = topo_sort(g=g, v=len(g))
    print(ans)
