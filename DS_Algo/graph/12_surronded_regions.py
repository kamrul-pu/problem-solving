"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def __bfs(self, board: List[List[str]]) -> None:
        # Define rows and cols of the board
        rows, cols = len(board), len(board[0])
        # Initialize a 2D visited array to keep track of visited cells
        visited: List[List[bool]] = [[False] * cols for _ in range(rows)]
        # Initialize a deque for BFS traversal
        q: Deque[Tuple[int]] = deque()

        # Check the left and right edges of the board
        for row in range(rows):
            if board[row][0] == "O" and not visited[row][0]:
                q.append((row, 0))
                visited[row][0] = True
            if board[row][cols - 1] == "O" and not visited[row][cols - 1]:
                q.append((row, cols - 1))
                visited[row][cols - 1] = True

        # Check the top and bottom edges of the board
        for col in range(cols):
            if board[0][col] == "O" and not visited[0][col]:
                q.append((0, col))
                visited[0][col] = True
            if board[rows - 1][col] == "O" and not visited[rows - 1][col]:
                q.append((rows - 1, col))
                visited[rows - 1][col] = True

        # Define direction arrays for BFS
        del_row: List[int] = [-1, 0, 1, 0]
        del_col: List[int] = [0, 1, 0, -1]

        # Perform BFS traversal
        while q:
            row, col = q.popleft()
            for i in range(4):
                nrow: int = row + del_row[i]
                ncol: int = col + del_col[i]
                # Check if the neighboring cell is valid and unvisited
                if (
                    rows > nrow >= 0
                    and cols > ncol >= 0
                    and board[nrow][ncol] == "O"
                    and not visited[nrow][ncol]
                ):
                    # Mark the neighboring cell as visited and add it to the queue
                    q.append((nrow, ncol))
                    visited[nrow][ncol] = True

        # After BFS traversal, mark all unvisited 'O's as 'X's
        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and board[row][col] == "O":
                    board[row][col] = "X"

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Call the BFS function
        self.__bfs(board=board)


if __name__ == "__main__":
    # Example board
    board: List[List[str]] = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    # Initialize solution object
    solution: Solution = Solution()
    # Solve the problem
    solution.solve(board=board)
    # Print the modified board
    print(board)
