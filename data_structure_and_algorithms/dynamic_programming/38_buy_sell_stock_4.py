"""Best time to buy and sell stock 3. Limiting transactions, to k."""
from typing import List


class Solution:
    def __f(
        self,
        i: int,
        trans: int,
        prices: List[int],
        n: int,
        k: int,
        dp: List[List[int]],
    ) -> int:
        if i == n or trans == k * 2:
            return 0
        if dp[i][trans] != -1:
            return dp[i][trans]
        if trans % 2 == 0:
            dp[i][trans] = max(
                -prices[i] + self.__f(i + 1, trans + 1, prices, n, k, dp),
                0 + self.__f(i + 1, trans, prices, n, k, dp),
            )
            return dp[i][trans]
        dp[i][trans] = max(
            prices[i] + self.__f(i + 1, trans + 1, prices, n, k, dp),
            0 + self.__f(i + 1, trans, prices, n, k, dp),
        )
        return dp[i][trans]

    def __max_profit_tabulation(self, prices: List[int], n: int, k: int) -> int:
        # Tabulation approach to calculate the maximum profit
        dp: List[List[int]] = [[0 for col in range(k * 2 + 1)] for row in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for trans in range(k * 2 - 1, -1, -1):
                if trans % 2 == 0:
                    dp[i][trans] = max(
                        -prices[i] + dp[i + 1][trans + 1], 0 + dp[i + 1][trans]
                    )
                else:
                    dp[i][trans] = max(
                        prices[i] + dp[i + 1][trans + 1], 0 + dp[i + 1][trans]
                    )

        return dp[0][0]

    def __max_profit_optimal(self, prices: List[int], n: int, k: int) -> int:
        # Optimized version using two arrays to represent current and ahead states
        ahed: List[int] = [0 for col in range(k * 2 + 1)]

        for i in range(n - 1, -1, -1):
            cur: List[int] = [0 for col in range(k * 2 + 1)]
            for trans in range(k * 2 - 1, -1, -1):
                if trans % 2 == 0:
                    cur[trans] = max(-prices[i] + ahed[trans + 1], 0 + ahed[trans])
                else:
                    cur[trans] = max(prices[i] + ahed[trans + 1], 0 + ahed[trans])
            ahed = cur

        return ahed[0]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n: int = len(prices)
        # Uncomment one of the following lines based on the method you want to use
        # dp: List[List[int]] = [[-1 for col in range(k * 2)] for row in range(n)]
        # return self.__f(i=0, trans=0, prices=prices, n=n, k=k, dp=dp)
        # return self.__max_profit_tabulation(prices=prices, n=n, k=k)
        return self.__max_profit_optimal(prices=prices, n=n, k=k)


if __name__ == "__main__":
    prices: List[int] = [3, 2, 6, 5, 0, 3]
    # prices: List[int] = [2, 4, 1]
    k: int = 2
    solution: Solution = Solution()
    print(solution.maxProfit(prices=prices, k=k))
