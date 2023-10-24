class Solution:
    # Brute Force solution
    # Complexity O(n^2)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

    def twoSumOptimized(self, nums: list[int], target: int) -> list[int]:
        index_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in index_dict:
                return [index_dict[target - nums[i]], i]
            else:
                index_dict[nums[i]] = i

        return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums=nums, target=target))
    print(solution.twoSumOptimized(nums=nums, target=target))
    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums=nums, target=target))
    print(solution.twoSumOptimized(nums=nums, target=target))
