"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

from typing import List, Set


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])  # Get the dimensions of the board
        path: Set = set()  # Set to track visited cells in the current path

        def dfs(r: int, c: int, i: int) -> bool:
            # Base case: If the entire word has been matched
            if i == len(word):
                return True

            # Check if current cell is out of bounds or doesn't match the required character
            # Also check if the cell has already been visited in the current path
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False

            # Mark the current cell as visited
            path.add((r, c))

            # Recursive DFS to explore adjacent cells
            res = (
                dfs(r + 1, c, i + 1)  # Move down
                or dfs(r - 1, c, i + 1)  # Move up
                or dfs(r, c + 1, i + 1)  # Move right
                or dfs(r, c - 1, i + 1)  # Move left
            )

            # Backtrack: Remove the current cell from the path set
            path.remove((r, c))

            return res

        # Iterate through each cell in the board to initiate DFS search
        for r in range(rows):
            for c in range(cols):
                # If the first character of the word matches the current board cell,
                # initiate DFS from this cell to find the entire word
                if dfs(r, c, 0):
                    return True

        return False


if __name__ == "__main__":
    # Example usage:
    board: List[List[str]] = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    word: str = "ABCCED"
    solution: Solution = Solution()
    print(solution.exist(board=board, word=word))
