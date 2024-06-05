"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse
of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
"""

from typing import Dict, List


class Solution:
    def __f(self, i: int, n: int, dp: Dict[int, int]) -> int:
        # If the result for the current index 'i' is already computed, return it from the memoization dictionary.
        if i in dp:
            return dp[i]

        # If the current digit is '0', it cannot be mapped to any letter, so return 0.
        if s[i] == "0":
            return 0

        # Initialize the result to the number of ways to decode the substring starting from the next index.
        res: int = self.__f(i + 1, n, dp)

        # If the current digit and the next digit form a valid mapping (between 1 and 26),
        # recursively compute the number of ways to decode the substring starting from the index after the next.
        if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
            res += self.__f(i + 2, n, dp)

        # Memoize the result for the current index 'i' and return it.
        dp[i] = res
        return dp[i]

    def __tabulation(self, s: str) -> int:
        n = len(s)
        # Create a table to store the number of ways to decode the substring ending at each position.
        dp = [0] * (n + 1)
        # There's one way to decode an empty string.
        dp[n] = 1

        # Iterate through the string from right to left.
        for i in range(n - 1, -1, -1):
            # If the current digit is '0', it cannot be mapped to any letter, so skip it.
            if s[i] == "0":
                continue

            # Compute the number of ways to decode the substring ending at the current position.
            dp[i] = dp[i + 1]
            # If the current digit and the next digit form a valid mapping, add the number of ways to decode
            # the substring starting from the position after the next.
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]

        # Return the number of ways to decode the entire string.
        return dp[0]

    def numDecodings(self, s: str) -> int:
        # n: int = len(s)

        # # Initialize a memoization dictionary to store computed results for dynamic programming.
        # dp: Dict[int, int] = dict()

        # # Initialize the result for the last index (one way to decode an empty string).
        # dp[n] = 1

        # # Call the recursive function to compute the number of ways to decode the entire string.
        # return self.__f(0, n, dp)
        return self.__tabulation(s=s)


# Test the solution
if __name__ == "__main__":
    s: str = "226"
    solution: Solution = Solution()
    print(solution.numDecodings(s=s))
