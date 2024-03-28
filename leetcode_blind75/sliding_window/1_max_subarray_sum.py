"""Maximum Sub array sum."""

from typing import List


class Solution:
    def max_subarray_sum(self, nums: List[int], k: int) -> int:
        """
        Find the maximum sum of subarrays of length k in the given list of numbers.

        Args:
            nums (List[int]): List of integers.
            k (int): Length of subarrays.

        Returns:
            int: Maximum sum of subarrays of length k.
        """
        n: int = len(nums)
        # Initialize mx to negative infinity
        max_sum: int = float("-inf")

        # Check if k is greater than the length of nums
        if k > n:
            return float("-inf")

        # Initialize max_sum with the sum of the first k elements
        max_sum = sum(nums[0:k])
        current_sum: int = max_sum

        # Initialize left and right pointers for the sliding window
        left: int = 0
        right: int = k - 1

        # Slide the window and update the maximum sum
        while right < n - 1:
            # Remove the leftmost element from the current sum
            current_sum -= nums[left]
            left += 1
            # Move the window to the right and add the new element
            right += 1
            current_sum += nums[right]
            # Update the maximum sum if the current sum is greater
            max_sum = max(max_sum, current_sum)

        return max_sum


if __name__ == "__main__":
    nums: List[int] = [-1, 2, 3, 3, 4, 5, -1]
    k: int = 4
    solution: Solution = Solution()
    print(solution.max_subarray_sum(nums=nums, k=k))
