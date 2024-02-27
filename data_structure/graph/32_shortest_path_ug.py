"""Shortest path in undirected graph."""

import heapq
from typing import List


def shortest_path_distance(adj_list: List[List[int]], src: int) -> List[int]:
    # Number of nodes in the graph
    n: int = len(adj_list)

    # Initialize distance and parent arrays
    distance: List[int] = [float("inf")] * (n)
    parent: List[int] = [i for i in range(n)]

    # Distance from source to itself is 0
    distance[src] = 0

    # Priority queue to keep track of nodes and their distances
    pq: List[int] = []
    heapq.heappush(pq, (distance[src], src))

    # Dijkstra's algorithm
    while pq:
        dist, node = heapq.heappop(pq)

        # Explore neighbors of the current node
        for neighbor in adj_list[node]:
            n_node: int = neighbor[0]
            new_dist: int = dist + neighbor[1]

            # If a shorter path is found, update distance and push to the priority queue
            if new_dist < distance[n_node]:
                distance[n_node] = new_dist
                heapq.heappush(pq, (new_dist, n_node))
                parent[n_node] = node

    # Reconstruct the shortest path from source to destination
    dest_node: int = n - 1
    ans: List[int] = []
    ans.append(dest_node)

    # Traverse the parent array to get the path
    while dest_node != src and dest_node > 0:
        dest_node = parent[dest_node]
        ans.append(dest_node)

    # Return the reversed path
    return ans[::-1]


if __name__ == "__main__":
    # Example graph represented as an adjacency List
    adj_list: List[List[int]] = [
        [],
        [(2, 2), (4, 1)],
        [(1, 2), (3, 4), (5, 5)],
        [(2, 4), (4, 3), (5, 1)],
        [(1, 1), (3, 3)],
        [(2, 5), (3, 1)],
    ]

    # Find and print the shortest path from source node 1
    ans: List[int] = shortest_path_distance(adj_list=adj_list, src=1)
    print(ans)
