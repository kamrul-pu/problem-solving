"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize an empty list to track the current combination of parentheses
        stack: List[str] = []

        # Initialize an empty list to store the valid combinations of parentheses
        res: List[str] = []

        # Define a recursive backtrack function to generate valid combinations
        def backtrack(open_p, close_p):
            # Base case: If the number of open and close parentheses reaches `n`
            if open_p == close_p == n:
                # Convert the current stack (combination) to a string and add to results
                res.append("".join(stack))
                return

            # Recursive cases:
            # Add an open parenthesis '(' if the count of open parentheses is less than `n`
            if open_p < n:
                stack.append("(")
                backtrack(open_p + 1, close_p)
                stack.pop()  # Backtrack: Remove the last added '('

            # Add a close parenthesis ')' if the count of close parentheses is less than the count of open parentheses
            if close_p < open_p:
                stack.append(")")
                backtrack(open_p, close_p + 1)
                stack.pop()  # Backtrack: Remove the last added ')'

        # Start the recursive function with initial counts of open and close parentheses as 0
        backtrack(0, 0)

        # Return the list of valid combinations of parentheses
        return res


if __name__ == "__main__":
    n: int = 3
    solution: Solution = Solution()
    print(solution.generateParenthesis(n=n))
