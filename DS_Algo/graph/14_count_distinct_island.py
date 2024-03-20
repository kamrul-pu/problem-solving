"""
Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct islands where a group of connected
1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is
not equal to another (not rotated or reflected).
"""

from typing import List, Set


def dfs(
    row: int,
    col: int,
    g: List[List[int]],
    visited: List[List[bool]],
    lst: List[int],
    row0: int,
    col0: int,
    n: int,
    m: int,
) -> None:
    # Mark the current cell as visited and add its relative position to the island
    visited[row][col] = True
    lst.append((row - row0, col - col0))

    # Define the possible moves: up, right, down, left
    dr: List[int] = [-1, 0, 1, 0]
    dc: List[int] = [0, 1, 0, -1]

    # Explore neighbors
    for i in range(len(dr)):
        nrow: int = row + dr[i]
        ncol: int = col + dc[i]

        # Check if the neighboring cell is within bounds, unvisited, and is part of the island
        if (
            nrow >= 0
            and nrow < n
            and ncol >= 0
            and ncol < m
            and not visited[nrow][ncol]
            and g[nrow][ncol] == 1
        ):
            # Recursively explore the neighboring cell
            dfs(
                row=nrow,
                col=ncol,
                g=g,
                visited=visited,
                lst=lst,
                row0=row0,
                col0=col0,
                n=n,
                m=m,
            )


def count_distinct_island(g: List[List[int]]) -> int:
    n: int = len(g)
    m: int = len(g[0])
    visited: List[List[bool]] = [[False for col in range(m)] for row in range(n)]
    st: Set = set()  # Set to store distinct islands

    # Iterate through each cell in the grid
    for row in range(n):
        for col in range(m):
            # If the cell is part of an unvisited island
            if not visited[row][col] and g[row][col] == 1:
                lst: List[int] = []

                # Explore the entire island and store its relative positions
                dfs(
                    row=row,
                    col=col,
                    g=g,
                    visited=visited,
                    lst=lst,
                    row0=row,
                    col0=col,
                    n=n,
                    m=m,
                )

                # Convert the relative positions to a tuple and add it to the set
                st.add(tuple(lst))

    return len(st)


if __name__ == "__main__":
    g: List[List[int]] = [
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [1, 1, 0, 1, 0],
    ]
    print(count_distinct_island(g=g))
