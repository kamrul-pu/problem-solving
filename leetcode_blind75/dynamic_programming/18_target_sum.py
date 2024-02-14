"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
"""

from typing import List, Tuple


class Solution:
    def __generate_subset(self, nums: List[int], i: int, target: int, memo={}) -> int:
        """
        Recursive function to generate subsets and count the ways to reach a target sum.

        Args:
            nums (List[int]): The list of integers representing the numbers to choose from.
            i (int): The current index being considered.
            target (int): The target sum to achieve.
            memo (dict): Memoization dictionary to store intermediate results.

        Returns:
            int: The number of ways to reach the target sum.
        """
        if i == 0:
            if target == 0 and nums[0] == 0:
                return 2
            if target == 0 or target == nums[0]:
                return 1
            return 0
        key: Tuple[int] = (i, target)
        if key in memo:
            return memo[key]
        take: int = (
            self.__generate_subset(
                nums=nums, i=i - 1, target=target - nums[i], memo=memo
            )
            if nums[i] <= target
            else 0
        )
        not_take: int = self.__generate_subset(
            nums=nums, i=i - 1, target=target, memo=memo
        )
        memo[key] = take + not_take
        return memo[key]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Function to find the number of ways to reach the target sum.

        Args:
            nums (List[int]): The list of integers representing the numbers to choose from.
            target (int): The target sum to achieve.

        Returns:
            int: The number of ways to reach the target sum.
        """
        n: int = len(nums)
        total: int = sum(nums)
        if total - target < 0 or (total - target) % 2 == 1:
            return 0
        return self.__generate_subset(
            nums=nums, i=n - 1, target=(total - target) // 2, memo={}
        )


if __name__ == "__main__":
    nums: List[int] = [1, 1, 1, 1, 1]
    target: int = 3
    solution: Solution = Solution()
    print(solution.findTargetSumWays(nums=nums, target=target))
