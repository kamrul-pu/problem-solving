class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        missing_num = 0
        for i in range(n + 1):
            if i == n:
                return i

            if nums[i] != i:
                return i

    def missingNumber2(self, nums: list[int]) -> int:
        return sum(range(1, len(nums) + 1)) - sum(nums)

    def missingNumber3(self, nums: list[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result += i - nums[i]
        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 3]
    print(solution.missingNumber3(nums))
