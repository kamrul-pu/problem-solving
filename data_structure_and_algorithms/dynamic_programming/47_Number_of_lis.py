"""Number of longest increasing subsequences."""

from typing import List


class Solution:
    def __f(self, nums: List[int], n: int) -> int:
        # Initialize an array to store the length of the longest increasing subsequences ending at each index
        dp: List[int] = [1] * n
        # Initialize an array to store the count of the longest increasing subsequences ending at each index
        cnt: List[int] = [1] * n
        # Initialize a variable to store the maximum length of the longest increasing subsequence
        maxi: int = 1

        # Iterate through the array
        for i in range(n):
            # Iterate through all previous elements
            for j in range(i):
                # If the current element is greater than the previous element
                # and adding the current element to the previous subsequence results in a longer subsequence
                if nums[i] > nums[j] and dp[i] < 1 + dp[j]:
                    # Update the length of the longest increasing subsequence ending at the current index
                    dp[i] = 1 + dp[j]
                    # Update the count of the longest increasing subsequence ending at the current index
                    cnt[i] = cnt[j]
                # If the current element is greater than the previous element
                # and adding the current element to the previous subsequence results in a subsequence with the same length
                elif nums[i] > nums[j] and dp[j] + 1 == dp[i]:
                    # Increment the count of the longest increasing subsequence ending at the current index
                    cnt[i] += cnt[j]
            # Update the maximum length of the longest increasing subsequence
            maxi = max(maxi, dp[i])

        # Initialize a variable to store the number of longest increasing subsequences
        nos: int = 0
        # Iterate through the array
        for i in range(n):
            # If the length of the longest increasing subsequence ending at the current index equals the maximum length
            if dp[i] == maxi:
                # Add the count of the longest increasing subsequence ending at the current index to the total count
                nos += cnt[i]

        # Return the number of longest increasing subsequences
        return nos

    def findNumberOfLIS(self, nums: List[int]) -> int:
        # Get the length of the input array
        n: int = len(nums)
        # Call the helper function to find the number of longest increasing subsequences
        return self.__f(nums, n)


if __name__ == "__main__":
    nums: List[int] = [1, 3, 5, 4, 7]
    nums: List[int] = [2, 2, 2, 2, 2]
    solution: Solution = Solution()
    # Print the number of longest increasing subsequence
    print(solution.findNumberOfLIS(nums=nums))
