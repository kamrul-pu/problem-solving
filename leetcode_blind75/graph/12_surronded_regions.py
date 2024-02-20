"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""

from typing import List


class Solution:
    # Define deltas for moving in four directions (up, right, down, left)
    del_row: List[int] = [-1, 0, 1, 0]
    del_col: List[int] = [0, 1, 0, -1]

    def __dfs(
        self,
        row: int,
        col: int,
        board: List[List[str]],
        visited: List[List[bool]],
        n: int,
        m: int,
    ) -> None:
        # Mark the current cell as visited
        visited[row][col] = True

        # Explore neighbors of the current cell
        for i in range(4):
            nrow: int = row + self.del_row[i]
            ncol: int = col + self.del_col[i]
            # Check if the neighbor is within grid boundaries, unvisited, and has value "O"
            if (
                n > nrow >= 0
                and m > ncol >= 0
                and not visited[nrow][ncol]
                and board[nrow][ncol] == "O"
            ):
                # Recursive call to explore the neighbor
                self.__dfs(nrow, ncol, board, visited, n, m)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n: int = len(board)
        m: int = len(board[0])

        # Initialize a 2D list to keep track of visited cells
        visited: List[List[bool]] = [[False] * m for _ in range(n)]

        # Traverse the boundary cells of the board and perform DFS for unvisited "O" cells
        for j in range(m):
            if board[0][j] == "O" and not visited[0][j]:
                self.__dfs(0, j, board, visited, n, m)
            if board[n - 1][j] == "O" and not visited[n - 1][j]:
                self.__dfs(n - 1, j, board, visited, n, m)

        for i in range(n):
            if board[i][0] == "O" and not visited[i][0]:
                self.__dfs(i, 0, board, visited, n, m)
            if board[i][m - 1] == "O" and not visited[i][m - 1]:
                self.__dfs(i, m - 1, board, visited, n, m)

        # Traverse the inner cells of the board and mark unvisited "O" cells as "X"
        for i in range(1, n):
            for j in range(1, m):
                if not visited[i][j] and board[i][j] == "O":
                    board[i][j] = "X"


# Test the solution
if __name__ == "__main__":
    board: List[List[str]] = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    solution: Solution = Solution()
    solution.solve(board=board)
    print(board)
