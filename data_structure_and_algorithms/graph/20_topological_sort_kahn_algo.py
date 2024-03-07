"""
Topological sort in python.
Graph Must be DAG -> Directed Acyclic Graph.
Using BFS Kahn's Algorithm
"""

from collections import deque
from typing import Deque, List


def topo_sort(g: List[List[int]], v: int) -> List[int]:
    """
    Perform topological sorting on a Directed Acyclic Graph (DAG) using BFS Kahn's Algorithm.

    :param g: Adjacency List representing the directed acyclic graph.
    :param v: Number of vertices in the graph.
    :return: List representing the topological ordering of nodes.
    """
    indegree: List[int] = [0] * v
    for i in range(v):
        for item in g[i]:
            indegree[item] += 1
    q: Deque = deque()
    for i in range(v):
        if indegree[i] == 0:
            q.append(i)

    topo: List[int] = []
    while q:
        node = q.popleft()
        topo.append(node)

        for it in g[node]:
            indegree[it] -= 1
            if indegree[it] == 0:
                q.append(it)

    return topo


if __name__ == "__main__":
    # Example usage:
    g: List[List[int]] = [[], [], [3], [1], [0, 1], [0, 2]]
    ans: List[int] = topo_sort(g=g, v=len(g))
    print(ans)
