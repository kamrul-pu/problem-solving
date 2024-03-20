"""Best time to buy and sell stock 3. Limiting transactions, max transaction 2."""
from typing import List


class Solution:
    def __f(
        self,
        i: int,
        buy: int,
        cap: int,
        prices: List[int],
        n: int,
        dp: List[List[List[int]]],
    ) -> int:
        # Base case: If we reach the end of prices or run out of transactions, profit is 0
        if i == n or cap == 0:
            return 0
        # If the result for the current state is already calculated, return it
        if dp[i][buy][cap] != -1:
            return dp[i][buy][cap]
        if buy:
            # If in the buying state, choose to buy or skip buying
            dp[i][buy][cap] = max(
                -prices[i] + self.__f(i + 1, 0, cap, prices, n, dp),
                0 + self.__f(i + 1, 1, cap, prices, n, dp),
            )
            return dp[i][buy][cap]
        # If in the selling state, choose to sell or skip selling
        dp[i][buy][cap] = max(
            prices[i] + self.__f(i + 1, 1, cap - 1, prices, n, dp),
            0 + self.__f(i + 1, 0, cap, prices, n, dp),
        )
        return dp[i][buy][cap]

    def __max_profit_tabulation(self, prices: List[int], n) -> int:
        # Tabulation approach to calculate the maximum profit
        dp: List[List[int]] = [
            [[0 for c1 in range(3)] for c2 in range(2)] for c3 in range(n + 1)
        ]

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy:
                        # If in the buying state, choose to buy or skip buying
                        dp[i][buy][cap] = max(
                            -prices[i] + dp[i + 1][0][cap], 0 + dp[i + 1][1][cap]
                        )
                    else:
                        # If in the selling state, choose to sell or skip selling
                        dp[i][buy][cap] = max(
                            prices[i] + dp[i + 1][1][cap - 1], 0 + dp[i + 1][0][cap]
                        )

        return dp[0][1][2]

    def __max_profit_optimal(self, prices: List[int], n: int) -> int:
        # Optimized version using two arrays to represent current and ahead states
        dp: List[List[int]] = [
            [[0 for c1 in range(3)] for c2 in range(2)] for c3 in range(n + 1)
        ]
        ahed: List[List[int]] = [[0 for c1 in range(3)] for c2 in range(2)]
        cur: List[List[int]] = [[0 for c1 in range(3)] for c2 in range(2)]

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy:
                        # If in the buying state, choose to buy or skip buying
                        cur[buy][cap] = max(-prices[i] + ahed[0][cap], 0 + ahed[1][cap])
                    else:
                        # If in the selling state, choose to sell or skip selling
                        cur[buy][cap] = max(
                            prices[i] + ahed[1][cap - 1], 0 + ahed[0][cap]
                        )

            ahed = cur.copy()

        return ahed[1][2]

    def maxProfit(self, prices: List[int]) -> int:
        n: int = len(prices)
        # Uncomment one of the following lines based on the method you want to use
        # return self.__f(i=0, buy=1, cap=2, prices=prices, n=n, dp=dp)
        return self.__max_profit_optimal(prices=prices, n=n)


if __name__ == "__main__":
    prices: List[int] = [3, 3, 5, 0, 0, 3, 1, 4]
    solution: Solution = Solution()
    print(solution.maxProfit(prices=prices))
