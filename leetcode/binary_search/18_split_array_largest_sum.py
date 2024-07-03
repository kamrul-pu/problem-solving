"""
Given an integer array nums and an integer k, split nums into k non-empty
subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.
"""

from typing import List


class Solution:
    def __f(self, nums: List[int], n: int, s: int) -> int:
        # Helper function to determine the number of partitions needed
        partition: int = 1  # Start with one partition
        current_sum: int = 0

        for i in range(n):
            if current_sum + nums[i] <= s:
                current_sum += nums[i]  # Add current number to current partition
            else:
                partition += 1  # Need another partition
                current_sum = nums[i]  # Start a new partition with current number

        return partition

    def __optimal(self, nums: List[int], k: int) -> int:
        # Optimal method using binary search to find the minimized largest sum
        n: int = len(nums)
        mx: int = nums[0]  # Maximum number in the array
        total: int = nums[0]  # Total sum of all numbers in the array

        # Find the maximum and total sum of the array
        for i in range(1, n):
            mx = max(mx, nums[i])
            total += nums[i]

        lo, hi = mx, total  # Binary search bounds

        while lo <= hi:
            mid: int = (lo + hi) // 2  # Middle value
            partitions: int = self.__f(
                nums, n, mid
            )  # Get partitions required for current mid

            if partitions > k:
                lo = mid + 1  # If partitions needed are more than k, increase mid
            else:
                hi = (
                    mid - 1
                )  # If partitions needed are less than or equal to k, decrease mid

        return lo  # Return the minimized largest sum found

    def splitArray(self, nums: List[int], k: int) -> int:
        # Main function to call either brute force or optimal method
        # return self.__brute(nums, k)  # Uncomment to use brute force method
        return self.__optimal(nums, k)  # Use optimal method


if __name__ == "__main__":
    nums: List[int] = [7, 2, 5, 10, 8]
    k: int = 2
    solution: Solution = Solution()
    print(solution.splitArray(nums, k))  # Output: 18
