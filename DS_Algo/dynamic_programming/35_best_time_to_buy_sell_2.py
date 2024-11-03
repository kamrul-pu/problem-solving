"""
The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock i at price[i],
you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

Note: Buying and selling the stock can be done multiple times, but you can only hold one stock at a time. In order to buy another
stock, firstly you have to sell the current holding stock.
"""

from typing import List


class Solution:
    # Helper function for recursion with memoization
    def __f(self, i, buy, p, n, dp) -> int:
        # Base case: If we have processed all days
        if i == n:
            return 0

        # Return already computed value from memoization table
        if dp[i][buy] != -1:
            return dp[i][buy]

        profit: int = 0

        # If we are allowed to buy (buy == 1)
        if buy:
            # Max profit is either:
            # 1. Buy the stock today (cost: -p[i]) and move to the next day (i + 1) with buy state set to 0 (selling)
            # 2. Do nothing today and check profit for the next day (i + 1) while still in the buy state
            profit = max(
                -p[i] + self.__f(i + 1, 0, p, n, dp),  # Buying today
                0 + self.__f(i + 1, 1, p, n, dp),  # Not buying today
            )
        else:
            # If we are allowed to sell (buy == 0)
            # Max profit is either:
            # 1. Sell the stock today (gain: p[i]) and move to the next day (i + 1) with buy state set to 1 (buying again)
            # 2. Do nothing today and check profit for the next day (i + 1) while still in the sell state
            profit = max(
                p[i] + self.__f(i + 1, 1, p, n, dp),  # Selling today
                0 + self.__f(i + 1, 0, p, n, dp),  # Not selling today
            )

        # Store the computed profit in the memoization table
        dp[i][buy] = profit
        return dp[i][buy]

    # Helper function for tabulation (bottom-up dynamic programming)
    def __tabulation(self, p, n) -> int:
        # Create a DP table with n + 1 days and 2 states (buy and sell)
        dp = [[0] * 2 for _ in range(n + 1)]
        # Iterate from the last day back to the first day
        for i in range(n - 1, -1, -1):
            # If we can buy on day i
            dp[i][1] = max(-p[i] + dp[i + 1][0], 0 + dp[i + 1][1])
            # If we can sell on day i
            dp[i][0] = max(p[i] + dp[i + 1][1], 0 + dp[i + 1][0])

        # The result for starting on the first day with the option to buy
        return dp[0][1]

    # Optimized solution using constant space
    def __optimized(self, p, n) -> int:
        # Only need to keep track of two states
        dp = [
            0
        ] * 2  # dp[0]: max profit if not holding stock, dp[1]: max profit if holding stock
        cur = [0] * 2  # Current state

        # Iterate from the last day back to the first day
        for i in range(n - 1, -1, -1):
            # Calculate current profit if we can buy
            cur[1] = max(-p[i] + dp[0], 0 + dp[1])
            # Calculate current profit if we can sell
            cur[0] = max(p[i] + dp[1], 0 + dp[0])
            # Update dp to current state
            dp = cur[:]

        # The result is the maximum profit when we are not holding stock at the start
        return dp[1]

    # Main function to calculate the maximum profit
    def maximumProfit(self, prices) -> int:
        n = len(prices)
        # Uncomment one of the following lines to choose the method
        # dp = [[-1] * 2 for _ in range(n)]
        # return self.__f(0, 1, prices, n, dp)  # Using recursion with memoization
        # return self.__tabulation(prices, n)   # Using tabulation (bottom-up DP)
        return self.__optimized(prices, n)  # Using optimized space approach


if __name__ == "__main__":
    prices: List[int] = [7, 1, 5, 3, 6, 4]
    solution: Solution = Solution()
    # Output the maximum profit for the given prices
    print(solution.maximumProfit(prices=prices))
