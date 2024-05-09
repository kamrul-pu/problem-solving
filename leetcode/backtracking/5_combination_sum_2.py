"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n: int = len(candidates)
        ans: List[List[int]] = []  # List to store valid combinations

        def backtrack(cur: List[int], i: int, target: int):
            # Step 3: Base case - If the target sum is achieved
            if target == 0:
                ans.append(cur[:])

            # Step 5: Skip candidates that exceed the remaining target
            if target <= 0:
                return

            for j in range(i, n):
                # Avoid duplicates within the same level of recursion
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                # Include the current candidate in the combination
                cur.append(candidates[j])

                # Recursively explore combinations with the current candidate
                # and update the remaining target
                backtrack(cur, j + 1, target - candidates[j])

                # Backtrack - Remove the last added candidate to explore other combinations
                cur.pop()

        # Step 2: Initiate backtracking from the start index (0) with an empty current list and target
        backtrack([], 0, target)

        # Step 6: Return the list of all valid combinations
        return ans


if __name__ == "__main__":
    candidates: List[int] = [10, 1, 2, 7, 6, 1, 5]
    target: int = 8
    solution: Solution = Solution()
    result: List[List[int]] = solution.combinationSum2(
        candidates=candidates, target=target
    )
    print(result)
