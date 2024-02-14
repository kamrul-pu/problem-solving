"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.
"""

from typing import List


class Solution:
    def __f(
        self, i: int, buy: int, n: int, prices: List[int], dp: List[List[int]]
    ) -> int:
        if i == n:
            return 0
        if dp[i][buy] != -1:
            return dp[i][buy]
        profit: int = 0
        if buy:
            profit = max(
                -prices[i] + self.__f(i + 1, 0, n, prices, dp),
                0 + self.__f(i + 1, 1, n, prices, dp),
            )
        else:
            profit = max(
                prices[i] + self.__f(i + 1, 1, n, prices, dp),
                0 + self.__f(i + 1, 0, n, prices, dp),
            )

        dp[i][buy] = profit
        return profit

    def __buy_sell_tabulation(self, prices: List[int], n: int) -> int:
        dp: List[List[int]] = [[0] * 2 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            dp[i][1] = max(-prices[i] + dp[i + 1][0], 0 + dp[i + 1][1])
            dp[i][0] = max(prices[i] + dp[i + 1][1], 0 + dp[i + 1][0])

        return dp[0][1]

    def __buy_sell_optimal(self, prices: List[int], n: int) -> int:
        ahed: List[int] = [0] * 2
        for i in range(n - 1, -1, -1):
            cur: List[int] = [0] * 2
            cur[1] = max(-prices[i] + ahed[0], 0 + ahed[1])
            cur[0] = max(prices[i] + ahed[1], 0 + ahed[0])

            ahed = cur

        return ahed[1]

    def __buy_sell_optimal_m(self, prices: List[int], n: int) -> int:
        ahed: List[int] = [0] * 2
        ahed0: int = 0
        ahed1: int = 0
        for i in range(n - 1, -1, -1):
            cur0: int = 0
            cur1: int = 0
            cur: List[int] = [0] * 2
            cur1 = max(-prices[i] + ahed0, 0 + ahed1)
            cur0 = max(prices[i] + ahed1, 0 + ahed0)
            ahed1 = cur1
            ahed0 = cur0

        return ahed1

    def maxProfit(self, prices: List[int]) -> int:
        n: int = len(prices)
        # dp: List[List[int]] = [[-1] * 2 for _ in range(n)]
        # return self.__f(i=0, buy=1, n=n, prices=prices, dp=dp)
        # return self.__buy_sell_tabulation(prices=prices, n=n)
        # return self.__buy_sell_optimal(prices=prices, n=n)
        return self.__buy_sell_optimal_m(prices=prices, n=n)


if __name__ == "__main__":
    prices: List[int] = [7, 1, 5, 3, 6, 4]
    solution: Solution = Solution()
    print(solution.maxProfit(prices=prices))
