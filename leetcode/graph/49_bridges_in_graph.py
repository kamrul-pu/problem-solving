"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming
a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server
can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other
server.

Return all critical connections in the network in any order.
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
        bridges: List[List[int]],
    ) -> None:
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
                    bridges=bridges,
                )
                # Update low time of the current node based on the neighbor
                low[node] = min(low[node], low[neighbor])
                # If low time of the neighbor is greater than discovery time of the current node
                # then the edge (node, neighbor) is a bridge
                if low[neighbor] > tin[node]:
                    bridges.append([neighbor, node])  # Add the bridge to the list
            else:
                # If neighbor is already visited, update the low time of the current node
                low[node] = min(low[node], low[neighbor])

    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        # Create adjacency list representation of the graph
        adj_list: List[List[int]] = [[] for _ in range(n)]
        for edge in connections:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        tin: List[int] = [0] * n  # Array to store discovery time of each node
        low: List[int] = [0] * n  # Array to store low time of each node
        visited: List[bool] = [False] * n  # Array to track visited nodes
        bridges: List[List[int]] = []  # List to store critical connections
        # Start DFS from the first node (node 0) with no parent
        self.__dfs(
            node=0,
            parent=-1,
            visited=visited,
            low=low,
            tin=tin,
            adj_list=adj_list,
            bridges=bridges,
        )
        return bridges  # Return the list of critical connections


if __name__ == "__main__":
    n: int = 4
    connections: List[List[int]] = [[0, 1], [1, 2], [2, 0], [1, 3]]
    solution: Solution = Solution()
    critical: List[List[int]] = solution.criticalConnections(
        n=n, connections=connections
    )
    print(critical)  # Print the critical connections
