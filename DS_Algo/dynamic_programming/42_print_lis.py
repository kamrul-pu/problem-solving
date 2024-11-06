"""Printing longest increasing subsequences."""

from typing import List


class Solution:
    def __f(self, nums: List[int], n: int) -> List[int]:
        """
        This function computes the longest increasing subsequence (LIS) in the given list of numbers.
        It uses Dynamic Programming (DP) with backtracking to reconstruct the LIS.
        """
        # Step 1: Initialize DP array where dp[i] will store the length of the longest increasing
        # subsequence that ends at index i.
        dp: List[int] = [
            1
        ] * n  # Initialize all elements to 1 as a minimum subsequence length of 1.

        # Step 2: Initialize the `hsh` array to store the index of the previous element that forms the LIS.
        # This is useful for backtracking the LIS.
        hsh: List[int] = [
            col for col in range(n)
        ]  # Initially, each element points to itself.

        maxi: int = 1  # The length of the longest increasing subsequence found so far.
        last_index: int = 0  # The index of the last element in the LIS.

        # Step 3: Compute the LIS length using a DP approach.
        # Iterate through each element in the array starting from index 1.
        for i in range(1, n):
            # Step 3.1: Compare the current element `nums[i]` with previous elements `nums[0]` to `nums[i-1]`.
            for prev in range(0, i):
                # Step 3.2: If `nums[prev]` is less than `nums[i]` and the subsequence ending at `prev` + 1
                # is longer than the subsequence ending at `i`, update dp[i] and backtrack index in `hsh`.
                if nums[prev] < nums[i] and 1 + dp[prev] > dp[i]:
                    dp[i] = (
                        1 + dp[prev]
                    )  # Increase the length of the subsequence ending at i.
                    hsh[i] = (
                        prev  # Store the index of the previous element in the LIS at index `i`.
                    )

            # Step 3.3: Update `maxi` to keep track of the maximum LIS length and store the `last_index`.
            if dp[i] > maxi:
                maxi = dp[i]  # Update the maximum length of LIS found so far.
                last_index = i  # Update the index of the last element of the LIS.

        # Step 4: Reconstruct the actual LIS by backtracking using the `hsh` array.
        lis: List[int] = [0] * maxi  # Create an array to store the elements of the LIS.
        maxi -= 1  # Start from the end of the LIS.
        lis[maxi] = nums[last_index]  # Set the last element of the LIS.

        # Step 5: Backtrack to fill in the rest of the LIS elements.
        while last_index != hsh[last_index]:
            last_index = hsh[last_index]  # Move to the previous element in the LIS.
            maxi -= 1  # Move to the next index in the LIS array.
            lis[maxi] = nums[last_index]  # Set the element at the current position.

        # Step 6: Return the reconstructed LIS.
        return lis

    def get_lis(self, nums: List[int]) -> List[int]:
        """
        This is the public method to get the longest increasing subsequence from the input list `nums`.
        It calls the internal function __f() to calculate the LIS.
        """
        n: int = len(nums)  # Get the number of elements in the input list.
        return self.__f(
            nums, n
        )  # Call the internal function to calculate and return the LIS.


# Driver Code
if __name__ == "__main__":
    # Test input
    arr: List[int] = [10, 9, 2, 5, 3, 7, 101, 18]

    # Create an instance of the Solution class
    solution: Solution = Solution()

    # Get the Longest Increasing Subsequence and print it
    print(solution.get_lis(nums=arr))  # Expected output: [2, 3, 7, 101]
