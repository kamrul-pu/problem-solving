"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
"""

from typing import List


class Solution:
    def __f(
        self, i: int, buy: int, n: int, prices: List[int], dp: List[List[int]]
    ) -> int:
        """
        Recursive function to calculate the maximum profit with cooldown.

        Args:
            i (int): Current index.
            buy (int): Whether the stock is bought (1) or not (0).
            n (int): Total number of days.
            prices (List[int]): Stock prices for each day.
            dp (List[List[int]]): Memoization table.

        Returns:
            int: Maximum profit.
        """
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

    def __max_profit_tabulation(self, prices: List[int], n: int) -> int:
        """
        Tabulation method to calculate the maximum profit with cooldown.

        Args:
            prices (List[int]): Stock prices for each day.
            n (int): Total number of days.

        Returns:
            int: Maximum profit.
        """
        dp: List[List[int]] = [[0] * 2 for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            dp[i][1] = max(-prices[i] + dp[i + 1][0], 0 + dp[i + 1][1])
            dp[i][0] = max(prices[i] + dp[i + 2][1], 0 + dp[i + 1][0])

        return dp[0][1]

    def __max_profit_optimal(self, prices: List[int], n: int) -> int:
        """
        Optimized method to calculate the maximum profit with cooldown.

        Args:
            prices (List[int]): Stock prices for each day.
            n (int): Total number of days.

        Returns:
            int: Maximum profit.
        """
        front1_0: int = 0
        front1_1: int = 0
        front2_0: int = 0
        front2_1: int = 0
        cur0: int = 0
        cur1: int = 0
        for i in range(n - 1, -1, -1):
            cur1 = max(-prices[i] + front1_0, 0 + front1_1)
            cur0 = max(prices[i] + front2_1, 0 + front1_0)
            front2_0 = front1_0
            front2_1 = front1_1
            front1_0 = cur0
            front1_1 = cur1

        return front1_1

    def maxProfit(self, prices: List[int]) -> int:
        """
        Function to find the maximum profit with cooldown.

        Args:
            prices (List[int]): Stock prices for each day.

        Returns:
            int: Maximum profit.
        """
        n: int = len(prices)
        # Uncomment one of the following lines to use different methods
        # dp: List[List[int]] = [[-1] * 2 for _ in range(n)]
        # return self.__f(0, 1, n, prices, dp)
        # return self.__max_profit_tabulation(prices=prices, n=n)
        return self.__max_profit_optimal(prices=prices, n=n)


if __name__ == "__main__":
    prices: List[int] = [1, 2, 3, 0, 2]
    solution: Solution = Solution()
    print(solution.maxProfit(prices=prices))
