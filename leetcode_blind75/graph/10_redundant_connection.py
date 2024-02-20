"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.

"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def __bfs(self, src: int, graph: List[List[int]], visited: List[bool]) -> List[int]:
        visited[src] = True
        q: Deque = deque()
        q.append((src, -1))
        while q:
            front: Tuple = q.popleft()
            node, parent = front
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    q.append((neighbor, node))
                    visited[neighbor] = True
                elif parent != neighbor:
                    return [parent, neighbor]
        return []

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        v: int = len(edges)
        visited: List[bool] = [False] * (v + 1)
        graph: List[List[int]] = [[] for _ in range(v + 1)]

        for edge in edges:
            first, second = edge
            graph[first].append(second)
            graph[second].append(first)

        for i in range(1, v + 1):
            if not visited[i]:
                return self.__bfs(src=i, graph=graph, visited=visited)

        return []


if __name__ == "__main__":
    edges: List[List[int]] = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    soltuion: Solution = Solution()
    print(soltuion.findRedundantConnection(edges=edges))
