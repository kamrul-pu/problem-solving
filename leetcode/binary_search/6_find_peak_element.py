"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always
considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""

from typing import List


class Solution:
    def __brute(self, nums: List[int]) -> int:
        peaks: List[int] = []
        n: int = len(nums)

        # Traverse through the array
        for i in range(0, n, 1):
            # Check conditions to identify a peak element
            if i == 0 and nums[i] > nums[i + 1]:
                peaks.append(i)  # Peak element at the start of the array
            elif i == n - 1 and nums[i] > nums[i - 1]:
                peaks.append(i)  # Peak element at the end of the array
            elif nums[i - 1] < nums[i] > nums[i + 1]:
                peaks.append(i)  # Peak element in the middle of the array

        return peaks

    def __optimal(self, nums: List[int]) -> int:
        n: int = len(nums)

        # Edge cases
        if n == 1:
            return 0  # Single element array has its only element as peak

        # Check first and last elements separately
        if nums[0] > nums[1]:
            return 0  # First element is a peak
        if nums[n - 1] > nums[n - 2]:
            return n - 1  # Last element is a peak

        # Binary search to find a peak element
        lo, hi = 1, n - 2
        while lo <= hi:
            mid: int = (lo + hi) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid  # Found a peak element
            elif nums[mid - 1] > nums[mid]:
                hi = mid - 1  # Peak is in the left half
            else:
                lo = mid + 1  # Peak is in the right half

    def findPeakElement(self, nums: List[int]) -> int:
        """
        Main function to find any peak element in the array.

        Args:
        - nums: List of integers where a peak element needs to be found.

        Returns:
        - Index of any peak element found.
        """
        # Uncomment to use brute-force approach
        # return self.__brute(nums)

        # Use optimal approach for O(log n) time complexity
        return self.__optimal(nums)


if __name__ == "__main__":
    nums: List[int] = [1, 2, 1, 3, 5, 6, 4]
    solution: Solution = Solution()
    print(solution.findPeakElement(nums))
