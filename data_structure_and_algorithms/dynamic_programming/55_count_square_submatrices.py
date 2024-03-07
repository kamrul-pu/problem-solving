"""Count Square submatrices with all ones."""

from typing import List


class Solution:
    # Function to count square submatrices with all ones
    def __f(self, matrix: List[List[int]], n: int, m: int) -> int:
        # Initialize a dynamic programming (DP) table to store the count of squares ending at each cell
        dp: List[List[int]] = [[0] * m for _ in range(n)]
        # Initialize the answer variable to store the total count of square submatrices
        ans: int = 0

        # Fill the first row of the DP table and update the answer accordingly
        for j in range(m):
            dp[0][j] = matrix[0][j]
            ans += dp[0][j]

        # Fill the first column of the DP table and update the answer accordingly
        for i in range(1, n):
            dp[i][0] = matrix[i][0]
            ans += dp[i][0]

        # Iterate through the matrix to fill the DP table
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    # If the current cell value is 1, compute the size of the square ending at this cell
                    # The size is determined by the minimum value of its adjacent cells in the DP table
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
                    # Increment the answer by the size of the square
                    ans += dp[i][j]
                else:
                    # If the current cell value is 0, the square ending at this cell cannot be extended
                    # Hence, set the size of the square to 0
                    dp[i][j] = 0

        return ans

    # Main function to count square submatrices with all ones in the input matrix
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Get the dimensions of the input matrix
        n: int = len(matrix)
        m: int = len(matrix[0])
        # Call the helper function to compute the count of square submatrices
        return self.__f(matrix, n, m)


# Test the countSquares function
if __name__ == "__main__":
    matrix: List[List[int]] = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
    ]
    solution: Solution = Solution()
    print(solution.countSquares(matrix=matrix))
