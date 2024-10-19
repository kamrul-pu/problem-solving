"""Count subsets with sum k."""

from typing import List


class Solution:
    # Recursive solution with memoization
    def __f(self, i: int, s: int, nums: List[int], dp: List[List[int]]) -> int:
        # Base case: if the target sum 's' is 0, there is one way to achieve it (by picking no elements)
        if s == 0:
            return 1
        # If we're at the first element (i = 0), check if it equals the target sum 's'
        if i == 0:
            return int(nums[0] == s)
        # If we've already computed this state, return the cached result
        if dp[i][s] != -1:
            return dp[i][s]

        # Option 1: Do not pick the current number (nums[i])
        not_pick = self.__f(i - 1, s, nums, dp)

        # Option 2: Pick the current number, if it does not exceed the target 's'
        pick = 0
        if nums[i] <= s:
            pick = self.__f(i - 1, s - nums[i], nums, dp)

        # Cache the result in the dp table and return it
        dp[i][s] = pick + not_pick
        return dp[i][s]

    # Dynamic programming approach using tabulation
    def __tabulation(self, nums: List[int], target: int) -> int:
        n: int = len(nums)
        # Create a 2D dp table where dp[i][s] represents the number of ways to achieve sum 's' with first 'i+1' elements
        dp: List[List[int]] = [[0] * (target + 1) for _ in range(n)]

        # There's one way to reach a target sum of 0: by selecting no elements
        for i in range(n):
            dp[i][0] = 1

        # Initialize for the first element
        if nums[0] <= target:
            dp[0][nums[0]] = 1

        # Fill the dp table
        for i in range(1, n):
            for s in range(target + 1):
                # Option 1: Do not pick the current number
                not_pick = dp[i - 1][s]

                # Option 2: Pick the current number if it does not exceed the target 's'
                pick = 0
                if nums[i] <= s:
                    pick = dp[i - 1][s - nums[i]]

                # Store the total ways in the dp table
                dp[i][s] = pick + not_pick

        # The result is in the last row and the column corresponding to 'target'
        return dp[n - 1][target]

    # Optimized dynamic programming approach using a single array
    def __optimized(self, nums: List[int], target: int) -> int:
        n: int = len(nums)
        # Create a 1D dp array where dp[s] represents the number of ways to achieve sum 's'
        dp: List[int] = [0] * (target + 1)
        dp[0] = 1  # There's one way to reach a target sum of 0: choose nothing.

        # Iterate over each number in the list
        for i in range(n):
            # Iterate backwards to avoid overwriting the dp values from the current round
            for s in range(target, nums[i] - 1, -1):
                dp[s] += dp[s - nums[i]]  # Update the dp array based on previous values

        # The final answer is the number of ways to achieve the target sum
        return dp[target]

    # Main function to count the number of subsets with a given target sum
    def count_subsets(self, nums: List[int], target: int) -> int:
        n: int = len(nums)
        # Uncomment any of the following lines to switch between approaches
        # dp: List[List[int]] = [[-1] * (target + 1) for _ in range(n)]
        # return self.__f(n - 1, target, nums, dp)  # Recursive with memoization
        # return self.__tabulation(nums, target)     # Tabulation approach
        return self.__optimized(nums, target)  # Optimized approach


# Testing the Solution
if __name__ == "__main__":
    nums: List[int] = [1, 2, 2, 3]  # Example input array
    target: int = 3  # Example target sum
    solution: Solution = Solution()
    print(
        solution.count_subsets(nums, target)
    )  # Output the number of subsets that sum to target
