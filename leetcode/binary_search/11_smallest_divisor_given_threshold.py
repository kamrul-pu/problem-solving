"""
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor,
divide all the array by it, and sum the division's result. Find the smallest divisor such that the
result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element.
(For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.
"""

from math import ceil
from typing import List


class Solution:
    def __f(self, nums: List[int], divisor: int) -> int:
        """
        Helper function to calculate the sum of divisions of array `nums`
        by a given `divisor`, rounded up to the nearest integer.

        Args:
        - nums: List of integers representing the array.
        - divisor: Integer, the divisor to divide each element of `nums`.

        Returns:
        - int: The sum of divisions of `nums` by `divisor`, rounded up.
        """
        s: int = 0
        for num in nums:
            s += ceil(num / divisor)
        return s

    def __brute(self, nums: List[int], threshold: int) -> int:
        """
        Brute-force approach to find the smallest divisor such that the
        sum of divisions of `nums` by this divisor does not exceed `threshold`.

        Args:
        - nums: List of integers representing the array.
        - threshold: Integer, the maximum allowed sum of divisions.

        Returns:
        - int: The smallest divisor found, or -1 if no valid divisor is found.
        """
        mx: int = max(nums)
        for i in range(1, mx + 1):
            s: int = self.__f(nums=nums, divisor=i)
            if s <= threshold:
                return i
        return -1

    def __optimal(self, nums: List[int], threshold: int) -> int:
        """
        Optimal approach using binary search to find the smallest divisor
        such that the sum of divisions of `nums` by this divisor does not exceed `threshold`.

        Args:
        - nums: List of integers representing the array.
        - threshold: Integer, the maximum allowed sum of divisions.

        Returns:
        - int: The smallest divisor found, or -1 if no valid divisor is found.
        """
        mx: int = max(nums)
        ans: int = mx
        lo, hi = 1, mx
        while lo <= hi:
            mid: int = (lo + hi) // 2
            s: int = self.__f(nums, mid)
            if s <= threshold:
                ans = min(ans, mid)  # Update answer if current mid divisor is valid
                hi = mid - 1  # Search for potentially smaller divisors
            else:
                lo = mid + 1  # Search for larger divisors

        return ans

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
        Main function to find the smallest divisor such that the sum of divisions
        of `nums` by this divisor does not exceed `threshold`.

        Args:
        - nums: List of integers representing the array.
        - threshold: Integer, the maximum allowed sum of divisions.

        Returns:
        - int: The smallest divisor found, or -1 if no valid divisor is found.
        """
        # Uncomment to use the brute-force approach
        # return self.__brute(nums, threshold)

        # Use the optimal binary search approach
        return self.__optimal(nums, threshold)


if __name__ == "__main__":
    nums: List[int] = [1, 2, 5, 9]
    threshold: int = 6
    solution: Solution = Solution()
    print(solution.smallestDivisor(nums=nums, threshold=threshold))
