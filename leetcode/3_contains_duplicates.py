"""Duplicate checker
Space O(1)
Time O(n)
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        index_dict = {}
        for i in range(len(nums)):
            if nums[i] in index_dict:
                return True
            else:
                index_dict[nums[i]] = i
        return False

    def containsDuplicateSet(self, nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    def containsDuplicateSetlength(self, nums: list[int]) -> bool:
        nums_set = set(nums)
        return len(nums_set) != len(nums)


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    solution = Solution()
    print(solution.containsDuplicate(nums=nums))
    nums = [1, 2, 3, 4]
    print(solution.containsDuplicate(nums=nums))
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(solution.containsDuplicateSetlength(nums=nums))
