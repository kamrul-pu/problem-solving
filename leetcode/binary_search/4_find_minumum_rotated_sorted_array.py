"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

from typing import List


class Solution:
    def __brute(self, nums: List[int]) -> int:
        n: int = len(nums)
        mn: int = nums[0]
        for i in range(1, n):
            mn = min(mn, nums[i])  # Update minimum element found so far

        return mn

    def __better(self, nums: List[int]) -> int:
        n: int = len(nums)
        mn: int = min(nums[0], nums[n - 1])  # Compare first and last elements
        l, r = 1, n - 2  # Initialize pointers for the rest of the array
        while l <= r:
            mn = min(mn, nums[l], nums[r])  # Update minimum element found so far
            l += 1
            r -= 1

        return mn

    def __optimal(self, nums: List[int]) -> int:
        n: int = len(nums)
        mn: int = float("inf")  # Initialize minimum element as infinity
        lo, hi = 0, n - 1
        while lo <= hi:
            mid: int = (lo + hi) // 2
            if nums[mid] >= nums[lo]:
                mn = min(mn, nums[lo])  # Update minimum element found so far
                lo = mid + 1  # Search in the right half
            else:
                mn = min(mn, nums[mid])  # Update minimum element found so far
                hi = mid - 1  # Search in the left half

        return mn

    def findMin(self, nums: List[int]) -> int:
        """
        Main function to find the minimum element in a rotated sorted array.

        Args:
        - nums: List of integers representing the rotated sorted array.

        Returns:
        - Minimum element in the array.
        """
        return self.__optimal(nums)  # Call the optimal method for finding minimum


if __name__ == "__main__":
    nums: List[int] = [4, 5, 6, 7, 0, 1, 2]
    solution: Solution = Solution()
    print(solution.findMin(nums))
