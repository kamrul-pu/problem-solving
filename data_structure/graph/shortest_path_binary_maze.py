"""Shortest path in a Binary Maze."""
from collections import deque


def shortest_distance(g: list[list[int]], src: tuple, dest: tuple) -> int:
    # Number of rows in the binary maze
    n: int = len(g)

    # Number of columns in the binary maze
    m: int = len(g[0])

    # Initialize distance matrix with infinity values
    distance: list[list[list]] = [
        [float("inf") for col in range(m)] for row in range(n)
    ]

    # Set distance from source to itself as 0
    distance[src[0]][src[1]] = 0

    # Queue for BFS traversal
    q: deque = deque()
    q.append((0, src[0], src[1]))  # Tuple: (distance, row, column)

    # Direction arrays for moving up, right, down, left
    dr: list[int] = [-1, 0, 1, 0]
    dc: list[int] = [0, 1, 0, -1]

    # BFS traversal
    while q:
        dist, row, col = q.popleft()

        # Explore neighbors in all four directions
        for i in range(len(dr)):
            n_row: int = row + dr[i]
            n_col: int = col + dc[i]

            # Check if the neighbor is within bounds and is a valid path (1)
            if (
                n_row >= 0
                and n_row < n
                and n_col >= 0
                and n_col < m
                and g[n_row][n_col] == 1
            ):
                n_dist: int = dist + 1

                # If a shorter path is found, update distance and enqueue the neighbor
                if n_dist < distance[n_row][n_col]:
                    distance[n_row][n_col] = n_dist

                    # If the destination is reached, return the distance
                    if n_row == dest[0] and n_col == dest[1]:
                        return n_dist

                    q.append((n_dist, n_row, n_col))

    # If destination is not reachable
    return -1


if __name__ == "__main__":
    # Example binary maze represented as a 2D list
    g: list[list[int]] = [
        [1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
    ]

    # Source and destination coordinates
    src: tuple = (0, 1)
    dest: tuple = (2, 2)

    # Find and print the shortest distance from source to destination
    distance: int = shortest_distance(g=g, src=src, dest=dest)
    print(distance)
