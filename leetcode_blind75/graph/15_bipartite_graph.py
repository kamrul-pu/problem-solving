"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.
"""

from collections import deque
from typing import Deque, List


class Solution:
    def __f(self, graph: List[List[int]], start: int, color: List[int]) -> bool:
        # Initialize colors for each node (-1: not colored, 0: color A, 1: color B)
        q: Deque = deque()
        q.append(start)  # Start BFS from the first node
        color[start] = 0  # Color the first node as A

        while q:
            node: int = q.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # Neighbor is not colored yet
                    # Color the neighbor with the opposite color of the current node
                    color[neighbor] = int(not color[node])
                    q.append(neighbor)
                # Neighbor has the same color as the current node
                elif color[neighbor] == color[node]:
                    return False  # Graph is not bipartite

        return True  # All nodes are colored in a bipartite manner

    def __dfs(
        self, node: int, col: int, color: List[int], graph: List[List[int]]
    ) -> bool:
        color[node] = col  # Color the current node with the specified color
        # Explore neighbors of the current node
        for neighbor in graph[node]:
            if color[neighbor] == -1:  # Neighbor is not colored yet
                # Recursively explore the neighbor node with the opposite color
                if not self.__dfs(neighbor, not col, color, graph):
                    return False
            elif color[neighbor] == color[node]:  # Neighbor has the same color
                return False  # Not bipartite

        return True  # All neighbors are colored with different colors

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n: int = len(graph)
        color: List[int] = [-1] * n
        for node in range(n):
            if color[node] == -1:  # node is unvisted
                # if not self.__f(graph=graph, start=node, color=color):
                #     return False  # not bipartite
                if not self.__dfs(node=node, col=0, color=color, graph=graph):
                    return False

        return True


if __name__ == "__main__":
    graph: List[List[int]] = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    # graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    graph = [
        [],
        [2, 4, 6],
        [1, 4, 8, 9],
        [7, 8],
        [1, 2, 8, 9],
        [6, 9],
        [1, 5, 7, 8, 9],
        [3, 6, 9],
        [2, 3, 4, 6, 9],
        [2, 4, 5, 6, 7, 8],
    ]

    solution: Solution = Solution()
    print(solution.isBipartite(graph=graph))
