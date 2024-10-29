"""Longest Palindrome Subsequence solution using dynamic programming."""

from typing import List


class Solution:
    def __f(self, s1: str, s2: str) -> int:
        # Create a DP table initialized to 0
        n = m = len(s1)  # Length of the input string
        dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]  # DP table

        # Fill the DP table based on LCS rules
        for i in range(1, n + 1):  # Iterate through each character of s1
            for j in range(1, m + 1):  # Iterate through each character of s2
                # If characters match, take the diagonal value and add 1
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = (
                        1 + dp[i - 1][j - 1]
                    )  # Increment the length of the common subsequence
                else:
                    # If characters don't match, take the maximum from left or above
                    dp[i][j] = max(
                        dp[i - 1][j], dp[i][j - 1]
                    )  # Choose the longer subsequence

        # The bottom-right cell contains the length of the LCS (Longest Common Subsequence)
        return dp[n][m]

    def __optimized(self, s1: str, s2: str) -> int:
        n = m = len(s1)  # Length of the input string
        # Use two arrays to save space: one for the previous row and one for the current row
        prev: List[int] = [0 for _ in range(m + 1)]  # Previous row
        cur: List[int] = [0 for _ in range(m + 1)]  # Current row

        # Fill the arrays based on LCS rules
        for i in range(1, n + 1):  # Iterate through each character of s1
            for j in range(1, m + 1):  # Iterate through each character of s2
                # If characters match, use the value from the previous row and column
                if s1[i - 1] == s2[j - 1]:
                    cur[j] = (
                        1 + prev[j - 1]
                    )  # Increment the length of the common subsequence
                else:
                    # If characters don't match, take the maximum from the previous row or the current column
                    cur[j] = max(prev[j], cur[j - 1])  # Choose the longer subsequence

            # Move to the next row, making current as previous for the next iteration
            prev = cur.copy()  # Update prev to the current row

        # The last value in prev array contains the length of the LCS
        return prev[m]  # Return the length of the longest palindromic subsequence

    def lcs_palindrome(self, s: str) -> int:
        s2: str = s[
            ::-1
        ]  # Reverse the input string to find the longest palindromic subsequence
        # return self.__f(s, s2)  # Uncomment to use the full DP implementation
        return self.__optimized(
            s, s2
        )  # Using the optimized version for better space efficiency


if __name__ == "__main__":
    s1: str = "bbabcbcab"  # Input string to find the longest palindromic subsequence
    solution: Solution = Solution()  # Create an instance of Solution
    print(
        solution.lcs_palindrome(s1)
    )  # Output the length of the longest palindromic subsequence
