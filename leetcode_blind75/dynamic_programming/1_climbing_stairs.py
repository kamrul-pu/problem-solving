"""Climbing Stairs."""

from typing import List


class Solution:
    def __f(self, i: int, dp: List[int]) -> int:
        if i == 0:
            return 1  # Base case: If there are no steps left, there's only one way to climb (no steps)
        if dp[i] != -1:
            return dp[
                i
            ]  # If the number of ways to climb 'i' steps has already been calculated, return it from the dp array

        # Calculate the number of ways to climb 'i' steps recursively
        one: int = self.__f(i - 1, dp)  # If taking one step at a time
        two: int = 0
        if i - 2 >= 0:
            two = self.__f(i - 2, dp)  # If taking two steps at a time (if possible)
        dp[i] = one + two  # Save the result in the dp array to avoid recalculating it
        return one + two  # Return the total number of ways to climb 'i' steps

    def __climb_stairs_tabulation(self, n: int) -> int:
        dp: List[int] = [1] * (
            n + 1
        )  # Initialize the dp array with 1, as there's one way to climb 0 steps
        for i in range(1, n + 1):
            one: int = dp[i - 1]  # Number of ways to climb 'i-1' steps
            two: int = 0
            if i - 2 >= 0:
                two = dp[i - 2]  # Number of ways to climb 'i-2' steps
            dp[i] = (
                one + two
            )  # Total number of ways to climb 'i' steps is the sum of ways to climb 'i-1' and 'i-2' steps

        return dp[n]  # Return the number of ways to climb 'n' steps

    def climbStairs(self, n: int) -> int:
        # return self.__f(i=n, dp=[-1] * (n + 1))  # Use recursion with memoization
        return self.__climb_stairs_tabulation(
            n=n
        )  # Use tabulation for dynamic programming


if __name__ == "__main__":
    n: int = 3  # Number of steps in the staircase
    solution: Solution = Solution()
    print(
        solution.climbStairs(n=n)
    )  # Print the number of ways to climb the staircase with 'n' steps
