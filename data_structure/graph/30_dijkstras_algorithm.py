"""Dijkstra's algorithm using priority queue."""

import heapq


def shortest_path_dijkstra(adj_list: list[list[int]], src: int) -> list[int]:
    """
    Computes the shortest path distances from a source node to all other nodes using Dijkstra's algorithm.

    Parameters:
    - adj_list (list[list[int]]): The adjacency list representing the weighted graph.
    - src (int): The source node from which to compute the shortest paths.

    Returns:
    - distances (list[int]): A list containing the shortest path distances from the source node to each node.
    """
    n: int = len(adj_list)
    distances: list[int] = [float("inf")] * n

    distances[src] = 0
    # Create an empty priority queue
    pq = []
    heapq.heappush(pq, (distances[src], src))

    while pq:
        distance, node = heapq.heappop(pq)
        for neighbor in adj_list[node]:
            n_node = neighbor[0]
            new_distance: int = distance + neighbor[1]

            if new_distance < distances[n_node]:
                distances[n_node] = new_distance
                heapq.heappush(pq, (new_distance, n_node))

    return distances


if __name__ == "__main__":
    adj_list: list[list[int]] = [
        [(1, 4), (2, 4)],
        [(0, 4), (2, 2)],
        [(0, 4), (1, 2), (3, 3), (4, 1), (5, 6)],
        [(2, 3), (5, 2)],
        [(2, 1), (5, 3)],
        [(2, 6), (3, 2), (4, 3)],
    ]

    distances: list[int] = shortest_path_dijkstra(adj_list=adj_list, src=0)
    print(distances)
