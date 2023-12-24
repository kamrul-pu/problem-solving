"""Rotten Oranges."""
from collections import deque


def oranges_rotting(matrix: list[list[int]]) -> int:
    # Get the number of rows and columns in the matrix
    n: int = len(matrix)
    m: int = len(matrix[0])

    # Initialize a deque for BFS, a matrix to track visited cells, and count of fresh oranges
    q = deque()
    visited: list[list[bool]] = [[False for col in range(m)] for row in range(n)]
    cnt_fresh: int = 0

    # Find all initially rotten oranges and add them to the queue
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                q.append((i, j, 0))  # Tuple format: (row, column, time)
                visited[i][j] = True
            if matrix[i][j] == 1:
                cnt_fresh += 1  # Count the number of fresh oranges

    tm: int = 0  # Initialize the time to 0
    del_row: list[int] = [
        -1,
        0,
        1,
        0,
    ]  # Delta for row in four directions (up, right, down, left)
    del_col: list[int] = [0, 1, 0, -1]  # Delta for column in four directions
    cnt: int = 0  # Initialize count of rotten oranges

    # Perform BFS to find the minimum time for all oranges to rot
    while q:
        front: tuple = q.popleft()
        r: int = front[0]
        c: int = front[1]
        t: int = front[2]
        tm = max(tm, t)  # Update the maximum time

        # Explore neighbors in four directions
        for i in range(len(del_row)):
            nrow: int = r + del_row[i]
            ncol: int = c + del_col[i]

            # Check if the neighbor is within bounds, not visited, and a fresh orange
            if (
                nrow >= 0
                and nrow < n
                and ncol >= 0
                and ncol < m
                and not visited[nrow][ncol]
                and matrix[nrow][ncol] == 1
            ):
                q.append(
                    (nrow, ncol, t + 1)
                )  # Add the neighbor to the queue with incremented time
                visited[nrow][ncol] = True
                cnt += 1  # Increment the count of rotten oranges

    # Check if all fresh oranges were visited; if not, return -1
    if cnt != cnt_fresh:
        return -1

    # Return the maximum time for all oranges to rot
    return tm


if __name__ == "__main__":
    # Example usage of the oranges_rotting function
    matrix: list[list[int]] = [[0, 1, 2], [0, 1, 1], [2, 1, 1]]
    print("Time taken for all oranges to rot:", oranges_rotting(matrix=matrix))
