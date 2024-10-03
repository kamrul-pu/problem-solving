"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time..
"""

from typing import List

# Constant for representing infinity
IM: int = float("inf")


class Solution:
    def __f(self, i: int, j: int, g: List[List[int]], dp: List[List[int]]) -> int:
        # Base case: when we reach the top-left corner, return its value
        if i == 0 and j == 0:
            return g[i][j]

        # If out of bounds, return infinity (not a valid path)
        if i < 0 or j < 0:
            return IM

        # If we have already computed the value for this cell, return it
        if dp[i][j] != -1:
            return dp[i][j]

        # Calculate the minimum path sum by moving from the top (up) or from the left
        up: int = g[i][j] + self.__f(i - 1, j, g, dp)  # Moving from the cell above
        left: int = g[i][j] + self.__f(
            i, j - 1, g, dp
        )  # Moving from the cell on the left

        # Store the minimum path sum in the dp array and return it
        dp[i][j] = min(up, left)
        return dp[i][j]

    def __tabulation(self, g: List[List[int]], n: int, m: int) -> int:
        # Create a dp table initialized to 0
        dp: List[List[int]] = [[0] * m for _ in range(n)]

        # Fill in the dp table
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    # The starting point
                    dp[i][j] = g[i][j]
                else:
                    # Calculate the minimum path sum from top and left
                    up: int = g[i][j] + (dp[i - 1][j] if i > 0 else IM)
                    left: int = g[i][j] + (dp[i][j - 1] if j > 0 else IM)
                    # Store the minimum of the two paths
                    dp[i][j] = min(up, left)

        # Return the minimum path sum to the bottom-right corner
        return dp[n - 1][m - 1]

    def __optimized(self, g: List[List[int]], n: int, m: int) -> int:
        # Use a single array to optimize space
        prev: List[int] = [0] * m

        # Iterate through the grid
        for i in range(n):
            cur: List[int] = [0] * m  # Current row's dp values
            for j in range(m):
                if i == 0 and j == 0:
                    # The starting point
                    cur[j] = g[i][j]
                else:
                    # Calculate the minimum path sum from top and left
                    up: int = g[i][j] + (prev[j] if i > 0 else IM)
                    left: int = g[i][j] + (cur[j - 1] if j > 0 else IM)
                    # Store the minimum of the two paths
                    cur[j] = min(up, left)
            prev = cur  # Update prev to current for the next iteration

        # Return the minimum path sum to the bottom-right corner
        return prev[m - 1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        # Get dimensions of the grid
        n: int = len(grid)
        m: int = len(grid[0])

        # Uncomment one of the following lines to use the desired approach:
        # dp: List[List[int]] = [[-1] * m for _ in range(n)]
        # return self.__f(n - 1, m - 1, grid, dp)  # Recursive memoization approach
        # return self.__tabulation(grid, n, m)  # Tabulation approach
        return self.__optimized(grid, n, m)  # Optimized space approach


if __name__ == "__main__":
    grid: list[list[int]] = [
        [5, 9, 6],
        [11, 5, 2],
    ]
    solution: Solution = Solution()
    print(solution.minPathSum(grid=grid))  # Output the minimum path sum
