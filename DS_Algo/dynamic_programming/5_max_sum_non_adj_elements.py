"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.
"""

from typing import List


class Solution:
    # This method uses recursion with memoization to solve the problem.
    def __f(self, i: int, nums: List[int], dp: List[int]) -> int:
        # Base case: If we're at the first house, we can only rob it.
        if i == 0:
            return nums[i]
        # If index is negative, it means we've gone past the start.
        if i < 0:
            return 0
        # If we have already computed the maximum money for this house, return it.
        if dp[i] != -1:
            return dp[i]

        # Option 1: Don't rob the current house, move to the previous one.
        not_pick: int = 0 + self.__f(i - 1, nums, dp)
        # Option 2: Rob the current house and add it to the maximum from two houses back.
        pick: int = nums[i] + self.__f(i - 2, nums, dp)

        # Store the maximum of the two options in dp and return it.
        dp[i] = max(not_pick, pick)
        return dp[i]

    # This method uses dynamic programming with tabulation to solve the problem.
    def __house_rob_tabulation(self, nums: List[int], n: int) -> int:
        # Create a dp array to store the maximum money we can rob up to each house.
        dp: List[int] = [0] * n
        # Initialize the first house's value.
        dp[0] = nums[0]

        # Fill the dp array based on the choices at each house.
        for i in range(1, n):
            # Option 1: Don't rob the current house.
            not_pick: int = 0 + dp[i - 1]
            # Option 2: Rob the current house.
            pick: int = nums[i] + (dp[i - 2] if i > 1 else 0)
            # Store the maximum of the two options in dp.
            dp[i] = max(not_pick, pick)

        # The last element in dp will hold the answer for the entire array.
        return dp[n - 1]

    # This method optimizes space complexity by only keeping track of the last two results.
    def __house_rob_optimal(self, nums: List[int], n: int) -> int:
        # Variables to store the maximum money that can be robbed from the last two houses.
        prev: int = nums[0]  # Maximum money if we rob the first house.
        prev2: int = 0  # Maximum money if we skip the first house.

        # Iterate through the houses starting from the second one.
        for i in range(1, n):
            # Option 1: Rob the current house and add to the maximum from two houses back.
            pick: int = nums[i] + prev2
            # Option 2: Don't rob the current house.
            not_pick: int = 0 + prev
            # Current maximum is the better of the two options.
            cur: int = max(pick, not_pick)
            # Update prev2 to the last maximum before the current house.
            prev2 = prev
            # Update prev to the current maximum.
            prev = cur

        # After processing all houses, prev holds the answer.
        return prev

    # Main method that calls the optimal solution based on the input list of house values.
    def rob(self, nums: List[int]) -> int:
        n: int = len(nums)
        # dp: List[int] = [-1] * n
        # return self.__f(n - 1, nums, dp)  # Uncomment for recursive solution.
        # return self.__house_rob_tabulation(nums, n)  # Uncomment for tabulation solution.
        return self.__house_rob_optimal(nums, n)  # Return optimal space solution.


# Entry point for testing the solution.
if __name__ == "__main__":
    arr: list[int] = [2, 1, 4, 9, 9, 7, 8, 5, 10, 100, 20, 30]
    n: int = len(arr)
    solution: Solution = Solution()
    print(
        solution.rob(arr)
    )  # This will print the maximum amount of money that can be robbed.
