"""
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.
"""

from typing import List


class Solution:
    def __f(self, s1: str, s2: str) -> int:
        # Initialize the lengths of the two strings
        n = len(s1)  # Length of the first string
        m = len(s2)  # Length of the second string (which is the reverse of s1)

        # Create a DP table initialized to 0
        # dp[i][j] will hold the length of the longest common subsequence
        dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the DP table based on LCS (Longest Common Subsequence) rules
        for i in range(1, n + 1):  # Iterate through each character of s1
            for j in range(1, m + 1):  # Iterate through each character of s2
                # If the characters match, we can extend the length of LCS by 1
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = (
                        1 + dp[i - 1][j - 1]
                    )  # Increment the count from the diagonal
                else:
                    # If the characters don't match, take the maximum from left or above
                    dp[i][j] = max(
                        dp[i - 1][j], dp[i][j - 1]
                    )  # Choose the longer subsequence

        # The bottom-right cell contains the length of the LCS
        return dp[n][m]

    def minInsertions(self, s: str) -> int:
        n: int = len(s)  # Get the length of the input string
        t: str = s[::-1]  # Reverse the string to compare with the original
        # The minimum insertions required to make s a palindrome is the difference
        # between the length of s and the length of its longest palindromic subsequence
        return n - self.__f(s, t)  # Call the helper function to find LCS length


if __name__ == "__main__":
    s: str = "abcaa"  # Example input string
    solution: Solution = Solution()  # Create an instance of Solution
    print(solution.minInsertions(s))  # Print the minimum insertions needed
