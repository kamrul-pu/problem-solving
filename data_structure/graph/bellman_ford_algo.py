"""Bellman Ford algorithm."""


def bellman_ford(edges: list[int], n: int) -> list[int]:
    # Initialize an array to store the distances from the source node
    distance: list[int] = [float("inf")] * n
    distance[0] = 0  # The distance from the source node to itself is 0

    # Perform relaxation for (n-1) iterations
    for i in range(n - 1):
        # Iterate over each edge in the graph
        for item in edges:
            u, v, wt = item
            if u != float("inf") and distance[u] + wt < distance[v]:
                # Relaxation step: Update the distance to the destination node if a shorter path is found
                distance[v] = distance[u] + wt

    # nth relaxation to check negetive cycles
    for item in edges:
        u, v, wt = item
        if u != float("inf") and distance[u] + wt < distance[v]:
            # in this case there is a negetive cycle return an array with -1
            return [-1]

    # Return the final distances from the source node to all nodes
    return distance


if __name__ == "__main__":
    edges: list[int] = [
        (3, 2, 6),
        (5, 3, 1),
        (0, 1, 5),
        (1, 5, -3),
        (1, 2, -2),
        (3, 4, -2),
        (2, 4, 3),
    ]
    n: int = 6

    # Find the distances using Bellman Ford algorithm
    distance: list[int] = bellman_ford(edges=edges, n=n)
    print(distance)
