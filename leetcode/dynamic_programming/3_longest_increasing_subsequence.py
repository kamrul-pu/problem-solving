"""Longest increasing subsequences of an array."""

from typing import List


class Solution:
    def __f(
        self, i: int, prev: int, n: int, nums: List[int], dp: List[List[int]]
    ) -> int:
        """
        Recursive helper function to find the length of the longest increasing subsequence.

        Args:
            i (int): Current index being considered.
            prev (int): Index of the previous element in the subsequence.
            n (int): Length of the array.
            nums (List[int]): The array of integers.
            dp (List[List[int]]): Memoization table to store computed values.

        Returns:
            int: Length of the longest increasing subsequence.
        """
        if i == n:
            return 0
        if dp[i][prev + 1] != -1:
            return dp[i][prev + 1]
        not_take: int = 0 + self.__f(i + 1, prev, n, nums, dp)
        take: int = -1e9
        if prev == -1 or nums[i] > nums[prev]:
            take = 1 + self.__f(i + 1, i, n, nums, dp)
        dp[i][prev + 1] = max(take, not_take)
        return dp[i][prev + 1]

    def __lis_tabulation(self, nums: List[int], n: int) -> int:
        """
        Tabulation approach to find the length of the longest increasing subsequence.

        Args:
            nums (List[int]): The array of integers.
            n (int): Length of the array.

        Returns:
            int: Length of the longest increasing subsequence.
        """
        dp: List[List[int]] = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for prev in range(i - 1, -2, -1):
                not_take: int = 0 + dp[i + 1][prev + 1]
                take: int = -1e9
                if prev == -1 or nums[i] > nums[prev]:
                    take = 1 + dp[i + 1][i + 1]
                dp[i][prev + 1] = max(take, not_take)

        return dp[0][0]

    def __lis_optimal(self, nums: List[int], n: int) -> int:
        """
        Optimal space complexity approach to find the length of the longest increasing subsequence.

        Args:
            nums (List[int]): The array of integers.
            n (int): Length of the array.

        Returns:
            int: Length of the longest increasing subsequence.
        """
        ahed: List[int] = [0 for _ in range(n + 1)]
        cur: List[int] = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for prev in range(i - 1, -2, -1):
                not_take: int = 0 + ahed[prev + 1]
                take: int = -1e9
                if prev == -1 or nums[i] > nums[prev]:
                    take = 1 + ahed[i + 1]
                cur[prev + 1] = max(take, not_take)

            ahed = cur

        return ahed[0]

    def __lis_single_arr(self, nums: List[int], n: int) -> int:
        """
        Efficient approach using a single array to find the length of the longest increasing subsequence.

        Args:
            nums (List[int]): The array of integers.
            n (int): Length of the array.

        Returns:
            int: Length of the longest increasing subsequence.
        """
        dp: List[int] = [1 for col in range(n)]
        lis: int = 1
        for i in range(n):
            for prev in range(0, i):
                if nums[prev] < nums[i]:
                    dp[i] = max(1 + dp[prev], dp[i])
            lis = max(lis, dp[i])

        return lis

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Function to find the length of the longest increasing subsequence.

        Args:
            nums (List[int]): The array of integers.

        Returns:
            int: Length of the longest increasing subsequence.
        """
        n: int = len(nums)
        # dp: List[int] = [[-1] * (n + 1) for _ in range(n + 1)]
        # return self.__f(0, -1, n, nums, dp)
        # return self.__lis_tabulation(nums=nums, n=n)
        # return self.__lis_optimal(nums=nums, n=n)
        return self.__lis_single_arr(nums=nums, n=n)


if __name__ == "__main__":
    nums: List[int] = [10, 9, 2, 5, 3, 7, 101, 18]
    solution: Solution = Solution()
    print(solution.lengthOfLIS(nums=nums))
