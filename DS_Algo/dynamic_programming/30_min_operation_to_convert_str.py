"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
"""

from typing import List


class Solution:
    def __f(self, s1: str, s2: str) -> int:
        # Initialize the lengths of the two strings
        n = len(s1)  # Length of the first string
        m = len(s2)  # Length of the second string

        # Create a DP table initialized to 0
        # dp[i][j] will hold the length of the longest common subsequence
        dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the DP table based on LCS (Longest Common Subsequence) rules
        for i in range(1, n + 1):  # Iterate through each character of s1
            for j in range(1, m + 1):  # Iterate through each character of s2
                # If the characters match, we can extend the length of LCS by 1
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]  # Increment from the diagonal
                else:
                    # If the characters don't match, take the maximum from left or above
                    dp[i][j] = max(
                        dp[i - 1][j], dp[i][j - 1]
                    )  # Choose the longer subsequence

        # The bottom-right cell contains the length of the LCS
        return dp[n][m]

    def minDistance(self, word1: str, word2: str) -> int:
        # Calculate the lengths of both input strings
        n: int = len(word1)
        m: int = len(word2)

        # The minimum distance is calculated as:
        # Total length of both strings minus twice the length of their longest common subsequence
        return n + m - 2 * self.__f(word1, word2)


if __name__ == "__main__":
    s1: str = "abcd"  # Example first string
    s2: str = "anc"  # Example second string
    solution: Solution = Solution()  # Create an instance of the Solution class
    print(
        solution.minDistance(s1, s2)
    )  # Print the minimum steps needed to make the strings the same
