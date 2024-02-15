"""Distance of nearest cell."""
from collections import deque


def distance(g: list[list[int]]) -> list[list[int]]:
    # Get the number of rows and columns in the grid
    n: int = len(g)
    m: int = len(g[0])

    # Initialize a deque for BFS and visited matrix to keep track of visited cells
    q = deque()
    visited: list[list[bool]] = [[False for col in range(m)] for row in range(n)]

    # Initialize the answer matrix with placeholders
    ans: list[list[int]] = [[False for col in range(m)] for row in range(n)]

    # Iterate through the grid to find the cells with value 1 and start BFS from those cells
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                q.append(
                    (i, j, 0)
                )  # Add the cell coordinates and distance to the queue
                visited[i][j] = True  # Mark the cell as visited

    # Define the directions for movement: up, right, down, left
    dr: list[int] = [-1, 0, 1, 0]
    dc: list[int] = [0, 1, 0, -1]

    # Perform BFS
    while q:
        front: tuple = q.popleft()
        row: int = front[0]
        col: int = front[1]
        dist: int = front[2]

        # Update the answer matrix with the distance to the current cell
        ans[row][col] = dist

        # Explore neighboring cells
        for i in range(len(dr)):
            nrow: int = row + dr[i]
            ncol: int = col + dc[i]

            # Check if the neighboring cell is within bounds and not visited
            if (
                nrow >= 0
                and nrow < n
                and ncol >= 0
                and ncol < m
                and not visited[nrow][ncol]
            ):
                visited[nrow][ncol] = True  # Mark the neighboring cell as visited
                q.append(
                    (nrow, ncol, dist + 1)
                )  # Add the neighboring cell to the queue with updated distance

    return ans


if __name__ == "__main__":
    # Example usage with a 2D grid
    g: list[list[int]] = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 0, 1],
    ]

    # Get the distance matrix using the defined function
    ans: list[list[int]] = distance(g=g)

    # Print the resulting distance matrix
    for row in ans:
        print(row)
