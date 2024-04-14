"""
A vertex v is an articulation point (also called cut vertex)
if removing v increases the number of connected components.
"""

from typing import List


class Solution:
    TIMER: int = 1

    def __dfs(
        self,
        node: int,
        parent: int,
        visited: List[bool],
        tin: List[int],
        low: List[int],
        adj_list: List[List[int]],
        mark: List[int],
    ) -> None:
        # Depth First Search (DFS) function
        visited[node] = True  # Mark the current node as visited
        tin[node] = self.TIMER  # Set the discovery time for the current node
        low[node] = self.TIMER  # Set the low time for the current node
        self.TIMER += 1  # Increment the timer
        for neighbor in adj_list[
            node
        ]:  # Iterate over all neighbors of the current node
            if neighbor == parent:  # Skip the parent node
                continue
            if not visited[neighbor]:  # If neighbor is not visited
                # Recursively call DFS on the neighbor
                self.__dfs(
                    node=neighbor,
                    parent=node,
                    visited=visited,
                    tin=tin,
                    low=low,
                    adj_list=adj_list,
                    mark=mark,
                )
                # Update low time of the current node based on the neighbor
                low[node] = min(low[node], low[neighbor])
                # If low time of the neighbor is greater than or equal to discovery time of the current node
                # and parent is not the root, then the current node is an articulation point
                if low[neighbor] >= tin[node] and parent != -1:
                    mark[node] = 1  # Mark the current node as an articulation point
            else:
                # If neighbor is already visited, update the low time of the current node
                low[node] = min(low[node], tin[neighbor])

    def articulation_points(self, n: int, connections: List[List[int]]) -> List[int]:
        # Create adjacency list representation of the graph
        adj_list: List[List[int]] = [[] for _ in range(n)]
        for edge in connections:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        tin: List[int] = [0] * n  # Array to store discovery time of each node
        low: List[int] = [0] * n  # Array to store low time of each node
        visited: List[bool] = [False] * n  # Array to track visited nodes
        mark: List[int] = [0] * n  # Array to mark articulation points
        # Start DFS from the first node (node 0) with no parent
        self.__dfs(
            node=0,
            parent=-1,
            visited=visited,
            low=low,
            tin=tin,
            adj_list=adj_list,
            mark=mark,
        )
        points: List[int] = []  # List to store articulation points
        # Collect all articulation points
        for node in range(n):
            if mark[node] == 1:
                points.append(node)

        return (
            points if len(points) > 0 else [-1]
        )  # Return the list of articulation points


if __name__ == "__main__":
    n: int = 4
    connections: List[List[int]] = [[0, 1], [1, 2], [2, 0], [1, 3]]
    solution: Solution = Solution()
    articulation_points: List[int] = solution.articulation_points(
        n=n, connections=connections
    )
    print(articulation_points)  # Print the articulation points
