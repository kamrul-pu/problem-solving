"""Minimum cost to climb stairs."""

from typing import List


class Solution:
    def __f(self, i: int, n: int, cost: List[int], dp: List[int]) -> int:
        """
        Recursive function to calculate the minimum cost to reach the top from index i.

        Args:
            i (int): Current index.
            n (int): Total number of steps.
            cost (List[int]): Cost of each step.
            dp (List[int]): Memoization table.

        Returns:
            int: Minimum cost to reach the top from index i.
        """
        if i >= n:
            return 0
        if dp[i] != -1:
            return dp[i]
        # We have two options from each step: either take one step or two steps.
        # We choose the option with the minimum cost and add the cost of the current step.
        op1: int = self.__f(i + 1, n, cost, dp)  # Taking one step
        op2: int = self.__f(i + 2, n, cost, dp)  # Taking two steps
        dp[i] = min(op1, op2) + cost[i]
        return dp[i]

    def __min_cost_tabulation(self, cost: List[int], n: int) -> int:
        """
        Tabulation method to calculate the minimum cost to reach the top.

        Args:
            cost (List[int]): Cost of each step.
            n (int): Total number of steps.

        Returns:
            int: Minimum cost to reach the top.
        """
        # We iterate through the steps from the top to the bottom,
        # calculating the minimum cost to reach the top from each step.
        # At each step, we have two options: either take one step or two steps.
        # We choose the option with the minimum cost and add the cost of the current step.
        dp: List[int] = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            dp[i] = min(dp[i + 1], dp[i + 2]) + cost[i]

        return min(dp[0], dp[1])

    def __min_cost_optimal(self, cost: List[int], n: int) -> int:
        """
        Optimized method to calculate the minimum cost to reach the top.

        Args:
            cost (List[int]): Cost of each step.
            n (int): Total number of steps.

        Returns:
            int: Minimum cost to reach the top.
        """
        # We start from the top and work our way down to the bottom,
        # keeping track of the minimum cost to reach each step.
        # At each step, we have two options: either take one step or two steps.
        # We update the minimum cost accordingly.
        ahed2: int = 0
        ahed1: int = 0
        for i in range(n - 1, -1, -1):
            cur: int = min(ahed1, ahed2) + cost[i]
            ahed2 = ahed1
            ahed1 = cur

        return min(ahed2, ahed1)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Function to find the minimum cost to climb the stairs.

        Args:
            cost (List[int]): Cost of each step.

        Returns:
            int: Minimum cost to climb the stairs.
        """
        n: int = len(cost)
        # Uncomment one of the following lines to use different methods
        # dp: List[int] = [-1] * n
        # return min(self.__f(0, n, cost, dp), self.__f(1, n, cost, dp))
        return self.__min_cost_optimal(cost=cost, n=n)


if __name__ == "__main__":
    cost: List[int] = [10, 15, 20]
    solution: Solution = Solution()
    print(solution.minCostClimbingStairs(cost=cost))
