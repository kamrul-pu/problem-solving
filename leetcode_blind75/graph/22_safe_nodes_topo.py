"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1.
The graph is represented by a 0-indexed 2D integer array graph where graph[i]
is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges.
A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
"""

from collections import deque
from typing import Deque, List


class Solution:
    def __dfs(
        self,
        node: int,
        graph: List[int],
        vis: List[int],
        path_vis: List[int],
        check: List[int],
    ) -> bool:
        # Depth-first search to check if a node is safe
        vis[node] = True  # Mark the node as visited
        path_vis[node] = True  # Mark the node as visited in the current path

        # Traverse through the neighbors of the current node
        for neighbor in graph[node]:
            if not vis[neighbor]:
                # If the neighbor hasn't been visited, recursively explore it
                if self.__dfs(neighbor, graph, vis, path_vis, check):
                    # If the neighbor leads to a cycle, mark the current node as unsafe
                    check[node] = False
                    return True
            elif path_vis[neighbor]:
                # If the neighbor is visited in the current path, it leads to a cycle
                check[node] = False
                return True

        # After exploring all neighbors and no cycles are found, mark the node as safe
        check[node] = True
        path_vis[node] = False  # Mark the node as not visited in the current path
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n: int = len(graph)
        # vis: List[bool] = [False] * n
        # path_vis: List[bool] = [False] * n
        # check: List[bool] = [False] * n
        # for node in range(n):
        #     if not vis[node]:
        #         self.__dfs(
        #             node=node, graph=graph, vis=vis, path_vis=path_vis, check=check
        #         )

        # safe_nodes: List[int] = []
        # for i in range(n):
        #     if check[i]:
        #         safe_nodes.append(i)

        # return safe_nodes
        return self.__find_safe_nodes(v=n, graph=graph)

    def __find_safe_nodes(self, v: int, graph: List[List[int]]) -> List[int]:
        # Reverse the graph and perform topological sort to find safe nodes

        graph_rev: List[List[int]] = [[] for _ in range(v)]  # Reversed graph
        indegree: List[int] = [0] * v  # Indegree of nodes
        safe_nodes: List[int] = []  # List to store safe nodes

        # Construct the reversed graph and calculate indegrees
        for node in range(v):
            for neighbor in graph[node]:
                graph_rev[neighbor].append(node)
                indegree[node] += 1

        # Initialize a queue for topological sorting
        q: Deque = deque()

        # Initialize the queue with nodes having indegree 0
        for node in range(v):
            if indegree[node] == 0:
                q.append(node)

        # Perform topological sorting
        while q:
            node: int = q.popleft()  # Pop a node with indegree 0
            safe_nodes.append(node)  # Add the node to the list of safe nodes
            for neighbor in graph_rev[node]:
                indegree[neighbor] -= 1  # Decrement the indegree of neighbors
                if indegree[neighbor] == 0:
                    q.append(
                        neighbor
                    )  # If neighbor's indegree becomes 0, add it to the queue

        safe_nodes.sort()  # Sort the safe nodes in ascending order
        return safe_nodes


if __name__ == "__main__":
    graph: List[List[int]] = [[1, 2], [2, 3], [5], [0], [5], [], []]
    solution: Solution = Solution()
    print(solution.eventualSafeNodes(graph=graph))
