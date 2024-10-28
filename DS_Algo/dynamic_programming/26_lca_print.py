"""Print Longest Common Subsequence Dynamic programming solution."""

from typing import List


class Solution:
    def get_lcs(self, s1: str, s2: str) -> str:
        """
        Function to find the length of the Longest Common Subsequence (LCS)
        using the tabulation (bottom-up) dynamic programming approach.

        Args:
            s1 (str): First input string.
            s2 (str): Second input string.

        Returns:
            str: LCS of the two strings.
        """
        n: int = len(s1)  # Length of the first string
        m: int = len(s2)  # Length of the second string

        # Initialize a 2D array (table) to store lengths of LCS
        # dp[i][j] will hold the length of LCS of s1[0...i-1] and s2[0...j-1]
        dp: List[List[int]] = [[0 for col in range(m + 1)] for row in range(n + 1)]

        # Build the dp array in a bottom-up manner
        for i in range(1, n + 1):  # Iterate through each character of s1
            for j in range(1, m + 1):  # Iterate through each character of s2
                # Check if the current characters of both strings match
                if s1[i - 1] == s2[j - 1]:
                    # If they match, increment the length of LCS by 1
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # If they don't match, take the maximum LCS length
                    # from either excluding the current character of s1 or s2
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The dp[n][m] now contains the length of the LCS
        ans: str = ""  # This will hold the actual LCS
        i: int = n  # Start from the end of s1
        j: int = m  # Start from the end of s2

        # Backtrack to find the actual LCS string
        while i > 0 and j > 0:
            # If characters match, include this character in LCS
            if s1[i - 1] == s2[j - 1]:
                ans += s1[i - 1]  # Append matched character
                i -= 1  # Move diagonally in the dp table
                j -= 1  # Move diagonally in the dp table
            # If they do not match, move in the direction of the larger value
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1  # Move up in the dp table
            else:
                j -= 1  # Move left in the dp table

        # The LCS is constructed in reverse order, so reverse it before returning
        return ans[::-1]


if __name__ == "__main__":
    s1: str = "abcde"  # First input string
    s2: str = "bdgek"  # Second input string
    solution: Solution = Solution()
    print(solution.get_lcs(s1, s2))  # Output the LCS
