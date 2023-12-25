"""Surrounded Regions Replace 0's with X's."""


def dfs(
    row: int, col: int, n: int, m: int, g: list[list[int]], visited: list[list[bool]]
) -> None:
    """Depth-First Search to mark connected '0' cells as visited."""
    visited[row][col] = True
    # Define directions for movement: up, right, down, left
    dr: list[int] = [-1, 0, 1, 0]
    dc: list[int] = [0, 1, 0, -1]

    for i in range(len(dr)):
        nrow: int = row + dr[i]
        ncol: int = col + dc[i]

        # Check if the neighboring cell is within bounds, unvisited, and contains '0'
        if (
            nrow >= 0
            and nrow < n
            and ncol >= 0
            and ncol < m
            and not visited[nrow][ncol]
            and g[nrow][ncol] == "0"
        ):
            # Recursively call DFS for the neighboring '0' cell
            dfs(row=nrow, col=ncol, n=n, m=m, g=g, visited=visited)


def replace_0s(g: list[list[str]], n: int, m: int) -> None:
    """Replace surrounded '0' cells with 'X'."""
    visited: list[list[bool]] = [[False for col in range(m)] for row in range(n)]

    # Visit top and bottom boundary
    for j in range(m):
        if g[0][j] == "0" and not visited[0][j]:
            dfs(row=0, col=j, n=n, m=m, g=g, visited=visited)
        if g[n - 1][j] == "0" and not visited[n - 1][j]:
            dfs(row=n - 1, col=j, n=n, m=m, g=g, visited=visited)

    # Visit the left and right boundary
    for i in range(n):
        if g[i][0] == "0" and not visited[i][0]:
            dfs(row=i, col=0, n=n, m=m, g=g, visited=visited)
        if g[i][m - 1] == "0" and not visited[i][m - 1]:
            dfs(row=i, col=m - 1, n=n, m=m, g=g, visited=visited)

    # Replace unvisited '0' cells with 'X'
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                g[i][j] = "X"


if __name__ == "__main__":
    # Example usage with a 2D grid
    g: list[list[str]] = [
        ["X", "X", "X", "X", "X"],
        ["X", "0", "0", "X", "0"],
        ["X", "X", "0", "X", "0"],
        ["X", "0", "X", "0", "X"],
        ["0", "0", "X", "X", "X"],
    ]
    n: int = len(g)
    m: int = len(g[0])

    # Print the original grid
    for row in g:
        print(row)
    print("=========================")

    # Replace surrounded '0' cells with 'X'
    replace_0s(g=g, n=n, m=m)

    # Print the modified grid
    for row in g:
        print(row)
