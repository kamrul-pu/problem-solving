"""Combination sum 4."""

from typing import List


class Solution:
    def __f(self, nums: List[int], n: int, target: int, dp: List[int]) -> int:
        """
        Recursive function to find the number of combinations that sum up to the target.

        Args:
            nums (List[int]): The list of available numbers.
            n (int): The length of the nums list.
            target (int): The target sum.
            dp (List[List[int]]): Memoization table to store the results of subproblems.

        Returns:
            int: The number of combinations.
        """
        if target == 0:
            return 1
        if target < 0:
            return 0
        if dp[target] != -1:
            return dp[target]
        ans: int = 0
        for i in range(n):
            ans += self.__f(nums, n, target - nums[i], dp)
        dp[target] = ans
        return ans

    def __combination_sum(self, nums: List[int], n: int, target: int) -> int:
        """
        Recursive function to find the number of combinations that sum up to the target using memoization.

        Args:
            nums (List[int]): The list of available numbers.
            n (int): The length of the nums list.
            target (int): The target sum.

        Returns:
            int: The number of combinations.
        """
        dp = {0: 1}
        for total in range(1, target + 1):
            dp[total] = 0
            for num in nums:
                dp[total] += dp.get(total - num, 0)

        return dp[target]

    def __combination_sum_tabulation(self, nums: List[int], n: int, target: int) -> int:
        """
        Function to find the number of combinations that sum up to the target using tabulation.

        Args:
            nums (List[int]): The list of available numbers.
            n (int): The length of the nums list.
            target (int): The target sum.

        Returns:
            int: The number of combinations.
        """
        dp: List[int] = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for j in range(n):
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]

        return dp[target]

    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Function to find the number of combinations that sum up to the target.

        Args:
            nums (List[int]): The list of available numbers.
            target (int): The target sum.

        Returns:
            int: The number of combinations.
        """
        n: int = len(nums)
        # Uncomment one of the following methods to use
        dp: List[int] = [-1] * (target + 1)
        # return self.__f(nums, n, target,dp)  # Using recursion with memoization
        # return self.__combination_sum(nums, n, target)  # Using recursion with memoization (alternative)
        return self.__combination_sum_tabulation(nums, n, target)  # Using tabulation


if __name__ == "__main__":
    nums: List[int] = [1, 2, 3]
    target: int = 4
    solution: Solution = Solution()
    print(solution.combinationSum4(nums=nums, target=target))
