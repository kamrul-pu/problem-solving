"""
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

from typing import List


class Solution:
    def __f(
        self, nums: List[int], i: int, n: int, s: List[int], sets: List[List[int]]
    ) -> None:
        # Base case: If we have processed all elements (i.e., reached the end of the array)
        if i == n:
            # Append the current subset `s` to the result sets
            sets.append(s.copy())
            return

        # Recursive call without including the current element `nums[i]` in the subset `s`
        self.__f(nums, i + 1, n, s, sets)

        # Recursive call including the current element `nums[i]` in the subset `s`
        s.append(nums[i])
        self.__f(nums, i + 1, n, s, sets)
        s.pop()  # Backtrack: Remove the last element to explore other subsets

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n: int = len(nums)
        sets: List[List[int]] = []
        # Start the recursive generation of subsets from index 0 with an empty subset `s`
        self.__f(nums, 0, n, [], sets)
        return sets


if __name__ == "__main__":
    nums: List[int] = [1, 2, 3]
    solution: Solution = Solution()
    print(solution.subsets(nums=nums))
