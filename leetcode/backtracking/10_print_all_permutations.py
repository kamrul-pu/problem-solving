"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

from typing import List


class Solution:
    def __f(
        self,
        nums: List[int],
        n: int,
        ds: List[int],
        mp: List[bool],
        result: List[List[int]],
    ) -> None:
        """
        Helper function for generating permutations recursively.

        Args:
            nums: The list of distinct integers.
            n: The length of the input list.
            ds: The current permutation being generated.
            mp: A list to keep track of which numbers have been used in the current permutation.
            result: The list to store all the generated permutations.
        """
        if len(ds) == n:
            # If the current permutation has reached the desired length, add it to the result list.
            result.append(ds[:])
            return
        for i in range(0, n):
            if not mp[i]:
                # If the number at index i has not been used in the current permutation, add it to the permutation.
                ds.append(nums[i])
                mp[i] = True  # Mark the number as used.
                # Recur with the updated permutation and mark the number as used.
                self.__f(nums, n, ds, mp, result)
                ds.pop()  # Backtrack: remove the last added number to explore other possibilities.
                mp[i] = False  # Mark the number as unused for the next permutation.

    def __optimal(self, i: int, nums: List[int], ans: List[List[int]]) -> None:
        """
        Helper function for generating permutations using backtracking.

        Args:
            i: The current index of the input list.
            nums: The list of distinct integers.
            ans: The list to store all the generated permutations.
        """
        if i == len(nums):
            # If the current index has reached the end of the list, add the current permutation to the result.
            ans.append(nums[:])
            return

        for j in range(i, len(nums)):
            # Swap the elements at indices i and j to generate different permutations.
            nums[i], nums[j] = nums[j], nums[i]
            # Recur with the updated list to explore other permutations.
            self.__optimal(i + 1, nums, ans)
            # Backtrack: restore the original order of elements for the next permutation.
            nums[i], nums[j] = nums[j], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        n: int = len(nums)
        result: List[List[int]] = []

        # mp: List[bool] = [False] * n
        # self.__f(nums, n, [], mp, result)
        self.__optimal(0, nums, result)

        return result


if __name__ == "__main__":
    nums: List[int] = [1, 2, 3]
    solution: Solution = Solution()
    result: List[List[int]] = solution.permute(nums=nums)
    print(result)
