"""Best time to buy and sell stock ii, to maximize profit."""

from typing import List


class Solution:
    def __f(self, i: int, buy: int, prices: List[int], n: int, dp) -> int:
        """
        Helper function for recursive approach with memoization.
        i: current index
        buy: flag indicating if stock can be buy (1) or not (0)
        prices: list of stock prices
        n: total number of days
        dp: memoization table
        """
        if i == n:
            return 0
        if dp[i][buy] != -1:
            return dp[i][buy]
        profit: int = 0
        if buy:
            # stock can be  bought, choose to buy or skip buying
            profit = max(
                -prices[i] + self.__f(i + 1, 0, prices, n, dp),
                0 + self.__f(i + 1, 1, prices, n, dp),
            )
        else:
            # stock can be sold, choose to sell or skip selling
            profit = max(
                prices[i] + self.__f(i + 1, 1, prices, n, dp),
                0 + self.__f(i + 1, 0, prices, n, dp),
            )

        dp[i][buy] = profit
        return dp[i][buy]

    def maxProfit(self, prices: List[int]) -> int:
        """
        Main function to calculate maximum profit.
        """
        return self.max_profit_optimal(prices)

    def max_profit_tabulation(self, prices: List[int]) -> int:
        """
        Dynamic Programming solution using tabulation.
        """
        n: int = len(prices)
        dp: List[List[int]] = [[0 for col in range(2)] for row in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for buy in range(2):
                profit: int = 0
                if buy:
                    profit = max(-prices[i] + dp[i + 1][0], 0 + dp[i + 1][1])
                else:
                    profit = max(prices[i] + dp[i + 1][1], 0 + dp[i + 1][0])
                dp[i][buy] = profit

        return dp[0][1]

    def max_profit_optimal(self, prices: List[int]) -> int:
        """
        Optimal Dynamic Programming solution using space optimization.
        """
        n: int = len(prices)
        ahed: List[int] = [0 for col in range(2)]

        for i in range(n - 1, -1, -1):
            cur: List[int] = [0 for col in range(2)]
            for buy in range(2):
                profit: int = 0
                if buy:
                    profit = max(-prices[i] + ahed[0], 0 + ahed[1])
                else:
                    profit = max(prices[i] + ahed[1], 0 + ahed[0])
                cur[buy] = profit

            ahed = cur

        return ahed[1]


if __name__ == "__main__":
    prices: List[int] = [7, 1, 5, 3, 6, 4]
    solution: Solution = Solution()
    print(solution.maxProfit(prices=prices))
