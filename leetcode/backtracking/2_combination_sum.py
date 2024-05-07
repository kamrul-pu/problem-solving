"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique
combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than
150 combinations for the given input.
"""

from typing import List


class Solution:
    def __f(
        self,
        i: int,
        n: int,
        nums: List[int],
        target: int,
        s: int,
        subset: List[int],
        ans: List[List[int]],
    ) -> None:
        """
        Helper function to recursively find all combinations of numbers from `nums`
        that sum up to `target`.

        Parameters:
        - i: Current index in the `nums` array.
        - n: Length of the `nums` array.
        - nums: The array of integers to choose from.
        - target: The target sum we want to achieve.
        - s: Current sum of numbers in the `subset`.
        - subset: Current subset of numbers being considered.
        - ans: List to store valid combinations that sum to `target`.
        """
        if i == n:
            # Base case: If we have reached the end of the `nums` array
            # Check if the current `subset` sums up to `target`
            if s == target:
                ans.append(subset.copy())
            return

        # Explore two choices for each number:
        # 1. Include `nums[i]` in the subset
        # 2. Exclude `nums[i]` from the subset
        # Note: The same number can be included multiple times due to unlimited selection
        if s > target:
            return  # If the current sum `s` exceeds `target`, stop exploring this path

        # Option 1: Include `nums[i]` in the subset
        subset.append(nums[i])
        self.__f(i, n, nums, target, s + nums[i], subset, ans)
        subset.pop()  # Backtrack after recursive call

        # Option 2: Exclude `nums[i]` from the subset and move to the next number
        self.__f(i + 1, n, nums, target, s, subset, ans)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Main function to find all unique combinations of `candidates` that sum up to `target`.

        Parameters:
        - candidates: List of distinct integers to choose from.
        - target: The target sum to achieve with combinations.

        Returns:
        - List of all unique combinations of `candidates` that sum to `target`.
        """
        n: int = len(candidates)
        subset: List[int] = []  # Current subset being considered
        ans: List[List[int]] = []  # List to store valid combinations

        # Start exploring combinations from the beginning of `candidates` (index 0)
        # Initial sum `s` is 0 (empty subset)
        self.__f(0, n, candidates, target, 0, subset, ans)

        return ans


if __name__ == "__main__":
    candidates: List[int] = [2, 3, 5]
    target: int = 8
    solution: Solution = Solution()
    result: List[List[int]] = solution.combinationSum(
        candidates=candidates, target=target
    )
    print(result)
