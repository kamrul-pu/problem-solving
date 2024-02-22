"""Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
or vertically neighboring. The same letter cell may not be used more than once.
"""

from typing import List


class Solution:
    def __f(
        self, i: int, j: int, n: int, m: int, board: List[List[int]], w: str, word: str
    ) -> bool:
        if i == n and j == m:
            return w == word
        if i >= n or j >= m:
            return False
        # consider current word
        w += board[i][j]
        if self.__f(i + 1, j, n, m, board, w, word) or self.__f(
            i, j + 1, n, m, board, w, word
        ):
            return True
        w = w[:-1]
        if self.__f(i + 1, j, n, m, board, w, word) or self.__f(
            i, j + 1, n, m, board, w, word
        ):
            return True

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        n: int = len(board)
        m: int = len(board[0])
        return self.__f(0, 0, n, m, board, "", word)


if __name__ == "__main__":
    board: List[List[chr]] = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    word: str = "ABCCED"
    solution: Solution = Solution()
    print(solution.exist(board=board, word=word))
