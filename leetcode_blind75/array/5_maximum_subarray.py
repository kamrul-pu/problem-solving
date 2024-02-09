"""Maximum subarray sum."""

from typing import List


from typing import List


class Solution:
    # Brute-force approach to find maximum subarray sum
    def __max_sum(self, nums: List[int], n: int) -> int:
        mx: int = -1e9
        # Iterate through each element as the starting point of a subarray
        for i in range(n):
            s: int = nums[i]
            # Iterate through elements from the starting point to find subarrays
            for j in range(i + 1, n):
                s += nums[j]
                # Update the maximum sum if the current subarray sum is greater
                mx = max(mx, s)
            # Update the maximum sum considering the single-element subarray
            mx = max(mx, s)

        # Ensure the maximum sum is non-negative
        return max(mx, 0)

    # Optimal approach to find maximum subarray sum
    def __max_sum_optimal(self, nums: List[int], n: int) -> int:
        mx_sum: int = -1e9
        cur_sum: int = 0
        # Iterate through the array to find maximum subarray sum
        for i in range(n):
            cur_sum += nums[i]
            # Update the maximum subarray sum if the current sum is greater
            mx_sum = max(mx_sum, cur_sum)
            # If the current sum becomes negative, reset it to 0
            if cur_sum < 0:
                cur_sum = 0

        return mx_sum

    # Main function to find maximum subarray sum
    def maxSubArray(self, nums: List[int]) -> int:
        n: int = len(nums)
        # Uncomment the appropriate function call based on the approach to use
        # return self.__max_sum(nums=nums, n=n)  # Brute-force approach
        return self.__max_sum_optimal(nums=nums, n=n)  # Optimal approach


# Main function to test the maxSubArray function
if __name__ == "__main__":
    nums: List[int] = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [1]
    # nums = [5, 4, -1, 7, 8]
    solution: Solution = Solution()
    print(solution.maxSubArray(nums=nums))
