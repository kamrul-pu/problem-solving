"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a
queen and an empty space, respectively.
"""

from typing import List


class Solution:
    def __is_safe(self, row: int, col: int, board: List[str], n: int) -> bool:
        # Store the original row and column indices for later use
        dup_row: int = row
        dup_col: int = col

        # Check upper left diagonal
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False  # If there is a queen in this diagonal, it's not safe
            row -= 1
            col -= 1

        # Reset row and col indices
        row = dup_row
        col = dup_col
        # Check left column
        while col >= 0:
            if board[row][col] == "Q":
                return False  # If there is a queen in this column, it's not safe
            col -= 1

        # Reset row and col indices
        row = dup_row
        col = dup_col
        # Check lower left diagonal
        while row < n and col >= 0:
            if board[row][col] == "Q":
                return False  # If there is a queen in this diagonal, it's not safe
            row += 1
            col -= 1

        # If no queens are attacking, it's safe to place a queen at this position
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans: List[List[str]] = []  # List to store solutions
        board: List[str] = [
            ["." for col in range(n)] for _ in range(n)
        ]  # Initialize empty board

        def solve(col: int):
            if col == n:  # If all queens are placed, a solution is found
                ans.append(
                    ["".join(row) for row in board]
                )  # Append solution to the list
                return

            for row in range(n):
                if self.__is_safe(row, col, board, n):
                    board[row][col] = "Q"  # Place queen at this position
                    solve(col + 1)  # Recur for the next column
                    board[row][col] = "."  # Backtrack: Remove queen from this position

        solve(0)  # Start the recursion from the first column
        return ans  # Return all solutions


if __name__ == "__main__":
    n: int = 4
    solution: Solution = Solution()
    print(solution.solveNQueens(n=n))
