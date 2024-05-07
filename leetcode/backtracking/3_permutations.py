"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible permutations of distinct integers in `nums`.

        Parameters:
        - nums: List of distinct integers for which permutations are to be generated.

        Returns:
        - List of all possible permutations of `nums`.
        """
        result: List[List[int]] = []  # List to store all permutations

        # Base case: If `nums` has only one element, return a list containing `nums`
        if len(nums) == 1:
            return [nums[:]]  # Return a copy of `nums` as a permutation

        # Explore each number in `nums` as the first element of permutations
        for i in range(len(nums)):
            n = nums.pop(0)  # Remove the current number at index 0
            perms = self.permute(
                nums
            )  # Recursively generate permutations for the rest of the list

            # Append the current number (`n`) to each permutation generated from the rest of the list (`perms`)
            for perm in perms:
                perm.append(n)  # Append `n` to the end of each permutation
            result.extend(
                perms
            )  # Extend the result list with the permutations generated
            nums.append(
                n
            )  # Restore the current number back to its original position in `nums`

        return result  # Return the list of all permutations


if __name__ == "__main__":
    nums: List[int] = [1, 2, 3]
    solution: Solution = Solution()
    result: List[List[int]] = solution.permute(nums=nums)
    print(result)
