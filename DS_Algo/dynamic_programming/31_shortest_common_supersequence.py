"""
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.
If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.
"""

from typing import List


class Solution:
    def __f(self, s1: str, s2: str) -> str:
        # Initialize the lengths of the two strings
        n = len(s1)  # Length of the first string
        m = len(s2)  # Length of the second string

        # Create a DP table initialized to 0
        # dp[i][j] will hold the length of the longest common subsequence (LCS)
        dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the DP table based on LCS (Longest Common Subsequence) rules
        for i in range(1, n + 1):  # Iterate through each character of s1
            for j in range(1, m + 1):  # Iterate through each character of s2
                # If the characters match, extend the length of LCS by 1
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]  # Increment from the diagonal
                else:
                    # If characters don't match, take the maximum from left or above
                    dp[i][j] = max(
                        dp[i - 1][j], dp[i][j - 1]
                    )  # Choose the longer subsequence

        # The bottom-right cell contains the length of the LCS
        lcs: int = dp[n][m]
        # Calculate the length of the shortest common supersequence
        scs: int = n + m - lcs  # SCS length

        # Initialize a list to construct the SCS
        ans: List[str] = [""] * scs
        scs -= 1  # Adjust index for ans array
        i: int = n  # Start from the end of s1
        j: int = m  # Start from the end of s2

        # Backtrack to construct the SCS
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                ans[scs] = s1[i - 1]  # If characters match, add to result
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                ans[scs] = s1[i - 1]  # Take character from s1
                i -= 1
            else:
                ans[scs] = s2[j - 1]  # Take character from s2
                j -= 1
            scs -= 1  # Move to the next position in the result

        # If there are remaining characters in s1, add them to the result
        while i > 0:
            ans[scs] = s1[i - 1]
            scs -= 1
            i -= 1

        # If there are remaining characters in s2, add them to the result
        while j > 0:
            ans[scs] = s2[j - 1]
            scs -= 1
            j -= 1

        # Join the list into a single string and return
        return "".join(ans)

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Call the helper function to get the SCS
        return self.__f(str1, str2)


if __name__ == "__main__":
    s1: str = "brute"  # Example first string
    s2: str = "groot"  # Example second string
    solution: Solution = Solution()  # Create an instance of the Solution class
    print(
        solution.shortestCommonSupersequence(s1, s2)
    )  # Print the SCS of the two strings
