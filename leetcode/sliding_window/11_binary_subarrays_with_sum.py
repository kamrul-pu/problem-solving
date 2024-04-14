"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.
"""

from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def __f(self, nums: List[int], goal: int) -> int:
        """
        Computes the number of subarrays with sum equal to goal using a sliding window approach.

        Args:
            nums (List[int]): The input binary array.
            goal (int): The target sum.

        Returns:
            int: The number of subarrays with sum equal to goal.
        """
        if goal < 0:
            return 0
        n: int = len(nums)
        l = r = s = cnt = 0
        while r < n:
            s += nums[r]  # Increment the current sum with the value at index r
            while (
                s > goal
            ):  # Shrink the window until the sum is less than or equal to the goal
                s -= nums[l]  # Decrement the current sum by the value at index l
                l += 1  # Move the left pointer to the right
            cnt = cnt + (r - l + 1)  # Count the number of valid subarrays
            r += 1  # Move the right pointer to the right
        return cnt

    def __helper(self, nums: List[int], goal: int) -> int:
        """
        Computes the number of subarrays with sum equal to goal using a prefix sum approach.

        Args:
            nums (List[int]): The input binary array.
            goal (int): The target sum.

        Returns:
            int: The number of subarrays with sum equal to goal.
        """
        if goal < 0:
            return 0
        count: DefaultDict = defaultdict(int)
        count[0] = 1
        cur_sum: int = 0
        total: int = 0
        for num in nums:
            cur_sum += num  # Update the current sum with the next element
            total += count[
                cur_sum - goal
            ]  # Add the count of previous prefix sums that form the goal sum
            count[cur_sum] += 1  # Increment the count of the current prefix sum
        return total

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        Computes the number of non-empty subarrays with a sum equal to goal.

        Args:
            nums (List[int]): The input binary array.
            goal (int): The target sum.

        Returns:
            int: The number of non-empty subarrays with a sum equal to goal.
        """
        # Uncomment the desired method call below
        # return self.__f(nums=nums, goal=goal)
        return self.__helper(nums=nums, goal=goal)


if __name__ == "__main__":
    nums: List[int] = [1, 0, 1, 0, 1]
    goal: int = 2
    solution: Solution = Solution()
    print(solution.numSubarraysWithSum(nums=nums, goal=goal))
