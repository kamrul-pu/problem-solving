"""
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
"""

from typing import Dict, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # List to store the resulting combinations
        ans: List[str] = []

        # Mapping of digits to corresponding letters
        digit_to_chars: Dict[int, str] = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        # Backtracking function to generate combinations
        def backtrack(i, cur_str):
            # Base case: If the current combination has the same length as the input digits, add to the result list
            if len(cur_str) == len(digits):
                ans.append(cur_str)
                return

            # Iterate over the characters corresponding to the current digit
            for c in digit_to_chars[int(digits[i])]:
                # Recursively call backtrack to build the combination
                backtrack(i + 1, cur_str + c)

        # Start backtracking from the first digit
        if digits:
            backtrack(0, "")

        return ans


if __name__ == "__main__":
    digits: str = "23"
    solution: Solution = Solution()
    result: List[str] = solution.letterCombinations(digits=digits)
    print(result)
