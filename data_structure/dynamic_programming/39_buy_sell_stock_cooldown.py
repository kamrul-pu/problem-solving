"""By and sell stocks with cooldown."""
from typing import List


class Solution:
    def __f(
        self, i: int, buy: int, n: int, prices: List[int], dp: List[List[int]]
    ) -> int:
        if i >= n:
            return 0

        if dp[i][buy] != -1:
            return dp[i][buy]

        if buy:
            dp[i][buy] = max(
                -prices[i] + self.__f(i + 1, 0, n, prices, dp),
                0 + self.__f(i + 1, 1, n, prices, dp),
            )
            return dp[i][buy]
        dp[i][buy] = max(
            prices[i] + self.__f(i + 2, 1, n, prices, dp),
            0 + self.__f(i + 1, 0, n, prices, dp),
        )
        return dp[i][buy]

    def __max_profit_tabulation(self, n: int, prices: List[int]) -> int:
        dp: List[List[int]] = [[0 for col in range(2)] for row in range(n + 2)]

        for i in range(n - 1, -1, -1):
            dp[i][1] = max(-prices[i] + dp[i + 1][0], 0 + dp[i + 1][1])
            dp[i][0] = max(prices[i] + dp[i + 2][1], 0 + dp[i + 1][0])

        return dp[0][1]

    def __max_profit_optimal(self, n: int, prices: List[int]) -> int:
        dp: List[List[int]] = [[0 for col in range(2)] for row in range(n + 2)]
        front1: List[int] = [0 for col in range(2)]
        front2: List[int] = [0 for col in range(2)]
        cur: List[int] = [0 for col in range(2)]

        for i in range(n - 1, -1, -1):
            cur[1] = max(-prices[i] + front1[0], 0 + front1[1])
            cur[0] = max(prices[i] + front2[1], 0 + front1[0])
            front2 = front1.copy()
            front1 = cur.copy()

        return cur[1]

    def maxProfit(self, prices: List[int]) -> int:
        n: int = len(prices)
        # dp: List[List[int]] = [[-1 for col in range(2)] for row in range(n)]
        # return self.__f(0, 1, n, prices, dp)
        # return self.__max_profit_tabulation(n=n, prices=prices)
        return self.__max_profit_optimal(n=n, prices=prices)


if __name__ == "__main__":
    prices: List[int] = [4, 9, 0, 4, 10]
    prices: List[int] = [1, 2, 3, 0, 2]
    solution: Solution = Solution()
    print(solution.maxProfit(prices=prices))
