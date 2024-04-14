"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
"""

from typing import List


class Solution:
    def __f(self, i: int, amount: int, coins: List[int], dp: List[List[int]]) -> int:
        """
        Recursive function to calculate the number of combinations to make up the amount.

        Args:
            i (int): Current index of coins.
            amount (int): Remaining amount to make up.
            coins (List[int]): Denominations of coins.
            dp (List[List[int]]): Memoization table.

        Returns:
            int: Number of combinations.
        """
        if i == 0:
            # If we have only one type of coin left, we can only make up the amount if it's divisible by this coin's value
            return int(amount % coins[i] == 0)
        if dp[i][amount] != -1:
            return dp[i][amount]
        not_take: int = self.__f(
            i - 1, amount, coins, dp
        )  # Number of combinations without taking the current coin
        take: int = 0
        if coins[i] <= amount:
            take = self.__f(
                i, amount - coins[i], coins, dp
            )  # Number of combinations after taking the current coin
        dp[i][amount] = not_take + take
        return dp[i][amount]

    def __ways_tabulation(self, amount: int, coins: List[int], n: int) -> int:
        """
        Tabulation method to calculate the number of combinations to make up the amount.

        Args:
            amount (int): Total amount.
            coins (List[int]): Denominations of coins.
            n (int): Number of coins.

        Returns:
            int: Number of combinations.
        """
        # dp[i][j] represents the number of combinations to make up amount j using coins up to index i
        dp: List[List[int]] = [
            [1 if amt % coins[0] == 0 else 0 for amt in range(amount + 1)]
            for _ in range(n)
        ]
        for i in range(1, n):
            for amt in range(amount + 1):
                not_take: int = dp[i - 1][
                    amt
                ]  # Number of combinations without taking the current coin
                take: int = 0
                if coins[i] <= amt:
                    take = dp[i][
                        amt - coins[i]
                    ]  # Number of combinations after taking the current coin
                dp[i][amt] = not_take + take

        return dp[n - 1][amount]

    def __ways_optimal(self, amount: int, coins: List[int], n: int) -> int:
        """
        Optimized tabulation method to calculate the number of combinations to make up the amount.

        Args:
            amount (int): Total amount.
            coins (List[int]): Denominations of coins.
            n (int): Number of coins.

        Returns:
            int: Number of combinations.
        """
        # Similar to tabulation method, but using two lists (prev and cur) to reduce space complexity
        dp: List[List[int]] = [
            [1 if amt % coins[0] == 0 else 0 for amt in range(amount + 1)]
            for _ in range(n)
        ]
        prev: List[int] = [1 if amt % coins[0] == 0 else 0 for amt in range(amount + 1)]
        cur: List[int] = [0] * (amount + 1)
        for i in range(1, n):
            for amt in range(amount + 1):
                not_take: int = prev[
                    amt
                ]  # Number of combinations without taking the current coin
                take: int = 0
                if coins[i] <= amt:
                    take = cur[
                        amt - coins[i]
                    ]  # Number of combinations after taking the current coin
                cur[amt] = not_take + take

            prev = cur

        return prev[amount]

    def change(self, amount: int, coins: List[int]) -> int:
        """
        Function to find the number of combinations to make up the amount.

        Args:
            amount (int): Total amount.
            coins (List[int]): Denominations of coins.

        Returns:
            int: Number of combinations.
        """
        n: int = len(coins)
        # Uncomment one of the following lines to use different methods
        # dp: List[List[int]] = [[-1] * (amount + 1) for _ in range(n)]
        # return self.__f(i=n - 1, amount=amount, coins=coins, dp=dp)
        # return self.__ways_tabulation(amount=amount, coins=coins, n=n)
        return self.__ways_optimal(amount=amount, coins=coins, n=n)


if __name__ == "__main__":
    coins: List[int] = [1, 2, 5]
    amount: int = 5
    solution: Solution = Solution()
    print(solution.change(amount=amount, coins=coins))
