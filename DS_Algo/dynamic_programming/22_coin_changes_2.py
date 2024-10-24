"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
"""

from typing import List


class Solution:
    # Recursive function with memoization
    def __f(self, i: int, t: int, coins: List[int], dp: List[List[int]]) -> int:
        # Base case: If we're at the first coin, check if we can form the amount t
        if i == 0:
            return int(
                t % coins[i] == 0
            )  # If t is divisible by coins[0], return 1 (can form t), else return 0

        # If the value has already been computed, return it
        if dp[i][t] != -1:
            return dp[i][t]

        # Option 1: Don't take the current coin
        not_take: int = self.__f(i - 1, t, coins, dp)

        # Option 2: Take the current coin (if it fits)
        take: int = 0
        if coins[i] <= t:
            take = self.__f(
                i, t - coins[i], coins, dp
            )  # Stay on the same coin for the next iteration

        # Store the result in dp table
        dp[i][t] = take + not_take
        return dp[i][t]

    # Dynamic programming approach using tabulation
    def __tabulation(self, amount: int, coins: List[int]) -> int:
        n: int = len(coins)
        # Create a 2D dp table initialized to 0
        dp: List[List[int]] = [[0] * (amount + 1) for _ in range(n)]

        # Base case: Fill for the first coin
        for t in range(amount + 1):
            dp[0][t] = int(
                t % coins[0] == 0
            )  # Can we form amount t with the first coin?

        # Fill the dp table for the rest of the coins
        for i in range(1, n):
            for t in range(amount + 1):
                # Option 1: Don't take the current coin
                not_take: int = dp[i - 1][t]

                # Option 2: Take the current coin (if it fits)
                take: int = 0
                if coins[i] <= t:
                    take = dp[i][t - coins[i]]

                # Store the total ways to form amount t
                dp[i][t] = take + not_take

        return dp[n - 1][amount]  # Return the ways to form 'amount' with all coins

    # Optimized dynamic programming approach using a single array
    def __optimized(self, amount: int, coins: List[int]) -> int:
        n: int = len(coins)
        # Initialize a dp array for storing the number of ways to form each amount
        dp: List[int] = [0] * (amount + 1)

        # Base case for the first coin
        for t in range(amount + 1):
            dp[t] = int(t % coins[0] == 0)  # Can we form amount t with the first coin?

        # Fill the dp array for the rest of the coins
        for i in range(1, n):
            for t in range(amount + 1):
                not_take: int = dp[t]  # Ways without taking the current coin
                take: int = 0
                if coins[i] <= t:
                    take = dp[t - coins[i]]  # Ways if we take the current coin

                # Update the dp array for amount t
                dp[t] = take + not_take

        return dp[amount]  # Return the ways to form 'amount' using all coins

    # Main method to find the number of ways to make change for a given amount
    def change(self, amount: int, coins: List[int]) -> int:
        # Uncomment any of the following lines to switch between approaches
        # n: int = len(coins)
        # dp: List[List[int]] = [[-1] * (amount + 1) for _ in range(n)]
        # return self.__f(n - 1, amount, coins, dp)  # Recursive with memoization
        # return self.__tabulation(amount, coins)     # Tabulation approach
        return self.__optimized(amount, coins)  # Optimized approach


# Example usage
if __name__ == "__main__":
    coins: List[int] = [1, 2, 5]  # List of coin denominations
    amount: int = 5  # Target amount
    solution: Solution = Solution()
    print(
        solution.change(amount, coins)
    )  # Output: Number of ways to make change for 'amount'
