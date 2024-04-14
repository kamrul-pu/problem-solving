class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

    def productExceptSelfSingleLoop(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = [1] * length

        prefix, postfix = 1, 1

        for i in range(length):
            result[i] *= prefix
            prefix *= nums[i]

            result[length - 1 - i] *= postfix
            postfix *= nums[length - 1 - i]

        return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.productExceptSelf(nums=nums))
