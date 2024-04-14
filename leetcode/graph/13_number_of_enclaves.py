"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    # Define deltas for moving in four directions (up, right, down, left)
    del_row: List[int] = [-1, 0, 1, 0]
    del_col: List[int] = [0, 1, 0, -1]

    # Breadth-First Search (BFS) function
    def __bfs(
        self, grid: List[List[int]], n: int, m: int, visited: List[List[bool]]
    ) -> None:
        q: Deque = deque()

        # Iterate over the top and bottom rows
        for j in range(m):
            if grid[0][j] == 1 and not visited[0][j]:
                q.append((0, j))
                visited[0][j] = True
            if grid[n - 1][j] == 1 and not visited[n - 1][j]:
                q.append((n - 1, j))
                visited[n - 1][j] = True

        # Iterate over the left and right columns
        for i in range(n):
            if grid[i][0] == 1 and not visited[i][0]:
                q.append((i, 0))
                visited[i][0] = True
            if grid[i][m - 1] == 1 and not visited[i][m - 1]:
                q.append((i, m - 1))
                visited[i][m - 1] = True

        # Perform BFS traversal
        while q:
            front: Tuple = q.popleft()
            row, col = front
            for i in range(4):
                nrow: int = row + self.del_row[i]
                ncol: int = col + self.del_col[i]

                # Check if the next cell is within bounds and not visited
                if (
                    n > nrow >= 0
                    and m > ncol >= 0
                    and not visited[nrow][ncol]
                    and grid[nrow][ncol] == 1
                ):
                    q.append((nrow, ncol))
                    visited[nrow][ncol] = True

    # Depth-First Search (DFS) function
    def __dfs(
        self,
        row: int,
        col: int,
        grid: List[List[int]],
        n: int,
        m: int,
        visited: List[List[bool]],
    ) -> None:
        visited[row][col] = 1

        # Traverse in all four directions
        for i in range(4):
            nrow: int = row + self.del_row[i]
            ncol: int = col + self.del_col[i]

            # Check if the next cell is within bounds and not visited
            if (
                n > nrow >= 0
                and m > ncol >= 0
                and not visited[nrow][ncol]
                and grid[nrow][ncol] == 1
            ):
                self.__dfs(nrow, ncol, grid, n, m, visited)

    # Helper function to count unbounded land cells
    def __get_count(
        self, visited: List[List[bool]], n: int, m: int, grid: List[List[int]]
    ) -> int:
        cnt: int = 0
        for i in range(1, n):
            for j in range(1, m):
                if not visited[i][j] and grid[i][j] == 1:
                    cnt += 1
        return cnt

    # Solve using DFS
    def __dfs_solve(
        self, grid: List[List[int]], n: int, m: int, visited: List[List[bool]]
    ) -> None:
        # Traverse over the top and bottom rows
        for j in range(m):
            if grid[0][j] == 1 and not visited[0][j]:
                self.__dfs(0, j, grid, n, m, visited)
            if grid[n - 1][j] == 1 and not visited[n - 1][j]:
                self.__dfs(n - 1, j, grid, n, m, visited)

        # Traverse over the left and right columns
        for i in range(n):
            if grid[i][0] == 1 and not visited[i][0]:
                self.__dfs(i, 0, grid, n, m, visited)
            if grid[i][m - 1] == 1 and not visited[i][m - 1]:
                self.__dfs(i, m - 1, grid, n, m, visited)

    # Main function to count the number of unbounded land cells
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n: int = len(grid)  # number of rows
        m: int = len(grid[0])  # number of columns
        visited: List[List[bool]] = [[False] * m for _ in range(n)]

        # Call the DFS function to solve
        self.__dfs_solve(grid=grid, n=n, m=m, visited=visited)

        # Return the count of unbounded land cells
        return self.__get_count(visited=visited, n=n, m=m, grid=grid)


if __name__ == "__main__":
    # Example grid
    grid: List[List[int]] = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    solution: Solution = Solution()
    print(solution.numEnclaves(grid=grid))
