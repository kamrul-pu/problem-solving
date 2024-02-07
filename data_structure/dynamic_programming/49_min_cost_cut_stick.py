"""Minimum cost to cut the stick."""

from typing import List


class Solution:
    # Private recursive function for finding minimum cost
    def __f(self, i: int, j: int, cuts: List[int], dp: List[List[int]]) -> int:
        # Base case: If the start index is greater than the end index, return 0
        if i > j:
            return 0
        # If the value for the current subproblem (i, j) is already computed, return it
        if dp[i][j] != -1:
            return dp[i][j]
        # Initialize minimum cost to a large value
        mini: int = 1e9
        # Iterate through all possible cutting points within the current segment
        for ind in range(i, j + 1):
            # Calculate the cost of cutting at the current point and recursively solve for left and right segments
            cost: int = (
                cuts[j + 1]
                - cuts[i - 1]
                + self.__f(i, ind - 1, cuts, dp)
                + self.__f(ind + 1, j, cuts, dp)
            )
            # Update minimum cost
            mini = min(mini, cost)
        # Memoize the computed minimum cost for the current subproblem
        dp[i][j] = mini
        # Return the minimum cost for the current subproblem
        return dp[i][j]

    # Public function to calculate minimum cost
    def minCost(self, n: int, cuts: List[int]) -> int:
        # c: int = len(cuts)
        # dp: List[List[int]] = [[-1] * (c + 1) for _ in range(c + 1)]
        # cuts.insert(0, 0)
        # cuts.append(n)
        # cuts.sort()
        # return self.__f(1, c, cuts, dp)
        # Delegate the task to tabulated version of the function
        return self.__min_cost_tabulation(n=n, cuts=cuts)

    # Tabulated version of the function to calculate minimum cost
    def __min_cost_tabulation(self, n: int, cuts: List[int]) -> int:
        # Get the number of cuts
        c: int = len(cuts)
        # Initialize DP table to store minimum costs for subproblems
        dp: List[List[int]] = [[0] * (c + 2) for _ in range(c + 2)]
        # Add boundary cuts and sort the cuts
        cuts.insert(0, 0)
        cuts.append(n)
        cuts.sort()
        # Iterate through the cuts in reverse order to fill the DP table bottom-up
        for i in range(c, 0, -1):
            for j in range(1, c + 1):
                # Skip invalid subproblems
                if i > j:
                    continue
                # Initialize minimum cost to a large value
                mini: int = 1e9
                # Iterate through all possible cutting points within the current segment
                for ind in range(i, j + 1):
                    # Calculate the cost of cutting at the current point and add costs of left and right segments
                    cost: int = (
                        cuts[j + 1] - cuts[i - 1] + dp[i][ind - 1] + dp[ind + 1][j]
                    )
                    # Update minimum cost
                    mini = min(mini, cost)
                # Store the computed minimum cost for the current subproblem in the DP table
                dp[i][j] = mini
        # Return the minimum cost for the entire stick
        return dp[1][c]


if __name__ == "__main__":
    # Example usage
    cuts: List[int] = [5, 6, 1, 4, 2]
    n: int = 9
    solution: Solution = Solution()
    print(solution.minCost(n=n, cuts=cuts))
