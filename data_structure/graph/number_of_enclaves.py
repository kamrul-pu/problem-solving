"""Find the enclaves."""
from collections import deque


def find_enclaves(g: list[list[str]], n: int, m: int) -> int:
    # Create a matrix to track visited cells
    visited: list[list[bool]] = [[False for col in range(m)] for row in range(n)]
    # Initialize a deque for BFS traversal
    q: deque = deque()

    # Visit top and bottom boundary
    for j in range(m):
        if g[0][j] == 1 and not visited[0][j]:
            q.append((0, j))
            visited[0][j] = True
        if g[n - 1][j] == 1 and not visited[n - 1][j]:
            q.append((n - 1, j))
            visited[n - 1][j] = True

    # Visit the left and right boundary
    for i in range(n):
        if g[i][0] == 1 and not visited[i][0]:
            q.append((i, 0))
            visited[i][0] = True
        if g[i][m - 1] == 1 and not visited[i][m - 1]:
            q.append((i, m - 1))
            visited[i][m - 1] = True

    # Define directions for movement: up, right, down, left
    dr: list[int] = [-1, 0, 1, 0]
    dc: list[int] = [0, 1, 0, -1]

    # Perform BFS traversal starting from the boundary cells
    while q:
        front: tuple = q.popleft()
        row: int = front[0]
        col: int = front[1]
        for i in range(len(dr)):
            nrow: int = row + dr[i]
            ncol: int = col + dc[i]
            # Check if the neighboring cell is within bounds, unvisited, and is part of the enclave
            if (
                nrow >= 0
                and nrow < n
                and ncol >= 0
                and ncol < m
                and not visited[nrow][ncol]
                and g[nrow][ncol] == 1
            ):
                q.append((nrow, ncol))
                visited[nrow][ncol] = True

    cnt: int = 0
    # Count the number of enclaves
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and g[i][j] == 1:
                cnt += 1

    return cnt


if __name__ == "__main__":
    # Example usage with a 2D grid
    g: list[list[str]] = [
        [0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]
    n: int = len(g)
    m: int = len(g[0])
    cnt: int = find_enclaves(g=g, n=n, m=m)
    print(cnt)
