"""Shortest path in undirected graph."""

from typing import List
import heapq
from collections import defaultdict


class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        """
        Finds the shortest path from node 1 to node n in a graph using Dijkstra's algorithm.

        Parameters:
        n (int): Number of nodes in the graph.
        m (int): Number of edges in the graph.
        edges (List[List[int]]): A list of edges where each edge is represented as [u, v, wt].
                                 u and v are nodes, and wt is the weight of the edge between u and v.

        Returns:
        List[int]: A list representing the shortest path from node 1 to node n. Returns [-1] if no path exists.
        """
        # Initialize adjacency list, distances, and parents
        adj = defaultdict(list)
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        # Distance from node 1 to all other nodes
        distances = [float("inf")] * (n + 1)
        distances[1] = 0

        # Parent array to reconstruct the path
        parent = [-1] * (n + 1)

        # Priority queue to select the node with the smallest distance
        pq = []
        heapq.heappush(pq, (0, 1, -1))  # (distance, current_node, parent_node)

        while pq:
            dist, node, par = heapq.heappop(pq)

            # Skip processing if the distance is not the smallest found so far
            if dist > distances[node]:
                continue

            # Update parent node
            if parent[node] == -1:
                parent[node] = par

            # Process each adjacent node
            for neighbor, weight in adj[node]:
                new_dist = dist + weight
                # If a shorter path to neighbor is found
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor, node))

        # Check if there's a path to the destination node
        if distances[n] == float("inf"):
            return [-1]

        # Reconstruct the shortest path from node n to node 1
        path = []
        current = n
        while current != -1:
            path.append(current)
            current = parent[current]

        # Reverse the path to get the correct order from node 1 to node n
        path.reverse()

        return path


if __name__ == "__main__":
    # Example graph represented as an adjacency List
    n: int = 5
    m: int = 6
    edges: List[List[int]] = [
        [1, 2, 2],
        [2, 5, 5],
        [2, 3, 4],
        [1, 4, 1],
        [4, 3, 3],
        [3, 5, 1],
    ]

    # Find and print the shortest path from source node 1
    solution: Solution = Solution()
    ans: List[int] = solution.shortestPath(n, m, edges)
    print(ans)
