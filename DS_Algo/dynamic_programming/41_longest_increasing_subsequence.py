"""Longest Increasing Subsequeces."""

from typing import List
import bisect


class Solution:
    # Helper function for Memoization approach
    def __f(
        self, i: int, prev: int, nums: List[int], n: int, dp: List[List[int]]
    ) -> int:
        # Base case: If we've reached the end of the array, no more subsequence
        if i == n:
            return 0

        # If the result has been computed for this state, return it from dp table
        if dp[i][prev + 1] != -1:
            return dp[i][prev + 1]

        # Option 1: Don't include the current element in the subsequence
        not_take: int = 0 + self.__f(i + 1, prev, nums, n, dp)

        # Option 2: Include the current element in the subsequence if it's larger than the previous element
        take: int = 0
        if prev == -1 or nums[i] > nums[prev]:
            take = 1 + self.__f(
                i + 1, i, nums, n, dp
            )  # Include nums[i] and move to next

        # Store the result in dp table and return the maximum of taking or not taking the element
        dp[i][prev + 1] = max(take, not_take)
        return dp[i][prev + 1]

    # Tabulation (Bottom-up) approach
    def __tabulation(self, nums: List[int], n: int) -> int:
        # Create a DP table where dp[i][prev] represents the length of LIS starting from index i
        dp: List[List[int]] = [[0 for col in range(n + 1)] for row in range(n + 1)]

        # Fill the DP table from bottom-up, starting from the last index of the array
        for i in range(n - 1, -1, -1):
            for prev in range(i - 1, -2, -1):  # prev can be from -1 to i-1
                # Option 1: Do not take the current element, so we look at the value for the next index
                not_take: int = 0 + dp[i + 1][prev + 1]

                # Option 2: Take the current element if it's larger than the previous element
                take: int = 0
                if prev == -1 or nums[i] > nums[prev]:
                    take = (
                        1 + dp[i + 1][i + 1]
                    )  # Include nums[i] and move to the next element

                # Store the best of both options in the DP table
                dp[i][prev + 1] = max(take, not_take)

        # The result will be stored in dp[0][0], which represents the best LIS starting from index 0
        return dp[0][0]

    # Optimized space approach using only two arrays (previous and current)
    def __optimal(self, nums: List[int], n: int) -> int:
        ahed: List[int] = [0 for col in range(n + 1)]  # Previous row in DP table
        cur: List[int] = [0 for row in range(n + 1)]  # Current row in DP table

        # Loop through the array in reverse order
        for i in range(n - 1, -1, -1):
            for prev in range(i - 1, -2, -1):
                # Option 1: Do not take the current element
                not_take: int = 0 + ahed[prev + 1]

                # Option 2: Take the current element if it's greater than the previous element
                take: int = 0
                if prev == -1 or nums[i] > nums[prev]:
                    take = 1 + ahed[i + 1]

                # Update the current row with the maximum of both options
                cur[prev + 1] = max(take, not_take)

            # Move the current row to the "ahead" row for the next iteration
            ahed = cur.copy()

        # The result is stored in ahed[0], which represents the best LIS starting from index 0
        return ahed[0]

    # Dynamic Programming (bottom-up) approach with a single array (classic O(n^2) DP)
    def __lis_single_arr(self, nums: List[int], n: int) -> int:
        dp: List[int] = [
            1 for col in range(n)
        ]  # Initialize the dp array where dp[i] represents LIS ending at i
        lis: int = (
            1  # The minimum length of LIS is 1 (every element is a subsequence itself)
        )

        # Loop through each element and find the longest subsequence ending at each index
        for i in range(n):
            for prev in range(
                0, i
            ):  # Check previous elements to see if they can form an increasing subsequence
                if nums[prev] < nums[i]:
                    dp[i] = max(
                        1 + dp[prev], dp[i]
                    )  # If nums[i] is larger, extend the LIS ending at prev
            lis = max(lis, dp[i])  # Keep track of the maximum LIS length found

        return lis

    # Using Binary Search and Greedy approach (O(n log n) time complexity)
    def __lis(self, nums: List[int]) -> int:
        n: int = len(nums)
        temp: List[int] = (
            []
        )  # This will store the elements in a sorted order that forms the LIS

        # Loop through each element in the array
        for i in range(1, n):
            if (
                nums[i] > temp[-1]
            ):  # If the current number is greater than the last element in LIS
                temp.append(nums[i])  # Add it to the LIS
            else:
                # Use binary search to find the position where nums[i] should be placed to maintain sorted order
                index = bisect.bisect_left(temp, nums[i])
                temp[index] = nums[i]  # Replace the element at that position

        # The length of temp array will be the length of the longest increasing subsequence
        return len(temp)

    # The main function to return the length of the Longest Increasing Subsequence
    def lengthOfLIS(self, nums: List[int]) -> int:
        n: int = len(nums)
        # Uncomment one of the following approaches to test

        # Memoization Approach (Top-Down)
        # dp: List[List[int]] = [[-1 for col in range(n)] for row in range(n)]
        # return self.__f(0, -1, nums, n, dp)

        # Tabulation Approach (Bottom-Up)
        # return self.__tabulation(nums, n)

        # Optimized Space Approach (Bottom-Up)
        # return self.__optimal(nums, n)

        # Classic DP Approach (O(n^2))
        return self.__lis_single_arr(nums, n)


if __name__ == "__main__":
    arr: List[int] = [10, 9, 2, 5, 3, 7, 101, 18]
    solution: Solution = Solution()
    print(solution.lengthOfLIS(nums=arr))  # Output: 4 (The LIS is [2, 3, 7, 101])
