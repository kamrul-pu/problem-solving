"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

from collections import defaultdict
from typing import List, Set, DefaultDict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create dictionaries to keep track of used numbers in rows, columns, and 3x3 squares
        rows: DefaultDict[Set[str]] = defaultdict(set)
        cols: DefaultDict[Set[str]] = defaultdict(set)
        squares: DefaultDict[Set[str]] = defaultdict(set)

        # Iterate through each cell in the board (9x9 grid)
        for r in range(9):
            for c in range(9):
                # Skip empty cells represented by '.'
                if board[r][c] == ".":
                    continue

                num = board[r][c]

                # Check if the current number has already appeared in the same row, column, or 3x3 square
                if num in rows[r] or num in cols[c] or num in squares[(r // 3, c // 3)]:
                    # If the number has already been used in the same row, column, or square, the Sudoku is invalid
                    return False

                # Record the current number as used in the corresponding row, column, and 3x3 square
                rows[r].add(num)
                cols[c].add(num)
                squares[(r // 3, c // 3)].add(num)

        # If no invalid number conflicts were found, the Sudoku board is valid
        return True


if __name__ == "__main__":
    # Example Sudoku board
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    # Create an instance of Solution class
    solution: Solution = Solution()

    # Check if the Sudoku board is valid
    print(solution.isValidSudoku(board=board))
