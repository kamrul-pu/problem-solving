"""Longest Bitonic Subsequences."""

from typing import List


class Solution:

    def __f(self, nums: list[int], n: int) -> int:
        # Initialize an array to store the length of the increasing subsequence ending at each index
        dp1: list[int] = [1] * n
        # Iterate through the array from left to right
        for i in range(n):
            # Iterate through all previous elements to find the longest increasing subsequence
            for j in range(i):
                # If the current element is greater than the previous element
                # and adding the current element to the previous subsequence results in a longer subsequence
                if nums[i] > nums[j] and dp1[i] < 1 + dp1[j]:
                    # Update the length of the increasing subsequence ending at the current index
                    dp1[i] = 1 + dp1[j]

        # Initialize an array to store the length of the decreasing subsequence starting at each index
        dp2: list[int] = [1] * n
        # Iterate through the array from right to left
        for i in range(n - 1, -1, -1):
            # Iterate through all following elements to find the longest decreasing subsequence
            for j in range(n - 1, i, -1):
                # If the current element is greater than the following element
                # and adding the current element to the following subsequence results in a longer subsequence
                if nums[i] > nums[j] and dp2[i] < 1 + dp2[j]:
                    # Update the length of the decreasing subsequence starting at the current index
                    dp2[i] = 1 + dp2[j]

        # Initialize a variable to store the maximum length of the bitonic subsequence
        maxi: int = 0
        # Iterate through all indices
        for i in range(n):
            # Update the maximum length of the bitonic subsequence by considering
            # the sum of the lengths of the increasing and decreasing subsequences at each index
            maxi = max(maxi, dp1[i] + dp2[i] - 1)

        # Return the maximum length of the bitonic subsequence
        return maxi

    def LongestBitonicSequence(self, nums):
        # Get the length of the input array
        n: int = len(nums)
        # Call the helper function to calculate the length of the longest bitonic subsequence
        return self.__f(nums, n)


if __name__ == "__main__":
    nums: List[int] = [1, 11, 2, 10, 4, 5, 2, 1]
    solution: Solution = Solution()
    # Print the length of the longest bitonic subsequence
    print(solution.LongestBitonicSequence(nums=nums))
