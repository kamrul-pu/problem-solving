"""Subset Sum equals to target sum."""

from typing import *


class Solution:
    # Recursive approach with memoization
    def __f(self, i: int, nums: List[int], target: int, dp: List[List[int]]) -> bool:
        # Base case: if the target is 0, we've found a valid subset
        if target == 0:
            return True
        # Base case: if we've reached the first element
        if i == 0:
            return target == nums[i]  # Check if the first number matches the target
        # Check if the result is already computed and stored in dp
        if dp[i][target] != -1:
            return dp[i][target]

        # Option 1: Not taking the current number
        not_take: bool = self.__f(i - 1, nums, target, dp)

        # Option 2: Taking the current number, if it's not greater than the target
        take: bool = False
        if target >= nums[i]:
            take = self.__f(i - 1, nums, target - nums[i], dp)

        # Store the result in dp table for future reference
        dp[i][target] = take or not_take
        return dp[i][target]

    # Tabulation approach
    def __tabulation(self, nums: List[int], n: int, k: int) -> bool:
        # Create a DP table with dimensions n x (k+1)
        dp: List[List[bool]] = [[False] * (k + 1) for _ in range(n)]

        # Base case: A sum of 0 can always be achieved with any number of elements
        for i in range(n):
            dp[i][0] = True

        # If the first element is less than or equal to the target, we can form that sum
        if nums[0] <= k:
            dp[0][nums[0]] = True

        # Fill the DP table
        for i in range(1, n):
            for target in range(1, k + 1):
                # Option 1: Not taking the current number
                not_take: bool = dp[i - 1][target]

                # Option 2: Taking the current number if it does not exceed the target
                take: bool = False
                if target >= nums[i]:
                    take = dp[i - 1][target - nums[i]]

                # Store the result in the DP table
                dp[i][target] = take or not_take

        # The answer will be in the last cell of the DP table
        return dp[n - 1][k]

    # Optimized space approach using a 1D DP array
    def __optimized(self, nums: List[int], n: int, k: int) -> bool:
        # Create a 1D array to keep track of achievable sums
        prev: List[bool] = [False] * (k + 1)
        prev[0] = True  # Base case: sum of 0 is always achievable

        # If the first element is less than or equal to the target, mark that sum as achievable
        if nums[0] <= k:
            prev[nums[0]] = True

        # Iterate through the elements of nums
        for i in range(1, n):
            # Create a new array for the current row's results
            cur: List[bool] = [False] * (k + 1)
            for target in range(1, k + 1):
                # Option 1: Not taking the current number
                not_take: bool = prev[target]

                # Option 2: Taking the current number if it does not exceed the target
                take: bool = False
                if target >= nums[i]:
                    take = prev[target - nums[i]]

                # Store the result in the current row
                cur[target] = take or not_take

            # Move to the next row by updating prev to cur
            prev = cur

        # The answer will be in the last position of the array
        return prev[k]

    # Main function to determine if there's a subset with a sum equal to target
    def target_sum(self, nums: List[int], target: int) -> bool:
        # If the input list is empty, return False
        if not nums:
            return False
        n: int = len(nums)

        # Uncomment one of the following lines to choose the approach:
        # Using the recursive approach with memoization
        # dp: List[List[int]] = [[-1] * (target + 1) for _ in range(n)]
        # return self.__f(n - 1, nums, target, dp)

        # Using the tabulation approach
        # return self.__tabulation(nums, n, target)

        # Using the optimized space approach
        return self.__optimized(nums, n, target)


if __name__ == "__main__":
    nums: List[int] = [1, 2, 3, 4]
    target: int = 11
    solution: Solution = Solution()
    print(solution.target_sum(nums, target))  # Output: False
