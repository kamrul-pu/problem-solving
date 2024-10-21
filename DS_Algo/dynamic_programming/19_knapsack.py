"""0/1 knapsack problem solution."""

from typing import List


class Solution:
    # Recursive solution with memoization
    def __f(
        self, i: int, W: int, wt: List[int], val: List[int], dp: List[List[int]]
    ) -> int:
        # Base case: if there's only one item (i == 0)
        if i == 0:
            return (
                val[0] if wt[0] <= W else 0
            )  # If the item's weight is within the capacity W, return its value

        # If the result for this state has been computed, return it
        if dp[i][W] != -1:
            return dp[i][W]

        # Option 1: Include the current item (if it fits)
        pick: int = float("-inf")  # Initialize as negative infinity
        if wt[i] <= W:
            pick = val[i] + self.__f(
                i - 1, W - wt[i], wt, val, dp
            )  # Add value of the item to the result of remaining capacity

        # Option 2: Exclude the current item
        not_pick: int = 0 + self.__f(
            i - 1, W, wt, val, dp
        )  # Proceed with the next item

        # Store the maximum value we can achieve at this state
        dp[i][W] = max(pick, not_pick)
        return dp[i][W]

    # Dynamic programming approach using tabulation
    def __tabulation(self, W: int, wt: List[int], val: List[int]) -> int:
        n: int = len(wt)
        # Create a 2D dp table where dp[i][w] represents the max value with first 'i+1' items and capacity 'w'
        dp: List[List[int]] = [[0] * (W + 1) for _ in range(n)]

        # Initialize the first row for the first item
        for w in range(wt[0], W + 1):
            dp[0][w] = val[0]  # If the first item's weight fits, take its value

        # Fill the dp table for remaining items
        for i in range(1, n):
            for w in range(W + 1):
                # Option 1: Include the current item
                pick: int = float("-inf")
                if wt[i] <= w:  # Only consider including if it fits
                    pick = (
                        val[i] + dp[i - 1][w - wt[i]]
                    )  # Value if we include this item

                # Option 2: Exclude the current item
                not_pick: int = 0 + dp[i - 1][w]  # Value if we exclude this item

                # Store the max value for the current state
                dp[i][w] = max(pick, not_pick)

        return dp[n - 1][W]  # Return the max value for the full capacity

    # Optimized dynamic programming approach using a single array
    def __optimized(self, W: int, wt: List[int], val: List[int]) -> int:
        n: int = len(wt)
        # Create a 1D dp array where dp[w] represents the max value for capacity 'w'
        prev: List[int] = [0] * (W + 1)
        cur: List[int] = [0] * (W + 1)

        # Initialize the first item in the dp array
        for w in range(wt[0], W + 1):
            prev[w] = val[0]

        # Fill the dp array for the remaining items
        for i in range(1, n):
            for w in range(W + 1):
                # Option 1: Include the current item
                pick: int = float("-inf")
                if wt[i] <= w:  # Only consider including if it fits
                    pick = val[i] + prev[w - wt[i]]  # Add value of current item

                # Option 2: Exclude the current item
                not_pick: int = 0 + prev[w]  # Value if we exclude this item

                # Update the current state in the dp array
                cur[w] = max(pick, not_pick)

            prev = cur  # Move to the next item by updating prev to cur

        return prev[W]  # Return the max value for the full capacity

    # Alternative optimized method
    def __optimized1(self, W: int, wt: List[int], val: List[int]) -> int:
        n: int = len(wt)
        prev: List[int] = [0] * (W + 1)

        # Initialize the first item in the dp array
        for w in range(wt[0], W + 1):
            prev[w] = val[0]

        # Fill the dp array for the remaining items
        for i in range(1, n):
            for w in range(W, -1, -1):  # Iterate backwards to avoid overwriting
                # Option 1: Include the current item
                pick: int = float("-inf")
                if wt[i] <= w:  # Only consider including if it fits
                    pick = val[i] + prev[w - wt[i]]  # Add value of current item

                # Option 2: Exclude the current item
                not_pick: int = 0 + prev[w]  # Value if we exclude this item

                # Update the dp array
                prev[w] = max(pick, not_pick)

        return prev[W]  # Return the max value for the full capacity

    # Main method to solve the knapsack problem
    def knapsack(self, W: int, wt: List[int], val: List[int]) -> int:
        n: int = len(wt)
        # Uncomment any of the following lines to switch between approaches
        # dp: List[List[int]] = [[-1] * (W + 1) for _ in range(n)]
        # return self.__f(n - 1, W, wt, val, dp)  # Recursive with memoization
        # return self.__tabulation(W, wt, val)     # Tabulation approach
        # return self.__optimized(W, wt, val)      # Optimized approach
        return self.__optimized1(W, wt, val)  # Alternative optimized approach


# Testing the Solution
if __name__ == "__main__":
    # Example input data
    wt: List[int] = [3, 2, 5]  # Weights of the items
    val: List[int] = [30, 40, 60]  # Values of the items
    n: int = len(wt)
    W: int = 6  # Maximum capacity of the knapsack
    solution: Solution = Solution()
    print(
        solution.knapsack(W, wt, val)
    )  # Output the maximum value that can be achieved
