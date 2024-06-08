"""
Given an integer array nums, return true if you can partition the array into two subsets
such that the sum of the elements in both subsets is equal or false otherwise.
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Get the length of the input array
        n = len(nums)
        # Calculate the total sum of all elements in the array
        s = sum(nums)
        # If the total sum is odd, it's impossible to partition the array into two subsets with equal sum
        if s % 2 == 1:
            return False
        # Calculate the target sum for each subset, which is half of the total sum
        target = s // 2
        # Create a boolean array dp of size target + 1, initialized with False
        dp = [False] * (target + 1)
        # Mark dp[0] as True, since it's always possible to have an empty subset with sum 0
        dp[0] = True
        # Iterate through each number in the input array
        for num in nums:
            # Iterate backwards through the dp array starting from target down to num
            # This is because updating dp[j] might depend on the previous value of dp[j - num]
            for j in range(target, num - 1, -1):
                # Update dp[j] to True if either dp[j] or dp[j - num] is True
                # This means if we can form a subset with sum j using the current num
                # or if we can form a subset with sum j - num and add the current num to it
                dp[j] = dp[j] or dp[j - num]
            # if target value is found then break the loop and return the result
            if dp[target] == True:
                return True
        # Return whether it's possible to form a subset with sum equal to the target
        return dp[target]


# Example usage:
if __name__ == "__main__":
    nums: List[int] = [1, 5, 11, 5]
    solution: Solution = Solution()
    print(solution.canPartition(nums=nums))
