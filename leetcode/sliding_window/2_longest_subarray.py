"""Longest subarray with sum<=k."""

from typing import List


class Solution:
    def __brute(self, nums: List[int], k: int) -> int:
        """
        Find the length of the longest subarray with sum less than or equal to k using a brute-force approach.

        Args:
            nums (List[int]): List of integers.
            k (int): Target sum.

        Returns:
            int: Length of the longest subarray with sum less than or equal to k.
        """
        mx: int = 0  # Initialize the maximum length of the subarray
        n: int = len(nums)  # Get the length of the input list

        # Iterate through all possible starting indices of the subarray
        for i in range(n):
            s: int = 0  # Initialize the sum of the current subarray

            # Iterate through all possible ending indices of the subarray
            for j in range(i, n):
                s += nums[j]  # Update the sum with the next element

                # If the current sum is less than or equal to k, update the maximum length
                if s <= k:
                    mx = max(mx, j - i + 1)
                # If the current sum exceeds k, break out of the inner loop
                elif s > k:
                    break
        return mx

    def __better(self, nums: List[int], k: int) -> int:
        """
        Find the length of the longest subarray with sum less than or equal to k using a better approach.

        Args:
            nums (List[int]): List of integers.
            k (int): Target sum.

        Returns:
            int: Length of the longest subarray with sum less than or equal to k.
        """
        max_length: int = 0  # Maximum length of the subarray
        n: int = len(nums)  # Length of the input list
        left_ptr: int = 0  # Left pointer of the sliding window
        right_ptr: int = 0  # Right pointer of the sliding window
        current_sum: int = 0  # Current sum of elements in the sliding window

        # Iterate through the elements of the list
        while right_ptr < n:
            current_sum += nums[right_ptr]  # Expand the sliding window to the right

            # Shrink the sliding window from the left until the sum becomes <= k
            while current_sum > k:
                current_sum -= nums[left_ptr]
                left_ptr += 1
            if current_sum <= k:
                # Update the maximum length if the current subarray length is greater
                max_length = max(max_length, right_ptr - left_ptr + 1)

            # Move the right pointer to the next element
            right_ptr += 1

        return max_length

    def __optimal(self, nums: List[int], k: int) -> int:
        """
        Find the length of the longest subarray with sum less than or equal to k using a better approach.

        Args:
            nums (List[int]): List of integers.
            k (int): Target sum.

        Returns:
            int: Length of the longest subarray with sum less than or equal to k.
        """
        max_length: int = 0  # Maximum length of the subarray
        n: int = len(nums)  # Length of the input list
        left_ptr: int = 0  # Left pointer of the sliding window
        right_ptr: int = 0  # Right pointer of the sliding window
        current_sum: int = 0  # Current sum of elements in the sliding window

        # Iterate through the elements of the list
        while right_ptr < n:
            current_sum += nums[right_ptr]  # Expand the sliding window to the right

            # Shrink the sliding window from the left if the sum > k
            if current_sum > k:
                current_sum -= nums[left_ptr]
                left_ptr += 1
            if current_sum <= k:
                # Update the maximum length if the current subarray length is greater
                max_length = max(max_length, right_ptr - left_ptr + 1)

            # Move the right pointer to the next element
            right_ptr += 1

        return max_length

    def longest_subarry(self, nums: List[int], k: int) -> int:
        # return self.__brute(nums=nums, k=k)
        # return self.__better(nums=nums, k=k)
        return self.__optimal(nums=nums, k=k)


if __name__ == "__main__":
    nums: List[int] = [2, 5, 1, 7, 10]
    k: int = 14
    solution: Solution = Solution()
    print(solution.longest_subarry(nums=nums, k=k))
