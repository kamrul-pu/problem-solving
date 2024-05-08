"""
Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

from typing import List, Set, Tuple


class Solution:
    def generate(
        self,
        i: int,
        n: int,
        nums: List[int],
        subset: List[int],
        all_sets: Set[Tuple[int]],
    ) -> None:
        # Base case: When index i reaches the length of nums (n)
        if i == n:
            # Convert subset to a tuple and add to the set to avoid duplicates
            all_sets.add(tuple(sorted(subset)))
            return

        # Recursive call without including nums[i] in the subset
        self.generate(i + 1, n, nums, subset, all_sets)

        # Recursive call including nums[i] in the subset
        subset.append(nums[i])
        self.generate(i + 1, n, nums, subset, all_sets)
        subset.pop()  # Backtrack: Remove the last element to explore other combinations

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Set to store unique subsets as tuples (to avoid duplicate subsets)
        all_sets: Set = set()
        n: int = len(nums)

        # Start recursive generation of subsets
        self.generate(0, n, nums, [], all_sets)

        # Convert each tuple subset back to a list and append to the result list
        ans: List[List[int]] = []
        for item in all_sets:
            ans.append(list(item))

        return ans


if __name__ == "__main__":
    nums: List[int] = [1, 2, 2]
    solution: Solution = Solution()
    result: List[List[int]] = solution.subsetsWithDup(nums=nums)
    print(result)
