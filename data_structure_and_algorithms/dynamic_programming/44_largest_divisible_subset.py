"""Largest Divisible subset using dynamic programming."""

from typing import List


class Solution:
    def __get_lds(self, nums: List[int], n: int) -> List[int]:
        # Dynamic programming approach to find and print the Longest divisible Subset
        dp: List[int] = [
            1 for col in range(n)
        ]  # Stores the length of LIS ending at each index
        hsh: List[int] = [
            0 for col in range(n)
        ]  # Stores the index of the previous element in LIS
        last_index: int = 0  # Keeps track of the last index of the LIS
        lis: int = 1  # Length of the LIS

        # Iterate over each element in the array
        for i in range(n):
            hsh[i] = i  # Initialize the previous index to be the current index
            # Iterate over previous elements to find the longest  divisible Subset
            for prev in range(0, i):
                if nums[i] % nums[prev] == 0 and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    hsh[i] = prev

            # Update the last index and length of the LIS
            if dp[i] > lis:
                lis = dp[i]
                last_index = i

        # Construct the LDS array
        lis_a: List[int] = [0] * lis
        lis_a[0] = nums[last_index]
        ind: int = 1
        while hsh[last_index] != last_index:
            last_index = hsh[last_index]
            lis_a[ind] = nums[last_index]
            ind += 1

        return lis_a[::-1]  # Reverse the array to get the correct order

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        nums.sort()
        return self.__get_lds(nums, n)


if __name__ == "__main__":
    arr: List[int] = [1, 16, 7, 8, 4]
    solution: Solution = Solution()
    print(solution.largestDivisibleSubset(nums=arr))
