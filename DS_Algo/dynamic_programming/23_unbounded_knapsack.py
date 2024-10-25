"""Unbounded knapsack. Infinite supply of items."""

from typing import List


class Solution:
    # Helper function for the recursive approach with memoization
    def __f(
        self, i: int, w: int, wt: List[int], val: List[int], dp: List[List[int]]
    ) -> int:
        # Base case: If we are at the first item
        if i == 0:
            # If the weight of the first item is less than or equal to the current capacity
            if wt[i] <= w:
                return (w // wt[i]) * val[i]  # Maximum times we can take the first item
            return 0  # Cannot take this item since it exceeds capacity

        # Return cached value if it has been computed before
        if dp[i][w] != -1:
            return dp[i][w]

        # Recursive case: explore both options (taking or not taking the item)
        not_take: int = 0 + self.__f(i - 1, w, wt, val, dp)  # If we don't take the item
        take: int = float("-inf")  # Initialize taking option as invalid
        if wt[i] <= w:
            take = val[i] + self.__f(
                i, w - wt[i], wt, val, dp
            )  # Take the item and keep the index

        # Store the maximum of taking or not taking the item in the DP table
        dp[i][w] = max(take, not_take)
        return dp[i][w]

    # Function for the tabulation (bottom-up) dynamic programming approach
    def __tabulation(self, W: int, wt: List[int], val: List[int]) -> int:
        n: int = len(wt)  # Number of items
        # Initialize DP table with 0 values
        dp: List[List[int]] = [[0] * (W + 1) for _ in range(n)]

        # Fill the first row for the first item
        for w in range(wt[0], W + 1):
            dp[0][w] = (w // wt[0]) * val[0]  # Maximum times we can take the first item

        # Fill the DP table
        for i in range(1, n):
            for w in range(W + 1):
                not_take: int = 0 + dp[i - 1][w]  # Not taking the current item
                take: int = float("-inf")  # Initialize taking option as invalid
                if wt[i] <= w:
                    take = val[i] + dp[i][w - wt[i]]  # Take the item and keep the index

                # Store the maximum value between taking and not taking the item
                dp[i][w] = max(take, not_take)

        return dp[n - 1][W]  # Return the maximum value for the full capacity

    # Function for the optimized space complexity approach
    def __optimized(self, W: int, wt: List[int], val: List[int]) -> int:
        n: int = len(wt)  # Number of items
        dp: List[int] = [0] * (W + 1)  # Single array to store current results

        # Fill the DP array
        for i in range(n):
            for w in range(wt[i], W + 1):  # Start from wt[i] to W
                dp[w] = max(
                    dp[w], val[i] + dp[w - wt[i]]
                )  # Take the item and keep the index

        return dp[W]  # Return the maximum value for the full capacity

    # Main function to find the maximum value that can be achieved within the given weight limit
    def max_weights(self, wt: List[int], val: List[int], W: int) -> int:
        # Uncomment one of the following lines to choose the desired approach
        # n: int = len(wt)
        # dp: List[List[int]] = [[-1] * (W + 1) for _ in range(n)]
        # return self.__f(n - 1, W, wt, val, dp)
        # return self.__tabulation(W, wt, val)
        return self.__optimized(W, wt, val)  # Call the optimized solution


if __name__ == "__main__":
    wt: List[int] = [2, 4, 6]  # Weights of the items
    val: List[int] = [5, 11, 13]  # Values of the items
    W: int = 10  # Maximum weight capacity
    solution: Solution = Solution()
    print(
        solution.max_weights(wt, val, W)
    )  # Output the maximum value that can be carried
