"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

from typing import List


class Solution:
    def __brute(self, nums: List[int], k: int) -> int:
        max_len: int = 0
        n: int = len(nums)

        # Iterate through each index of the array
        for i in range(n):
            zeros: int = 0
            # Consider each subarray starting from index i
            for j in range(i, n):
                # Count the number of zeros encountered
                if nums[j] == 0:
                    zeros += 1
                # If the number of zeros encountered does not exceed k,
                # update the length of the current subarray
                if zeros <= k:
                    length: int = j - i + 1
                    max_len = max(max_len, length)
                else:
                    break

        return max_len

    def __better(self, nums: List[int], k: int) -> int:
        max_len: int = 0
        n: int = len(nums)
        left = right = zeros = 0

        # Use a sliding window approach to iterate through the array
        while right < n:
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            if zeros <= k:
                length: int = right - left + 1
                max_len = max(max_len, length)
            right += 1

        return max_len

    def __optimal(self, nums: List[int], k: int) -> int:
        max_len: int = 0
        n: int = len(nums)
        left = right = zeros = 0

        # Use a sliding window approach to iterate through the array
        while right < n:
            if nums[right] == 0:
                zeros += 1

            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            if zeros <= k:
                length: int = right - left + 1
                max_len = max(max_len, length)
            right += 1

        return max_len

    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Finds the maximum number of consecutive 1's in the array if you can flip at most k 0's.

        Args:
            nums (List[int]): The binary array.
            k (int): The maximum number of 0's that can be flipped.

        Returns:
            int: The maximum number of consecutive 1's.
        """
        # return self.__brute(nums=nums, k=k)
        # return self.__better(nums=nums, k=k)
        return self.__optimal(nums=nums, k=k)


if __name__ == "__main__":
    nums: List[int] = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k: int = 2
    solution: Solution = Solution()
    print(solution.longestOnes(nums=nums, k=k))
