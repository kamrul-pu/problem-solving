"""Best time to buy and sell stock 3. Limiting transactions, max transaction 2."""
from typing import List


class Solution:
    def __f(
        self,
        i: int,
        trans: int,
        prices: List[int],
        n: int,
        dp: List[List[int]],
    ) -> int:
        # Base case: If we reach the end of prices or run out of transactions, profit is 0
        if i == n or trans == 4:
            return 0
        # If the result for the current state is already calculated, return it
        if dp[i][trans] != -1:
            return dp[i][trans]
        if trans % 2 == 0:
            # If in the buying state, choose to buy or skip buying
            dp[i][trans] = max(
                -prices[i] + self.__f(i + 1, trans + 1, prices, n, dp),
                0 + self.__f(i + 1, trans, prices, n, dp),
            )
            return dp[i][trans]
        # If in the selling state, choose to sell or skip selling
        dp[i][trans] = max(
            prices[i] + self.__f(i + 1, trans + 1, prices, n, dp),
            0 + self.__f(i + 1, trans, prices, n, dp),
        )
        return dp[i][trans]

    def __max_profit_tabulation(self, prices: List[int], n) -> int:
        # Tabulation approach to calculate the maximum profit
        dp: List[List[int]] = [[0 for col in range(5)] for row in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for trans in range(3, -1, -1):
                if trans % 2 == 0:
                    # If in the buying state, choose to buy or skip buying
                    dp[i][trans] = max(
                        -prices[i] + dp[i + 1][trans + 1], 0 + dp[i + 1][trans]
                    )
                else:
                    # If in the selling state, choose to sell or skip selling
                    dp[i][trans] = max(
                        prices[i] + dp[i + 1][trans + 1], 0 + dp[i + 1][trans]
                    )
        return dp[0][0]

    def __max_profit_optimal(self, prices: List[int], n: int) -> int:
        # Optimized version using two arrays to represent current and ahead states
        ahed: List[int] = [0 for c1 in range(5)]

        for i in range(n - 1, -1, -1):
            cur: List[int] = [0 for c1 in range(5)]
            for trans in range(3, -1, -1):
                if trans % 2 == 0:
                    # If in the buying state, choose to buy or skip buying
                    cur[trans] = max(-prices[i] + ahed[trans + 1], 0 + ahed[trans])
                else:
                    # If in the selling state, choose to sell or skip selling
                    cur[trans] = max(prices[i] + ahed[trans + 1], 0 + ahed[trans])
            ahed = cur

        return ahed[0]

    def maxProfit(self, prices: List[int]) -> int:
        n: int = len(prices)
        # Uncomment one of the following lines based on the method you want to use
        # dp: List[List[int]] = [[-1 for col in range(4)] for row in range(n)]
        # return self.__f(i=0, trans=0, prices=prices, n=n, dp=dp)
        return self.__max_profit_optimal(prices=prices, n=n)


if __name__ == "__main__":
    prices: List[int] = [3, 3, 5, 0, 0, 3, 1, 4]
    solution: Solution = Solution()
    print(solution.maxProfit(prices=prices))
