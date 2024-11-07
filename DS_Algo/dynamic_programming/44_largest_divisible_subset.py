"""Largest Divisible subset using dynamic programming."""

from typing import List


class Solution:
    # Helper method to compute the largest divisible subset using dynamic programming
    def __get_lds(self, nums: List[int], n: int) -> List[int]:
        # dp[i] stores the length of the longest divisible subset that ends at index i
        dp: List[int] = [
            1 for _ in range(n)
        ]  # Initialize dp array with 1 (every number can be a subset of size 1 by itself)

        # hsh[i] stores the index of the previous element in the subset that ends at index i
        hsh: List[int] = [
            col for col in range(n)
        ]  # hsh will be used to reconstruct the subset

        last_index: int = (
            0  # Variable to track the index of the last element of the largest subset found
        )
        lis: int = (
            1  # The length of the longest divisible subset, starting with 1 as every element is divisible by itself
        )

        # Iterate over the array to fill dp and hsh arrays
        for i in range(n):
            hsh[i] = i  # Initially, the previous index for each element is itself
            # Check all previous elements to see if we can form a divisible subset
            for prev in range(0, i):
                if nums[i] % nums[prev] == 0 and dp[prev] + 1 > dp[i]:
                    # If nums[i] is divisible by nums[prev], and including nums[i] forms a longer subset
                    dp[i] = dp[prev] + 1  # Update dp[i] to reflect the longer subset
                    hsh[i] = (
                        prev  # Update the previous index of i to prev (i is now part of the subset ending at prev)
                    )

            # If the subset ending at i is the longest found so far, update the last_index and lis
            if dp[i] > lis:
                lis = dp[i]  # Update the length of the longest subset found
                last_index = i  # Update the index of the last element in the subset

        # Reconstruct the largest divisible subset from the hsh array
        lis_a: List[int] = [0] * lis  # Initialize an array to store the result
        lis -= 1  # Decrease the length since we start filling from the last index of the subset

        # Start from the last index and trace back to construct the largest subset
        lis_a[lis] = nums[last_index]
        while hsh[last_index] != last_index:  # While there is a valid previous index
            lis -= 1  # Move backwards in the subset
            last_index = hsh[last_index]  # Move to the previous element in the subset
            lis_a[lis] = nums[last_index]  # Add that element to the result

        return lis_a  # Return the largest divisible subset found

    # Main method to find and return the largest divisible subset
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n: int = len(nums)  # Get the length of the input list
        nums.sort()  # Sort the list to make it easier to form the divisible subsets
        return self.__get_lds(
            nums, n
        )  # Call the helper method to get the largest divisible subset


# Example usage:
if __name__ == "__main__":
    arr: List[int] = [1, 16, 7, 8, 4]  # Example input list
    solution: Solution = Solution()  # Create an instance of the Solution class
    print(
        solution.largestDivisibleSubset(nums=arr)
    )  # Print the largest divisible subset
