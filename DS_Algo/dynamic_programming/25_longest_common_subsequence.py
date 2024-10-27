"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without
changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

from typing import List


class Solution:
    # Recursive approach with memoization to find the LCS length
    def __lcs(self, i: int, j: int, s1: str, s2: str, dp: List[List[int]]) -> int:
        # Base case: If either string is empty, LCS length is 0
        if i == 0 or j == 0:
            return 0

        # Return the cached result if it exists
        if dp[i][j] != -1:
            return dp[i][j]

        # If the characters match, include this character in LCS and move diagonally in the matrix
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = 1 + self.__lcs(i - 1, j - 1, s1, s2, dp)
            return dp[i][j]

        # If the characters do not match, find the maximum LCS by either excluding the current character of s1 or s2
        dp[i][j] = max(
            self.__lcs(i - 1, j, s1, s2, dp), self.__lcs(i, j - 1, s1, s2, dp)
        )
        return dp[i][j]

    # Tabulation approach to find the LCS length
    def __lcs_tabulation(self, s1: str, s2: str, n: int, m: int) -> int:
        # Create a DP table initialized to 0
        dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the DP table based on LCS rules
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If characters match, take the diagonal value and add 1
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # If characters don't match, take the maximum from left or above
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The bottom-right cell contains the length of the LCS
        return dp[n][m]

    # Optimized space approach to find the LCS length
    def __lcs_optimal(self, s1: str, s2: str, n: int, m: int) -> int:
        # Use two arrays to save space: one for the previous row and one for the current row
        prev: List[int] = [0 for _ in range(m + 1)]
        cur: List[int] = [0 for _ in range(m + 1)]

        # Fill the arrays based on LCS rules
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If characters match, use the value from the previous row and column
                if s1[i - 1] == s2[j - 1]:
                    cur[j] = 1 + prev[j - 1]
                else:
                    # If characters don't match, take the maximum from the previous row or the current column
                    cur[j] = max(prev[j], cur[j - 1])

            # Move to the next row, making current as previous
            prev = cur

        # The last value in prev array contains the length of the LCS
        return prev[m]

    # Main function to determine the length of the longest common subsequence
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n: int = len(text1)  # Length of first string
        m: int = len(text2)  # Length of second string
        # Uncomment one of the following lines to use different approaches
        # dp: List[List[int]] = [[-1] * (m + 1) for _ in range(n + 1)]
        # return self.__lcs(n, m, text1, text2, dp)  # Recursive approach with memoization
        # return self.__lcs_tabulation(text1, text2, n, m)  # Tabulation approach
        return self.__lcs_optimal(text1, text2, n, m)  # Optimized space approach


if __name__ == "__main__":
    s1: str = "adcbc"
    s2: str = "dcadb"
    solution: Solution = Solution()
    print(
        solution.longestCommonSubsequence(s1, s2)
    )  # Output the length of the longest common subsequence
