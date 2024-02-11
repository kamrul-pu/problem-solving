"""Coin Change."""

from typing import List


class Solution:
    def __f(self, i: int, amount: int, coins: List[int], dp: List[List[int]]) -> int:
        """
        Recursive helper function to find the minimum number of coins needed to make up a given amount.

        Args:
            i (int): Current index of coin being considered.
            amount (int): Remaining amount to make up.
            coins (List[int]): List of available coin denominations.
            dp (List[List[int]]): Memoization table to store computed values.

        Returns:
            int: Minimum number of coins needed.
        """
        if i == 0:
            if amount % coins[i] == 0:
                return amount // coins[i]
            return 1e9
        if dp[i][amount] != -1:
            return dp[i][amount]
        not_take: int = 0 + self.__f(i - 1, amount, coins, dp)
        take: int = 1e9
        if coins[i] <= amount:
            take = 1 + self.__f(i, amount - coins[i], coins, dp)
        dp[i][amount] = min(take, not_take)
        return dp[i][amount]

    def __coin_change_tabulation(self, coins: List[int], amount: int, n: int) -> int:
        """
        Tabulation approach to find the minimum number of coins needed to make up a given amount.

        Args:
            coins (List[int]): List of available coin denominations.
            amount (int): Target amount to make up.
            n (int): Number of available coin denominations.

        Returns:
            int: Minimum number of coins needed.
        """
        dp: list[list[int]] = [[0 for col in range(amount + 1)] for row in range(n)]

        for t in range(amount + 1):
            if t % coins[0] == 0:
                dp[0][t] = t // coins[0]
            else:
                dp[0][t] = 1e9

        for i in range(1, n):
            for t in range(amount + 1):
                not_take: int = 0 + dp[i - 1][t]
                take: int = 1e9
                if coins[i] <= t:
                    take = 1 + dp[i][t - coins[i]]
                dp[i][t] = min(take, not_take)

        return dp[n - 1][amount]

    def __coin_change_optimal(self, coins: List[int], amount: int, n: int) -> int:
        """
        Optimal space complexity approach to find the minimum number of coins needed to make up a given amount.

        Args:
            coins (List[int]): List of available coin denominations.
            amount (int): Target amount to make up.
            n (int): Number of available coin denominations.

        Returns:
            int: Minimum number of coins needed.
        """
        prev: List[int] = [
            t // coins[0] if t % coins[0] == 0 else 1e9 for t in range(amount + 1)
        ]
        cur: List[int] = [0 for col in range(amount + 1)]
        for i in range(1, n):
            for t in range(amount + 1):
                not_take: int = 0 + prev[t]
                take: int = 1e9
                if coins[i] <= t:
                    take = 1 + cur[t - coins[i]]
                cur[t] = min(take, not_take)
            prev = cur
        return prev[amount] if prev[amount] != 1e9 else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Function to find the minimum number of coins needed to make up a given amount.

        Args:
            coins (List[int]): List of available coin denominations.
            amount (int): Target amount to make up.

        Returns:
            int: Minimum number of coins needed.
        """
        n: int = len(coins)
        # dp: List[List[int]] = [[-1] * (amount + 1) for _ in range(n)]
        # ans: int = self.__f(n - 1, amount, coins, dp)
        # ans: int = self.__coin_change_tabulation(coins=coins, amount=amount, n=n)
        # return ans if ans != 1e9 else -1
        return self.__coin_change_optimal(coins=coins, amount=amount, n=n)


if __name__ == "__main__":
    coins: List[int] = [1, 2, 5]
    amount: int = 11
    solution: Solution = Solution()
    print(solution.coinChange(coins=coins, amount=amount))
