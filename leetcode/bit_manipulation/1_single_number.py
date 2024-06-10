"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # If the array has only one element, that element is the single number
        if len(nums) == 1:
            return nums[0]

        # Initialize the answer variable to store the single number
        ans = 0

        # Iterate through all elements in the array
        for num in nums:
            # Using XOR operation, if the same number appears twice, it cancels out (becomes 0)
            # Leaving only the single number in the end
            ans ^= num

        # Return the single number
        return ans


if __name__ == "__main__":
    nums: List[int] = [4, 1, 2, 1, 2]
    solution: Solution = Solution()
    print(solution.singleNumber(nums=nums))
