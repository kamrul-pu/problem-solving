"""Matrix Chain multiplication. Using Partition DP."""

from typing import List


class Solution:
    def __f(self, i: int, j: int, arr: List[int], dp: List[List[int]]) -> int:
        # Base case: if the start and end indices are the same, return 0 (no multiplication needed)
        if i == j:
            return 0
        # If the result for the current indices is already computed, return it from the dp table
        if dp[i][j] != -1:
            return dp[i][j]
        # Initialize the minimum steps needed for multiplication to a large value
        mini: int = 1e9
        # Iterate through possible partitioning points
        for k in range(i, j):
            # Calculate the total steps needed for multiplication if the matrix chain is partitioned at index k
            steps: int = (
                arr[i - 1] * arr[k] * arr[j]  # Matrix multiplication cost
                + self.__f(i, k, arr, dp)  # Cost of multiplying matrices from i to k
                + self.__f(
                    k + 1, j, arr, dp
                )  # Cost of multiplying matrices from k+1 to j
            )
            # Update the minimum steps needed
            mini = min(mini, steps)
        # Store the minimum steps needed in the dp table for future reference
        dp[i][j] = mini
        return dp[i][j]

    def matrix_multiplication(self, arr: List[int]) -> int:
        n: int = len(arr)
        # Initialize a dp table to store computed results to avoid recomputation
        dp: List[List[int]] = [[-1 for col in range(n)] for row in range(n)]
        # Call the recursive function to find the minimum steps for matrix multiplication
        return self.__f(i=1, j=n - 1, arr=arr, dp=dp)


if __name__ == "__main__":
    arr: List[int] = [10, 20, 30, 40, 50]
    solution: Solution = Solution()
    # Find the minimum steps for matrix multiplication
    min_steps = solution.matrix_multiplication(arr=arr)
    print("Minimum steps for matrix multiplication:", min_steps)
