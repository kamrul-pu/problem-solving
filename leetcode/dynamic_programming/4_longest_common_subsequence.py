"""Longest common subsequence of two strings"""

from typing import List


class Solution:
    def __lcs(self, i: int, j: int, s1: str, s2: str, dp: List[List[int]]) -> int:
        """
        Recursive helper function to find the length of the longest common subsequence.

        Args:
            i (int): Current index in string s1.
            j (int): Current index in string s2.
            s1 (str): First string.
            s2 (str): Second string.
            dp (List[List[int]]): Memoization table to store computed values.

        Returns:
            int: Length of the longest common subsequence.
        """
        if i == 0 or j == 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = 1 + self.__lcs(i - 1, j - 1, s1, s2, dp)
            return dp[i][j]
        dp[i][j] = max(
            self.__lcs(i - 1, j, s1, s2, dp), self.__lcs(i, j - 1, s1, s2, dp)
        )
        return dp[i][j]

    def __lcs_tabulation(self, s1: str, s2: str, n: int, m: int) -> int:
        """
        Tabulation approach to find the length of the longest common subsequence.

        Args:
            s1 (str): First string.
            s2 (str): Second string.
            n (int): Length of s1.
            m (int): Length of s2.

        Returns:
            int: Length of the longest common subsequence.
        """
        dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]

    def __lcs_optimal(self, s1: str, s2: str, n: int, m: int) -> int:
        """
        Optimal space complexity approach to find the length of the longest common subsequence.

        Args:
            s1 (str): First string.
            s2 (str): Second string.
            n (int): Length of s1.
            m (int): Length of s2.

        Returns:
            int: Length of the longest common subsequence.
        """
        prev: List[int] = [0 for _ in range(m + 1)]
        cur: List[int] = [0 for _ in range(m + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    cur[j] = 1 + prev[j - 1]
                else:
                    cur[j] = max(prev[j], cur[j - 1])

            prev = cur
        return prev[m]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Function to find the length of the longest common subsequence of two strings.

        Args:
            text1 (str): The first input string.
            text2 (str): The second input string.

        Returns:
            int: Length of the longest common subsequence.
        """
        n: int = len(text1)
        m: int = len(text2)
        # dp: List[List[int]] = [[-1] * (m + 1) for _ in range(n + 1)]
        # return self.__lcs(n, m, text1, text2, dp)
        # return self.__lcs_tabulation(text1, text2, n, m)
        return self.__lcs_optimal(text1, text2, n, m)


if __name__ == "__main__":
    text1: str = "abcde"
    text2: str = "ace"
    solution: Solution = Solution()
    print(solution.longestCommonSubsequence(text1=text1, text2=text2))
