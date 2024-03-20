"""Dijkstra's algorithm using  queue."""

from collections import deque
from typing import List, Tuple


def shortest_path_dijkstra(adj_list: List[Tuple[int]], src: int) -> List[int]:
    """
    Computes the shortest path distances from a source node to all other nodes using Dijkstra's algorithm.

    Parameters:
    - adj_list (List[List[int]]): The adjacency List representing the weighted graph.
    - src (int): The source node from which to compute the shortest paths.

    Returns:
    - distances (List[int]): A List containing the shortest path distances from the source node to each node.
    """
    n: int = len(adj_list)
    distances: List[int] = [float("inf")] * n

    distances[src] = 0
    # Create an empty priority queue
    q: deque = deque()
    q.append((distances[src], src))

    while q:
        distance, node = q.popleft()
        for neighbor in adj_list[node]:
            n_node = neighbor[0]
            new_distance: int = distance + neighbor[1]

            if new_distance < distances[n_node]:
                distances[n_node] = new_distance
                q.append((distances[n_node], n_node))

    return distances


if __name__ == "__main__":
    adj_list: List[Tuple[int]] = [
        [(1, 4), (2, 4)],
        [(0, 4), (2, 2)],
        [(0, 4), (1, 2), (3, 3), (4, 1), (5, 6)],
        [(2, 3), (5, 2)],
        [(2, 1), (5, 3)],
        [(2, 6), (3, 2), (4, 3)],
    ]

    distances: List[int] = shortest_path_dijkstra(adj_list=adj_list, src=0)
    print(distances)
