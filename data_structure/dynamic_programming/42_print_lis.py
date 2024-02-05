"""Printing longest increasing subsequences."""

from typing import List


class Solution:
    def __get_lis(self, nums: List[int], n: int) -> List[int]:
        # Dynamic programming approach to find and print the Longest Increasing Subsequence
        dp: List[int] = [1] * n  # Stores the length of LIS ending at each index
        hsh: List[int] = [0] * n  # Stores the index of the previous element in LIS
        last_index: int = 0  # Keeps track of the last index of the LIS
        lis: int = 1  # Length of the LIS

        # Iterate over each element in the array
        for i in range(n):
            hsh[i] = i  # Initialize the previous index to be the current index
            # Iterate over previous elements to find the longest increasing subsequence
            for prev in range(0, i):
                if nums[prev] < nums[i] and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    hsh[i] = prev

            # Update the last index and length of the LIS
            if dp[i] > lis:
                lis = dp[i]
                last_index = i

        # Construct the LIS array
        lis_a: List[int] = [0] * lis
        lis_a[0] = nums[last_index]
        ind: int = 1
        while hsh[last_index] != last_index:
            last_index = hsh[last_index]
            lis_a[ind] = nums[last_index]
            ind += 1

        return lis_a[::-1]  # Reverse the array to get the correct order

    def get_lis(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        return self.__get_lis(nums, n)


if __name__ == "__main__":
    arr: List[int] = [10, 9, 2, 5, 3, 7, 101, 18]
    solution: Solution = Solution()
    print(solution.get_lis(nums=arr))
