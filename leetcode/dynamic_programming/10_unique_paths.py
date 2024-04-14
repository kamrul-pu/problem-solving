"""Unique paths to reach destination."""

from typing import List


class Solution:
    def __f(self, i: int, j: int, dp: List[List[int]]) -> int:
        """
        Recursive function to count the number of unique paths from the top-left corner to the bottom-right corner of a grid.

        Args:
            i (int): The current row index.
            j (int): The current column index.
            dp (List[List[int]]): Memoization table to store the results of subproblems.

        Returns:
            int: The number of unique paths to reach the current cell.
        """
        if i == 1 and j == 1:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        up: int = self.__f(i - 1, j, dp) if i - 1 >= 1 else 0
        left: int = self.__f(i, j - 1, dp) if j - 1 >= 1 else 0

        dp[i][j] = up + left
        return up + left

    def __paths_tabulation(self, m: int, n: int) -> int:
        """
        Function to count the number of unique paths using a tabulated approach.

        Args:
            m (int): The number of rows in the grid.
            n (int): The number of columns in the grid.

        Returns:
            int: The number of unique paths from the top-left corner to the bottom-right corner of the grid.
        """
        dp: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][1] = 1
        for j in range(1, n + 1):
            dp[1][j] = 1

        for i in range(2, m + 1):
            for j in range(2, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m][n]

    def __paths_optimal(self, m: int, n: int) -> int:
        """
        Function to count the number of unique paths using an optimal approach.

        Args:
            m (int): The number of rows in the grid.
            n (int): The number of columns in the grid.

        Returns:
            int: The number of unique paths from the top-left corner to the bottom-right corner of the grid.
        """
        prev: List[int] = [1] * (n + 1)
        cur: List[int] = [1] * (n + 1)
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                cur[j] = prev[j] + cur[j - 1]
            prev = cur
        return prev[n]

    def uniquePaths(self, m: int, n: int) -> int:
        """
        Function to count the number of unique paths from the top-left corner to the bottom-right corner of a grid.

        Args:
            m (int): The number of rows in the grid.
            n (int): The number of columns in the grid.

        Returns:
            int: The number of unique paths from the top-left corner to the bottom-right corner of the grid.
        """
        # Uncomment one of the following methods to use
        # dp: List[List[int]] = [[-1] * (n + 1) for _ in range(m + 1)]
        # return self.__f(i=m, j=n, dp=dp)  # Using recursion with memoization
        # return self.__paths_tabulation(m=m, n=n)  # Using tabulation
        return self.__paths_optimal(m=m, n=n)  # Using an optimal approach


# Example usage:
if __name__ == "__main__":
    m: int = 3  # Number of rows
    n: int = 7  # Number of columns
    solution: Solution = Solution()
    print(solution.uniquePaths(m=m, n=n))
