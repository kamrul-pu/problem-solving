"""
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges,
check whether it contains any cycle or not.
"""

from typing import List


class Solution:
    def __dfs(
        self,
        node: int,
        adj: List[List[int]],
        visited: List[bool],
        path_visited: List[bool],
    ) -> bool:
        """
        Depth-first search (DFS) function to detect cycles in a directed graph.

        Args:
            node (int): The current node being visited.
            adj (List[List[int]]): The adjacency list representation of the graph.
            visited (List[bool]): List to keep track of visited nodes.
            path_visited (List[bool]): List to keep track of visited nodes in the current path.

        Returns:
            bool: True if a cycle is detected, False otherwise.
        """
        visited[node] = True
        path_visited[node] = True

        # Explore neighbors of the current node
        for neighbor in adj[node]:
            if not visited[neighbor]:  # Neighbor not visited yet
                if self.__dfs(neighbor, adj, visited, path_visited):
                    return True  # Cycle detected
            elif path_visited[neighbor]:  # Neighbor already visited in the current path
                return True  # Cycle detected

        path_visited[node] = False
        return False  # No cycle found in the current path

    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        """
        Function to check whether a directed graph contains any cycle.

        Args:
            V (int): Number of vertices in the graph.
            adj (List[List[int]]): The adjacency list representation of the graph.

        Returns:
            bool: True if the graph contains a cycle, False otherwise.
        """
        visited: List[bool] = [False] * V
        path_visited: List[bool] = [False] * V
        for node in range(V):
            if not visited[node]:
                if self.__dfs(
                    node=node, adj=adj, visited=visited, path_visited=path_visited
                ):
                    return True  # Cycle detected

        return False  # No cycle found


if __name__ == "__main__":
    adj: List[List[int]] = [[1], [2], [3], [3]]
    # adj = [[1], [2], []]
    v: int = 4
    solution: Solution = Solution()
    print(solution.isCyclic(V=v, adj=adj))
