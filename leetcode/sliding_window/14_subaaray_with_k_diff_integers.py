"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.
"""

from collections import defaultdict
from typing import DefaultDict, List, Set


class Solution:
    def __f(self, nums: List[int], k: int) -> int:
        """
        Count the number of good subarrays using a brute-force approach.

        Args:
            nums (List[int]): The input integer array.
            k (int): The number of different integers required in a good subarray.

        Returns:
            int: The number of good subarrays.
        """
        n: int = len(nums)
        cnt: int = 0

        # Iterate through each starting index
        for i in range(n):
            st: Set = set()
            # Iterate through each ending index
            for j in range(i, n):
                st.add(nums[j])

                # If the number of distinct integers equals k, increment count
                if len(st) == k:
                    cnt += 1
                # If the number of distinct integers exceeds k, exit the loop
                elif len(st) > k:
                    break
        return cnt

    def __better(self, nums: List[int], k: int) -> int:
        """
        Count the number of good subarrays using a sliding window approach.

        Args:
            nums (List[int]): The input integer array.
            k (int): The number of different integers required in a good subarray.

        Returns:
            int: The number of good subarrays.
        """
        n: int = len(nums)
        l = r = cnt = 0
        mp: DefaultDict = defaultdict(int)

        # Initialize a sliding window [l, r]
        while r < n:
            mp[nums[r]] += 1
            # Adjust the window to contain exactly k distinct integers
            while len(mp) > k:
                mp[nums[l]] -= 1
                if mp[nums[l]] == 0:
                    mp.pop(nums[l])
                l += 1

            # Increment the count by the length of the subarray [l, r]
            cnt = cnt + (r - l + 1)
            r += 1
        return cnt

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        Count the number of good subarrays with exactly k distinct integers.

        Args:
            nums (List[int]): The input integer array.
            k (int): The number of different integers required in a good subarray.

        Returns:
            int: The number of good subarrays.
        """
        # Uncomment the desired method call below
        # return self.__f(nums=nums, k=k)
        return self.__better(nums=nums, k=k) - self.__better(nums=nums, k=k - 1)


if __name__ == "__main__":
    nums: List[int] = [1, 2, 1, 3, 4]
    k: int = 3
    solution: Solution = Solution()
    print(solution.subarraysWithKDistinct(nums=nums, k=k))
