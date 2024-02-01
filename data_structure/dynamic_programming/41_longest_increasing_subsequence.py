"""Longest Increasing Subsequeces."""

from typing import List


class Solution:
    def __f(
        self, i: int, prev: int, nums: List[int], n: int, dp: List[List[int]]
    ) -> int:
        if i == n:
            return 0
        if dp[i][prev + 1] != -1:
            return dp[i][prev + 1]
        not_take: int = 0 + self.__f(i + 1, prev, nums, n, dp)
        take: int = 0
        if prev == -1 or nums[i] > nums[prev]:
            take = 1 + self.__f(i + 1, i, nums, n, dp)

        dp[i][prev + 1] = max(take, not_take)
        return dp[i][prev + 1]

    def __lis_tabulation(self, nums: List[int], n: int) -> int:
        dp: List[List[int]] = [[0 for col in range(n + 1)] for row in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for prev in range(i - 1, -2, -1):
                not_take: int = 0 + dp[i + 1][prev + 1]
                take: int = 0
                if prev == -1 or nums[i] > nums[prev]:
                    take = 1 + dp[i + 1][i + 1]

                dp[i][prev + 1] = max(take, not_take)
        return dp[0][0]

    def __list_optimal(self, nums: List[int], n: int) -> int:
        ahed: List[int] = [0 for col in range(n + 1)]
        cur: List[int] = [0 for row in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for prev in range(i - 1, -2, -1):
                not_take: int = 0 + ahed[prev + 1]
                take: int = 0
                if prev == -1 or nums[i] > nums[prev]:
                    take = 1 + ahed[i + 1]

                cur[prev + 1] = max(take, not_take)
            ahed = cur.copy()

        return ahed[0]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n: int = len(nums)
        # dp: List[List[int]] = [[-1 for col in range(n)] for row in range(n)]
        # return self.__f(0, -1, nums, n, dp)
        # return self.__lis_tabulation(nums, n)
        return self.__list_optimal(nums, n)


if __name__ == "__main__":
    arr: List[int] = [10, 9, 2, 5, 3, 7, 101, 18]
    solution: Solution = Solution()
    print(solution.lengthOfLIS(nums=arr))
