"""
Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct islands where a group of connected
1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is
not equal to another (not rotated or reflected).
"""

import sys
from typing import List, Set

sys.setrecursionlimit(10**8)


class Solution:
    # Define the possible moves: up, right, down, left
    dr: List[int] = [-1, 0, 1, 0]  # delta row
    dc: List[int] = [0, 1, 0, -1]  # delta column

    def __dfs(
        self,
        row: int,
        col: int,
        row0: int,
        col0: int,
        grid: List[List[int]],
        n: int,
        m: int,
        visited: List[List[bool]],
        lst: List[int],
    ) -> None:
        visited[row][col] = True
        lst.append((row - row0, col - col0))

        for i in range(4):
            nrow: int = row + self.dr[i]
            ncol: int = col + self.dc[i]
            if (
                n > nrow >= 0
                and m > ncol >= 0
                and not visited[nrow][ncol]
                and grid[nrow][ncol] == 1
            ):
                self.__dfs(nrow, ncol, row0, col0, grid, n, m, visited, lst)

    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        m: int = len(grid[0])
        visited: List[List[bool]] = [[False] * m for _ in range(n)]
        st: Set = set()

        for row in range(n):
            for col in range(m):
                if not visited[row][col] and grid[row][col] == 1:
                    lst: List[int] = []
                    self.__dfs(row, col, row, col, grid, n, m, visited, lst)
                    st.add(tuple(lst))

        return len(st)


if __name__ == "__main__":
    grid: List[List[int]] = [
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
    ]

    solution: Solution = Solution()
    print(solution.countDistinctIslands(grid=grid))
