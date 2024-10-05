"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that
is either directly below or diagonally left/right. Specifically, the next element from position
(row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1)
"""

from typing import List


class Solution:
    def __f(
        self,
        i: int,
        j: int,
        matrix: List[List[int]],
        n: int,
        m: int,
        dp: List[List[int]],
    ) -> int:
        # Check for out-of-bounds columns
        if j < 0 or j >= m:
            return float("inf")  # Return infinity if out of bounds

        # Base case: If we reach the last row, return the value at that position
        if i == n - 1:
            return matrix[i][j]

        # If this subproblem has already been solved, return the cached result
        if dp[i][j] != float("inf"):
            return dp[i][j]

        # Get the current cell's value
        current: int = matrix[i][j]

        # Recursively compute the minimum falling path sum from the three possible positions in the next row
        one: int = self.__f(i + 1, j - 1, matrix, n, m, dp)  # Down-left
        two: int = self.__f(i + 1, j, matrix, n, m, dp)  # Down
        three: int = self.__f(i + 1, j + 1, matrix, n, m, dp)  # Down-right

        # Store the minimum path sum for this cell in the dp array
        dp[i][j] = current + min(one, two, three)
        return dp[i][j]

    def __tabulation(self, matrix: List[List[int]], n: int, m: int) -> int:
        # Create a DP table initialized to 0
        dp: List[List[int]] = [[0] * m for _ in range(n)]

        # Initialize the last row of the dp table with the last row of the matrix
        dp[n - 1] = matrix[n - 1][:]  # Copy the last row values

        # Fill the DP table from the second last row to the top
        for i in range(n - 2, -1, -1):  # Start from the second last row
            for j in range(m):  # Iterate through each column in the current row
                current: int = matrix[i][j]  # Current cell's value

                # Calculate the minimum path sum from the three possible downward positions
                one: int = (
                    dp[i + 1][j - 1] if j > 0 else float("inf")
                )  # Down-left (check bounds)
                two: int = dp[i + 1][j]  # Down (directly below)
                three: int = (
                    dp[i + 1][j + 1] if j < m - 1 else float("inf")
                )  # Down-right (check bounds)

                # Store the minimum path sum to this cell
                dp[i][j] = current + min(one, two, three)

        # Return the minimum value from the first row, which contains the minimum path sums starting from any cell in the top row
        return min(dp[0])

    def __optimized(self, matrix: List[List[int]], n: int, m: int) -> int:
        # Start with the last row of the matrix as the initial DP state
        dp: List[int] = matrix[n - 1][:]  # Copy the last row directly

        # Iterate from the second last row to the top
        for i in range(n - 2, -1, -1):
            cur: List[int] = [0] * m  # Initialize current row's DP values
            for j in range(m):  # Iterate through each column
                current: int = matrix[i][j]  # Current cell's value

                # Calculate the minimum path sum for this position
                one: int = (
                    dp[j - 1] if j > 0 else float("inf")
                )  # Down-left (check bounds)
                two: int = dp[j]  # Down (directly below)
                three: int = (
                    dp[j + 1] if j < m - 1 else float("inf")
                )  # Down-right (check bounds)

                # Store the minimum path sum for the current cell
                cur[j] = current + min(one, two, three)

            # Update dp to the current row for the next iteration
            dp = cur

        # Return the minimum value from the first row, which contains the minimum path sums starting from any cell in the top row
        return min(dp)

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n: int = len(matrix)  # Number of rows
        m: int = len(matrix[0])  # Number of columns

        # Uncomment one of the following lines to use the desired approach:
        # return self.__f(0, j, matrix, n, m, dp)  # Use recursive approach with memoization
        # return self.__tabulation(matrix, n, m)  # Use tabulation approach
        return self.__optimized(matrix, n, m)  # Use optimized space approach


if __name__ == "__main__":
    matrix: List[List[int]] = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    solution: Solution = Solution()
    print(solution.minFallingPathSum(matrix))  # Output the minimum falling path sum
