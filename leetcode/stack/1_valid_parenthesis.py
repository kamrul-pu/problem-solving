"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

from typing import Dict, List


class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of open brackets
        st: List[chr] = []

        # Dictionary to map closing brackets to their corresponding opening brackets
        parenthesis: Dict[chr] = {")": "(", "}": "{", "]": "["}

        # Iterate over each character in the input string 's'
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                # If the character is an open bracket, push it onto the stack
                st.append(ch)
            else:
                # If the character is a closing bracket
                if not st:
                    # If the stack is empty and we encounter a closing bracket, it's invalid
                    return False

                # Pop the top element from the stack
                top: chr = st.pop()

                # Check if the popped open bracket matches the corresponding bracket for 'ch'
                if top != parenthesis[ch]:
                    # If the popped bracket does not match the expected opening bracket for 'ch', it's invalid
                    return False

        # After iterating through all characters, ensure the stack is empty
        # If there are unmatched open brackets left in the stack, it's invalid
        return len(st) == 0


if __name__ == "__main__":
    s: str = "()[]{}"
    solution: Solution = Solution()
    print(solution.isValid(s=s))
