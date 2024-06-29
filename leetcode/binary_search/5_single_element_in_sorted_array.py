"""
You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
"""

from typing import List


class Solution:
    def __brute(self, nums: List[int]) -> int:
        """
        Brute-force approach to find the single element that appears only once.

        Args:
        - nums: List of integers where every element appears twice except for one.

        Returns:
        - The single element that appears only once.
        """
        ans: int = 0
        for num in nums:
            ans ^= num  # Using XOR to find the single element

        return ans

    def __optimal(self, nums: List[int]) -> int:
        """
        Optimal approach to find the single element that appears only once using binary search.

        Args:
        - nums: List of integers where every element appears twice except for one.

        Returns:
        - The single element that appears only once.
        """
        n: int = len(nums)

        # Edge cases
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        # Binary search to find the single element
        lo, hi = 1, n - 2
        while lo <= hi:
            mid: int = (lo + hi) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]  # Found the single element
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (
                mid % 2 == 0 and nums[mid] == nums[mid + 1]
            ):
                lo = mid + 1  # Move right if mid is part of a pair
            else:
                hi = mid - 1  # Move left if mid is not part of a pair

        return -1  # Edge case where single element is not found (should not happen)

    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Main function to find the single element that appears only once.

        Args:
        - nums: List of integers where every element appears twice except for one.

        Returns:
        - The single element that appears only once.
        """
        # return self.__brute(nums)  # Uncomment to use brute-force approach
        return self.__optimal(nums)  # Use optimal approach for O(log n) time complexity


if __name__ == "__main__":
    nums: List[int] = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    solution: Solution = Solution()
    print(solution.singleNonDuplicate(nums))
