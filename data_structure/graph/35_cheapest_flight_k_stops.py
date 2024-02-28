"""Chepest flight within k Stops."""

from collections import deque
from typing import Deque, List


def find_min_cost(g: List[List[int]], src: int, dest: int, k: int) -> int:
    # Number of nodes in the graph
    n: int = len(g)

    # Initialize a deque for BFS traversal
    q: Deque = deque()
    # Add the source node to the queue with initial stops, node, and distance
    q.append((0, (src, 0)))  # (stops, (node, distance))

    # Initialize distance array with infinity for all nodes
    dist: List[int] = [float("inf")] * n
    # Distance from source to itself is 0
    dist[src] = 0

    # Perform BFS traversal
    while q:
        stops, sr_d = q.popleft()
        node: int = sr_d[0]
        cost: int = sr_d[1]

        # If the number of stops exceeds the allowed limit, skip to the next iteration
        if stops > k:
            continue

        # Explore neighbors of the current node
        for neighbor in g[node]:
            neighbor_node: int = neighbor[0]
            e_wt: int = neighbor[1]
            new_cost: int = cost + e_wt

            # If the new cost is smaller than the previously recorded distance
            # and the number of stops is within the limit, update the distance and add to the queue
            if new_cost < dist[neighbor_node] and stops <= k:
                dist[neighbor_node] = new_cost
                q.append((stops + 1, (neighbor_node, new_cost)))

    # If the destination is not reachable, return -1. Otherwise, return the minimum cost to reach the destination.
    return -1 if dist[dest] == float("inf") else dist[dest]


# Example usage
if __name__ == "__main__":
    g: List[List[int]] = [
        [(1, 5), (3, 2)],
        [(2, 5), (4, 1)],
        [],
        [(1, 2)],
        [(2, 1)],
    ]

    src: int = 0
    dest: int = 2
    k: int = 2
    min_cost: int = find_min_cost(g=g, src=src, dest=dest, k=k)
    print(min_cost)
