"""
Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without
disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.
"""

from typing import List, Set


class Solution:
    def __f(self, i: int, s: str, t: str, st: Set) -> int:
        if i < 0:
            st.add(t)
            return
        self.__f(i - 1, s, t, st)
        t += s[i]
        self.__f(i - 1, s, t, st)

    def __tabulation(self, s: str) -> int:
        # Length of the input string
        n = len(s)

        # DP array to count distinct subsequences ending with each character
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: the empty subsequence

        # Dictionary to remember the last occurrence of each character
        last = {}

        for i in range(1, n + 1):
            current_char = s[i - 1]
            # Total distinct subsequences is double the previous total
            dp[i] = (2 * dp[i - 1]) % (10**9 + 7)

            # If the character has appeared before, subtract the count of subsequences
            # that end before the last occurrence of the current character
            if current_char in last:
                dp[i] = (dp[i] - dp[last[current_char] - 1]) % (10**9 + 7)

            # Update the last occurrence of the current character
            last[current_char] = i

        # Subtract 1 to exclude the empty subsequence
        return (dp[n] - 1) % (10**9 + 7)

    def distinctSubseqII(self, s: str) -> int:
        # n: int = len(s)
        # st: Set[str] = set()
        # self.__f(n - 1, s, "", st)
        # return len(st) - 1
        return self.__tabulation(s)


if __name__ == "__main__":
    s: str = "abc"
    solution: Solution = Solution()
    print(solution.distinctSubseqII(s))
