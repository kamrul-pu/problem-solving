"""Best time to buy and sell stock with transaction fee."""
from typing import List


class Solution:
    def __f(
        self,
        i: int,
        buy: int,
        n: int,
        fee: int,
        prices: List[List[int]],
        dp: List[List[int]],
    ) -> int:
        # Recursive function to calculate maximum profit
        if i == n:
            return 0
        if dp[i][buy] != -1:
            return dp[i][buy]
        if buy:
            # If not holding a stock, choose to buy or skip a day
            dp[i][buy] = max(
                -prices[i] + self.__f(i + 1, 0, n, fee, prices, dp),
                0 + self.__f(i + 1, 1, n, fee, prices, dp),
            )
            return dp[i][buy]

        # If currently holding a stock, choose to sell or skip a day
        dp[i][buy] = max(
            prices[i] - fee + self.__f(i + 1, 1, n, fee, prices, dp),
            0 + self.__f(i + 1, 0, n, fee, prices, dp),
        )
        return dp[i][buy]

    def __max_profit_tabulation(self, prices: List[List[int]], n: int, fee: int) -> int:
        # Tabulation approach to find maximum profit
        dp: List[List[int]] = [[0 for col in range(2)] for row in range(n + 1)]

        for i in range(n - 1, -1, -1):
            dp[i][1] = max(-prices[i] + dp[i + 1][0], 0 + dp[i + 1][1])
            dp[i][0] = max(prices[i] - fee + dp[i + 1][1], 0 + dp[i + 1][0])

        return dp[0][1]

    def __max_profit_optimal(self, prices: List[List[int]], n: int, fee: int) -> int:
        # Optimized tabulation approach using space optimization technique
        dp: List[List[int]] = [[0 for col in range(2)] for row in range(n + 1)]
        prev: List[int] = [0 for col in range(2)]
        cur: List[int] = [0 for col in range(2)]

        for i in range(n - 1, -1, -1):
            cur[1] = max(-prices[i] + prev[0], 0 + prev[1])
            cur[0] = max(prices[i] - fee + prev[1], 0 + prev[0])
            prev = cur.copy()

        return prev[1]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n: int = len(prices)
        # Uncomment one of the following two lines based on the approach you want to use
        # dp: List[List[int]] = [[-1 for col in range(2)] for row in range(n)]
        # return self.__f(0, 1, n, fee, prices, dp)
        # return self.__max_profit_tabulation(prices, n, fee)
        return self.__max_profit_optimal(prices, n, fee)


if __name__ == "__main__":
    prices: List[int] = [1, 3, 2, 8, 4, 9]
    fee: int = 2
    solution: Solution = Solution()
    print(solution.maxProfit(prices=prices, fee=fee))
