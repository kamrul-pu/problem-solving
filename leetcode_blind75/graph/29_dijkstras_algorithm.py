"""
Dijkstra's algorithm using priority queue.
1. Mark the source node with a current distance of 0 and the rest with infinity.
2. Set the non-visited node with the smallest current distance as the current node.
3. For each neighbor, N of the current node adds the current distance of the adjacent
node with the weight of the edge connecting 0->1. If it is smaller than the current
distance of Node, set it as the new current distance of N.
4. Mark the current node 1 as visited.
5. Go to step 2 if there are any nodes are unvisited.
"""

import heapq

from typing import List, Tuple


class Solution:
    def __dijkstras(self, adj_list: List[Tuple[int]], src: int) -> List[int]:
        # Number of nodes in the graph
        n: int = len(adj_list)

        # Initialize distances to all nodes as infinity
        distances: List[int] = [float("inf")] * n

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

        return distances

    def shortest_path(self, adj_list: List[Tuple[int]], src: int) -> List[int]:
        # Call Dijkstra's algorithm to find shortest paths
        return self.__dijkstras(adj_list=adj_list, src=src)


if __name__ == "__main__":
    # Adjacency list representation of the graph
    adj_list: List[Tuple[int]] = [
        [(1, 4), (2, 4)],  # Node 0
        [(0, 4), (2, 2)],  # Node 1
        [(0, 4), (1, 2), (3, 3), (4, 1), (5, 6)],  # Node 2
        [(2, 3), (5, 2)],  # Node 3
        [(2, 1), (5, 3)],  # Node 4
        [(2, 6), (3, 2), (4, 3)],  # Node 5
    ]

    # Create an instance of the Solution class
    solution: Solution = Solution()

    # Find the shortest distances from source node 0 to all other nodes
    distances: List[int] = solution.shortest_path(adj_list=adj_list, src=0)

    # Print the shortest distances
    print(distances)
