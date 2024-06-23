"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

from collections import defaultdict
from typing import Dict, List


class Solution:
    def __brute(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        cnt: int = 0
        for i in range(n):
            for j in range(i, n):
                s: int = 0
                for k in range(i, j + 1):
                    s += nums[k]
                if s == k:
                    cnt += 1
        return cnt

    def __better(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        cnt: int = 0
        for i in range(n):
            s: int = 0
            for j in range(i, n):
                s += nums[j]
                if s == k:
                    cnt += 1
        return cnt

    def __optimal(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        cnt: int = 0
        hsh: Dict[int, int] = defaultdict(
            int
        )  # Dictionary to store prefix sums and their frequencies
        hsh[0] = 1  # Initialize with prefix sum of 0 with count 1
        pre_sum: int = 0  # Variable to store the running prefix sum

        for i in range(n):
            pre_sum += nums[i]  # Update the prefix sum with the current element
            rem: int = pre_sum - k  # Calculate the remainder needed to achieve sum k

            cnt += hsh[
                rem
            ]  # Add the count of how many times 'rem' has appeared as a prefix sum
            hsh[
                pre_sum
            ] += 1  # Update the count of the current prefix sum in the dictionary

        return cnt

    def subarraySum(self, nums: List[int], k: int) -> int:
        # Uncomment one of the following to choose the method to execute
        # return self.__brute(nums=nums, k=k)   # Brute force method
        # return self.__better(nums=nums, k=k)  # Improved method using cumulative sum
        return self.__optimal(nums=nums, k=k)  # Optimal method using hash map


if __name__ == "__main__":
    nums: List[int] = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
    k: int = 3
    solution: Solution = Solution()
    print(solution.subarraySum(nums=nums, k=k))
