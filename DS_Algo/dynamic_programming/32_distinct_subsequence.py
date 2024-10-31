"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.
"""

from typing import List


class Solution:
    # This is a recursive approach with memoization
    def __f(self, i: int, j: int, s: str, t: str, dp: List[List[int]]) -> int:
        # Base case: if t is empty, there is one subsequence of s that equals t (the empty subsequence)
        if j == 0:
            return 1
        # If s is empty but t is not, there are no subsequences that can match t
        if i == 0:
            return 0
        # Return cached result if it exists
        if dp[i][j] != -1:
            return dp[i][j]
        # If the current characters match, we can either include or exclude the character from s
        if s[i - 1] == t[j - 1]:
            dp[i][j] = self.__f(i - 1, j - 1, s, t, dp) + self.__f(i - 1, j, s, t, dp)
        else:
            # If they don't match, we can only exclude the character from s
            dp[i][j] = self.__f(i - 1, j, s, t, dp)
        return dp[i][j]

    # This function implements a bottom-up tabulation approach
    def __tabulation(self, s: str, t: str, n: int, m: int) -> int:
        # Create a 2D list to store the number of distinct subsequences
        dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]
        # There's one way to form the empty string (t) from any prefix of s
        for i in range(n + 1):
            dp[i][0] = 1
        # Fill the dp table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If characters match, add the two possibilities
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # If they don't match, just carry forward the previous value
                    dp[i][j] = dp[i - 1][j]
        return dp[n][m]  # Result is in the bottom-right corner of the table

    # This is an optimized version using a 1D array
    def __optimized(self, s: str, t: str, n: int, m: int) -> int:
        # Use a single array to store the current counts
        dp: List[int] = [0] * (m + 1)
        dp[0] = 1  # One way to form the empty string
        # Iterate through the characters of s
        for i in range(1, n + 1):
            # Iterate backwards through the characters of t
            for j in range(m, 0, -1):
                if s[i - 1] == t[j - 1]:
                    # Update the current count based on previous counts
                    dp[j] = dp[j - 1] + dp[j]
        return dp[m]  # The result is in the last position

    # Main function to determine the number of distinct subsequences
    def numDistinct(self, s: str, t: str) -> int:
        n: int = len(s)
        m: int = len(t)
        # Uncomment one of the following lines to use a specific approach:
        # dp: List[List[int]] = [[-1] * (m + 1) for _ in range(n + 1)]
        # return self.__f(n, m, s, t, dp)
        # return self.__tabulation(s, t, n, m)
        return self.__optimized(s, t, n, m)


if __name__ == "__main__":
    s1: str = "babgbag"
    s2: str = "bag"
    solution: Solution = Solution()
    print(solution.numDistinct(s1, s2))  # Output: 5
