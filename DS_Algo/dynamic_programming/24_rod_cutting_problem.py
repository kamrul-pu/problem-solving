"""
Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:


Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick,
it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut).
Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.
"""

from typing import List


class Solution:
    # Dynamic programming approach to find the minimum cost of making cuts
    def __f(self, i: int, N: int, cuts: List[int], dp: List[List[int]]) -> int:
        # Base case: If we're at the first cut, the cost is simply the length of the stick
        if i == 0:
            return N * cuts[0]

        # Return the cached result if it exists
        if dp[i][N] != -1:
            return dp[i][N]

        # Option 1: Not taking the current cut
        not_take: int = self.__f(i - 1, N, cuts, dp)

        # Option 2: Taking the current cut
        take: int = float("-inf")
        r: int = i + 1  # the number of units this cut would reduce the stick length by
        if r <= N:  # Check if the remaining length allows this cut
            take = cuts[i] + self.__f(
                i, N - r, cuts, dp
            )  # Cost of cut + cost of remaining stick

        # Store the result in dp table and return the max cost from taking or not taking
        dp[i][N] = max(take, not_take)
        return dp[i][N]

    # Tabulation approach to find the minimum cost of making cuts
    def __tabulation(self, N: int, cuts: List[int]) -> int:
        n: int = len(cuts)
        # Initialize the dp table with zeros
        dp: List[List[int]] = [[0] * (N + 1) for _ in range(n)]

        # Fill the first row: cost of making cuts when only the first cut is considered
        for c in range(N + 1):
            dp[0][c] = c * cuts[0]

        # Fill the dp table for each cut
        for i in range(1, n):
            for c in range(N + 1):
                # Option 1: Not taking the current cut
                not_take: int = dp[i - 1][c]

                # Option 2: Taking the current cut
                take: int = float("-inf")
                r: int = (
                    i + 1
                )  # Number of units this cut would reduce the stick length by
                if r <= c:  # Check if the remaining length allows this cut
                    take = (
                        cuts[i] + dp[i][c - r]
                    )  # Cost of cut + cost of remaining stick

                # Store the maximum cost from taking or not taking in the dp table
                dp[i][c] = max(take, not_take)

        # Return the result for the whole stick and all cuts
        return dp[n - 1][N]

    # Optimized space approach to find the minimum cost of making cuts
    def __optimized(self, N: int, cuts: List[int]) -> int:
        n: int = len(cuts)
        # Initialize a 1D dp array for space optimization
        dp: List[int] = [0] * (N + 1)

        # Fill the first row: cost of making cuts when only the first cut is considered
        for c in range(N + 1):
            dp[c] = c * cuts[0]

        # Fill the dp array for each cut
        for i in range(1, n):
            # Store the previous values for not taking the current cut
            for c in range(N + 1):
                # Option 1: Not taking the current cut
                not_take: int = dp[c]

                # Option 2: Taking the current cut
                take: int = float("-inf")
                r: int = (
                    i + 1
                )  # Number of units this cut would reduce the stick length by
                if r <= c:  # Check if the remaining length allows this cut
                    take = cuts[i] + dp[c - r]  # Cost of cut + cost of remaining stick

                # Update the dp array with the maximum cost from taking or not taking
                dp[c] = max(take, not_take)

        # Return the result for the whole stick and all cuts
        return dp[N]

    # Main function to determine the minimum cost of cuts
    def minCost(self, N: int, cuts: List[int]) -> int:
        # n: int = len(cuts)
        # dp: List[List[int]] = [[-1] * (N + 1) for _ in range(n)]
        # return self.__f(n - 1, N, cuts, dp)
        # return self.__tabulation(N, cuts)
        return self.__optimized(N, cuts)  # Use the optimized space version


if __name__ == "__main__":
    # Example usage
    price: List[int] = [2, 5, 7, 8, 10]
    N: int = 10
    solution: Solution = Solution()
    print(solution.minCost(N=N, cuts=price))
