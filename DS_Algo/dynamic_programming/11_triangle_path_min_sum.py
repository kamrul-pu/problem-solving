"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row, you may
move to either index i or index i + 1 on the next row.
"""

from typing import List


class Solution:
    def __f(
        self, i: int, j: int, n: int, triangle: List[List[int]], dp: List[List[int]]
    ) -> int:
        # Base case: If we are at the last row of the triangle, return the value at that position
        if i == n - 1:
            return triangle[i][j]

        # If the value has already been computed, return it from the dp array
        if dp[i][j] != -1:
            return dp[i][j]

        # Calculate the minimum path sum for moving down and diagonally
        down: int = triangle[i][j] + self.__f(
            i + 1, j, n, triangle, dp
        )  # Move down to the next row, same column
        diagonal: int = triangle[i][j] + self.__f(
            i + 1, j + 1, n, triangle, dp
        )  # Move down to the next row, next column

        # Store the minimum of the two path sums in the dp array
        dp[i][j] = min(down, diagonal)
        return dp[i][j]

    def __tabulation(self, triangle: List[List[int]], n: int) -> int:
        # Create a dp table initialized to 0
        dp: List[List[int]] = [[0] * n for _ in range(n)]
        dp[n - 1] = triangle[n - 1][:]  # Start with the last row of the triangle

        # Fill in the dp table from the second-to-last row to the top
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                # Calculate the minimum path sum for each cell
                down: int = triangle[i][j] + dp[i + 1][j]  # Move down
                diagonal: int = triangle[i][j] + dp[i + 1][j + 1]  # Move diagonally
                # Store the minimum of the two path sums
                dp[i][j] = min(down, diagonal)

        # The minimum path sum to the top of the triangle is now at dp[0][0]
        return dp[0][0]

    def __optimized(self, triangle: List[List[int]], n: int) -> int:
        # Start with the last row as our initial "previous" row
        prev: List[int] = triangle[n - 1][:]

        # Iterate from the second-to-last row to the top
        for i in range(n - 2, -1, -1):
            cur: List[int] = [0] * (i + 1)  # Current row's dp values
            for j in range(i + 1):
                # Calculate the minimum path sum for this position
                down: int = triangle[i][j] + prev[j]  # Move down
                diagonal: int = triangle[i][j] + prev[j + 1]  # Move diagonally
                cur[j] = min(down, diagonal)  # Store the minimum path sum
            prev = cur  # Update prev to current for the next iteration

        # The minimum path sum to the top of the triangle is now at prev[0]
        return prev[0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n: int = len(triangle)  # Get the number of rows in the triangle
        # Uncomment one of the following lines to use the desired approach:
        # dp: List[List[int]] = [[-1] * n for _ in range(n)]  # Memoization approach
        # return self.__f(0, 0, n, triangle, dp)  # Recursive memoization
        # return self.__tabulation(triangle, n)  # Tabulation approach
        return self.__optimized(triangle, n)  # Optimized space approach


if __name__ == "__main__":
    triangle: List[List[int]] = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3],
    ]  # Example triangle input
    solution: Solution = Solution()
    print(solution.minimumTotal(triangle))  # Output the minimum path sum
