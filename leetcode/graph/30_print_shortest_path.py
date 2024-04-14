"""Print shortest path using dijkstra algorithm."""

import heapq
from typing import List, Tuple


class Solution:
    def __dijkstras(self, adj_list: List[List[Tuple[int]]], src: int) -> List[int]:
        """
        Dijkstra's algorithm to find the shortest path from source node to all other nodes.
        """
        # Number of nodes in the graph
        n: int = len(adj_list)

        # Initialize distances to all nodes as infinity
        distances: List[int] = [float("inf")] * n
        parent: List[int] = [
            i for i in range(n)
        ]  # Track parent nodes for constructing path

        # Set distance to source node as 0
        distances[src] = 0

        # Priority queue to store nodes to be visited, initialized with source node
        pq: List[Tuple[int]] = []
        heapq.heappush(pq, (distances[src], src))

        while pq:
            # Pop the node with the minimum distance from the priority queue
            distance, node = heapq.heappop(pq)

            # Explore neighbors of the current node
            for neighbor in adj_list[node]:
                n_node: int = neighbor[0]  # Neighbor node index
                new_distance: int = (
                    distance + neighbor[1]
                )  # Updated distance to neighbor

                # If new distance is smaller, update the distance and push the node to priority queue
                if new_distance < distances[n_node]:
                    distances[n_node] = new_distance
                    heapq.heappush(pq, (new_distance, n_node))
                    parent[n_node] = node  # Update parent node for constructing path

        # If destination node is not reachable from source node, return -1
        if distances[n - 1] == float("inf"):
            return -1

        # Construct shortest path from source node to destination node
        destination: int = n - 1
        path: List[int] = []
        path.append(destination)

        while destination != src and destination >= 0:
            destination = parent[destination]
            path.append(destination)

        # Reverse the path to get the correct order
        return path[::-1]

    def shortest_path(self, adj_list: List[List[Tuple[int]]], src: int) -> List[int]:
        """
        Find the shortest path from source node to destination node using Dijkstra's algorithm.
        """
        # Call Dijkstra's algorithm to find shortest path
        return self.__dijkstras(adj_list=adj_list, src=src)


if __name__ == "__main__":
    # Adjacency list representation of the graph
    adj_list: List[List[Tuple[int]]] = [
        [(1, 4), (2, 4)],  # Node 0
        [(0, 4), (2, 2)],  # Node 1
        [(0, 4), (1, 2), (3, 3), (4, 1), (5, 6)],  # Node 2
        [(2, 3), (5, 2)],  # Node 3
        [(2, 1), (5, 3)],  # Node 4
        [(2, 6), (3, 2), (4, 3)],  # Node 5
    ]

    # Create an instance of the Solution class
    solution: Solution = Solution()

    # Find the shortest path from source node 0 to last node n-1
    path: List[int] = solution.shortest_path(adj_list=adj_list, src=0)

    # Print the shortest path
    print(path)
