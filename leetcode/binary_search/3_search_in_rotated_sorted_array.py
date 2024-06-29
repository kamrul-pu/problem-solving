"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
(0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
"""

from typing import List


class Solution:
    def __f(self, nums: List[int], target: int) -> int:
        """
        Binary search function to find the index of the target in a rotated sorted array.

        Args:
        - nums: List of integers representing the rotated sorted array.
        - target: Integer value to search for in the array.

        Returns:
        - Index of the target if found, otherwise -1.
        """
        n: int = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid: int = (lo + hi) // 2
            if nums[mid] == target:
                return mid  # Return index of target if found
            if nums[mid] >= nums[lo]:
                # Left half is sorted
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1  # Target is in the left sorted half
                else:
                    lo = mid + 1  # Target is in the right half
            else:
                # Right half is sorted
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1  # Target is in the right sorted half
                else:
                    hi = mid - 1  # Target is in the left half

        return -1  # Target not found

    def __duplicate(self, nums: List[int], target) -> bool:
        """
        Binary search function to determine if the target exists in a rotated sorted array with duplicates.

        Args:
        - nums: List of integers representing the rotated sorted array with duplicates.
        - target: Integer value to search for in the array.

        Returns:
        - True if target exists in the array, False otherwise.
        """
        n: int = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid: int = (lo + hi) // 2
            if nums[mid] == target:
                return True  # Return True if target found
            if nums[lo] == nums[mid] and nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
                continue  # Skip duplicates
            if nums[mid] >= nums[lo]:
                # Left half is sorted
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1  # Target is in the left sorted half
                else:
                    lo = mid + 1  # Target is in the right half
            else:
                # Right half is sorted
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1  # Target is in the right sorted half
                else:
                    hi = mid - 1  # Target is in the left half

        return False  # Target not found

    def search(self, nums: List[int], target: int) -> bool:
        """
        Wrapper function to perform binary search using __f method.

        Args:
        - nums: List of integers representing the rotated sorted array.
        - target: Integer value to search for in the array.

        Returns:
        - True if target exists in the array, False otherwise.
        """
        return self.__f(nums, target)


# Example usage:
nums: List[int] = [7, 8, 9, 0, 1, 2, 3, 4, 5]
solution: Solution = Solution()
print(solution.search(nums, 4))
