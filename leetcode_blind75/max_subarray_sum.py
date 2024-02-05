from typing import List


class Solution:
    # def __f(self, i: int, n: int, nums: List[int]) -> int:
    #     if i == n:
    #         return 0
    #     take: int = nums[i] + self.__f(i + 1, n, nums)
    #     not_take: int = 0 + self.__f(i + 1, n, nums)
    #     return max(take, not_take)

    # def maxSubArray(self, nums: List[int]) -> int:
    #     n: int = len(nums)
    #     return self.__f(0, n, nums)

    def maxSubArray(self, nums):
        ans = float("-inf")
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum)
        return ans


if __name__ == "__main__":
    nums: List[int] = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [5, 4, -1, 7, 8]
    solution: Solution = Solution()
    print(solution.maxSubArray(nums=nums))
