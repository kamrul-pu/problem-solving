"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combination
of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.
 """

from typing import List


class Solution:
    def __f(
        self,
        i: int,
        candidates: List[int],
        subset: List[int],
        subsets: List[List[int]],
        n: int,
        s: int,
        target: int,
    ) -> None:
        """
        Recursive function to find all combinations of candidates that sum up to the target.

        Args:
            i (int): Current index in the candidates list.
            candidates (List[int]): List of candidate integers.
            subset (List[int]): Current subset of candidates being considered.
            subsets (List[List[int]]): List to store all valid subsets.
            n (int): Length of the candidates list.
            s (int): Current sum of elements in the subset.
            target (int): Target sum to achieve.

        Returns:
            None: This function operates by side effect and populates 'subsets' list with valid combinations.
        """
        # Base case: if we have reached the end of the candidates list
        if i == n:
            # Check if the current subset sums up to the target
            if s == target:
                # If it does, add this subset to the list of valid subsets
                subsets.append(subset.copy())
            return

        # If the current sum exceeds the target, stop recursion for this branch
        if s > target:
            return

        # Include the current number and recurse
        subset.append(candidates[i])
        self.__f(i, candidates, subset, subsets, n, s + candidates[i], target)
        subset.pop()

        # Move to the next number
        self.__f(i + 1, candidates, subset, subsets, n, s, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of candidates that sum up to the target.

        Args:
            candidates (List[int]): List of candidate integers.
            target (int): Target sum to achieve.

        Returns:
            List[List[int]]: List of all unique combinations of candidates that sum up to the target.
        """
        # Determine the length of the candidates list
        n: int = len(candidates)
        # Initialize list to store all valid subsets
        subsets: List[List[int]] = []
        # Start recursive function from the beginning of the candidates list
        self.__f(0, candidates, [], subsets, n, 0, target)
        return subsets


if __name__ == "__main__":
    candidates: List[int] = [2, 3, 6, 7]
    candidates = [2, 3, 5]
    target: int = 8
    solution: Solution = Solution()
    print(solution.combinationSum(candidates=candidates, target=target))
