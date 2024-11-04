"""Best time to buy and sell stock 3. Limiting transactions, to k."""

from typing import List


class Solution:
    # Recursive function with memoization
    def __f(self, K: int, N: int, A: List[int]) -> int:
        # Double K because we need to track both buy and sell actions
        K *= 2
        # Create a memoization table initialized to -1
        dp = [[-1] * (K) for _ in range(N)]

        # Recursive helper function
        def f(i: int, t: int) -> int:
            # Base case: If we are out of days or have reached the maximum transactions
            if i == N or t == K:
                return 0
            # Return already computed value
            if dp[i][t] != -1:
                return dp[i][t]

            profit: int = 0
            # If it's time to buy (t is even)
            if t % 2 == 0:
                # Max profit is either:
                # 1. Buy today (-A[i]) and move to the next day (i + 1) with one more transaction used (t + 1)
                # 2. Do nothing today and check the profit for the next day (i + 1) without using a transaction
                profit = max(-A[i] + f(i + 1, t + 1), 0 + f(i + 1, t))
            else:
                # If it's time to sell (t is odd)
                # Max profit is either:
                # 1. Sell today (A[i]) and move to the next day (i + 1) with one more transaction used (t + 1)
                # 2. Do nothing today and check the profit for the next day (i + 1) without using a transaction
                profit = max(A[i] + f(i + 1, t + 1), 0 + f(i + 1, t))

            # Store the computed profit in the memoization table
            dp[i][t] = profit
            return profit

        return f(0, 0)

    # Tabulation (bottom-up dynamic programming)
    def __tabulation(self, K: int, N: int, A: List[int]) -> int:
        # Double K for the same reason as above
        K *= 2
        # Create a DP table with dimensions (N + 1) x (K + 1)
        dp = [[0] * (K + 1) for _ in range(N + 1)]

        # Fill the DP table in reverse order
        for i in range(N - 1, -1, -1):
            for t in range(K - 1, -1, -1):
                profit: int = 0
                # If it's time to buy
                if t % 2 == 0:
                    profit = max(-A[i] + dp[i + 1][t + 1], 0 + dp[i + 1][t])
                else:
                    # If it's time to sell
                    profit = max(A[i] + dp[i + 1][t + 1], 0 + dp[i + 1][t])

                # Store the computed profit in the DP table
                dp[i][t] = profit

        # The result is found in the starting state (day 0, transaction count 0)
        return dp[0][0]

    # Optimized solution using constant space
    def __optimized(self, K: int, N: int, A: List[int]) -> int:
        K *= 2  # Double K
        # Create a 1D DP array to store current state
        dp = [0] * (K + 1)

        # Fill the DP array in reverse order
        for i in range(N - 1, -1, -1):
            for t in range(K - 1, -1, -1):
                if t % 2 == 0:
                    dp[t] = max(-A[i] + dp[t + 1], 0 + dp[t])
                else:
                    dp[t] = max(A[i] + dp[t + 1], 0 + dp[t])

        # The result is found in the starting state (transaction count 0)
        return dp[0]

    # Main function to calculate the maximum profit
    def maxProfit(self, K: int, N: int, A: List[int]) -> int:
        # Uncomment one of the following lines to choose the method
        # return self.__f(K, N, A)  # Using recursion with memoization
        # return self.__tabulation(K, N, A)  # Using tabulation (bottom-up DP)
        return self.__optimized(K, N, A)  # Using optimized space approach


if __name__ == "__main__":
    prices: List[int] = [3, 2, 6, 5, 0, 3]
    k: int = 2  # Maximum number of transactions allowed
    solution: Solution = Solution()
    # Output the maximum profit for the given prices and transactions
    print(solution.maxProfit(k, len(prices), prices))
