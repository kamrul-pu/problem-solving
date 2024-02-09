"""Partition Array for Maximum Sum."""

from typing import List


class Solution:
    def __f(self, i: int, n: int, k: int, arr: List[int], dp: List[int]) -> int:
        # Recursive function to find the maximum sum after partitioning the array
        if i == n:
            return 0
        if dp[i] != -1:
            return dp[i]
        mx_ans: int = -1e9  # Initialize maximum answer with negative infinity
        ln: int = 0  # Length of current partition
        maxi: int = -1e9  # Maximum element in current partition

        # Iterate over elements in the current partition
        for j in range(i, min(i + k, n)):
            ln += 1  # Increment partition length
            maxi = max(maxi, arr[j])  # Update maximum element in partition
            sm: int = ln * maxi + self.__f(
                j + 1, n, k, arr, dp
            )  # Calculate sum for current partition
            mx_ans = max(mx_ans, sm)  # Update maximum answer

        dp[i] = mx_ans  # Memoize the result
        return mx_ans

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n: int = len(arr)
        # dp: List[int] = [-1 for _ in range(n)]  # Initialize memoization array
        # return self.__f(0, n, k, arr, dp)  # Call recursive function
        return self.__max_sum_tabulation(arr, k, n)  # Call tabulation function

    def __max_sum_tabulation(self, arr: List[int], k: int, n: int) -> int:
        # Function to find the maximum sum using tabulation (bottom-up dynamic programming)
        dp: List[int] = [
            0 for _ in range(n + 1)
        ]  # Initialize dp array to store results

        # Iterate over elements in reverse order
        for i in range(n - 1, -1, -1):
            mx_ans: int = -1e9  # Initialize maximum answer for current position
            ln: int = 0  # Length of current partition
            maxi: int = -1e9  # Maximum element in current partition

            # Iterate over elements in current partition
            for j in range(i, min(i + k, n)):
                ln += 1  # Increment partition length
                maxi = max(maxi, arr[j])  # Update maximum element in partition
                sm: int = ln * maxi + dp[j + 1]  # Calculate sum for current partition
                mx_ans = max(mx_ans, sm)  # Update maximum answer

            dp[i] = mx_ans  # Store the maximum answer for current position in dp array

        return dp[0]  # Return the maximum sum


if __name__ == "__main__":
    arr: List[int] = [1, 15, 7, 9, 2, 5, 10]
    k: int = 3
    solution: Solution = Solution()
    print(solution.maxSumAfterPartitioning(arr, k))
