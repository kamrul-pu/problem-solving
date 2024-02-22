"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1.
The graph is represented by a 0-indexed 2D integer array graph where graph[i]
is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges.
A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
"""

from typing import List


class Solution:
    def __dfs(
        self,
        node: int,
        graph: List[List[int]],
        visited: List[bool],
        path_visited: List[bool],
        safe_nodes: List[bool],
    ) -> bool:
        # Mark the current node as visited and in the current DFS path
        visited[node] = True
        path_visited[node] = True

        # Traverse through all neighbors of the current node
        for neighbor in graph[node]:
            if not visited[neighbor]:
                # If the neighbor is unvisited, recursively visit it
                # If the neighbor is eventually not safe, mark the current node as not safe as well
                if self.__dfs(neighbor, graph, visited, path_visited, safe_nodes):
                    safe_nodes[node] = False
                    return True
            elif path_visited[neighbor]:
                # If the neighbor is visited in the current DFS path, it forms a cycle
                # Mark the current node as not safe
                safe_nodes[node] = False
                return True

        # Mark the current node as safe and remove it from the current DFS path
        safe_nodes[node] = True
        path_visited[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Number of nodes in the graph
        n: int = len(graph)

        # Lists to track visited nodes, nodes visited in the current DFS path, and safe nodes
        visited: List[bool] = [False] * n
        path_visited: List[bool] = [False] * n
        safe_nodes: List[bool] = [False] * n

        # Perform DFS from each unvisited node to determine safe nodes
        for node in range(n):
            if not visited[node]:
                self.__dfs(node, graph, visited, path_visited, safe_nodes)

        # Collect the indices of all safe nodes
        result: List[int] = []
        for i in range(n):
            if safe_nodes[i]:
                result.append(i)

        return result


if __name__ == "__main__":
    graph: List[List[int]] = [[1, 2], [2, 3], [5], [0], [5], [], []]
    solution: Solution = Solution()
    print(solution.eventualSafeNodes(graph=graph))
