"""Wildcard matching. Recursion. 1. ?-> match single 2. * -> match 0 or more."""


class Solution:
    def __f(self, i: int, j: int, s: str, p: str, dp) -> bool:
        # Base case: both strings are empty, it's a match
        if i == 0 and j == 0:
            return True
        # If pattern is empty, but string is not, no match
        if i == 0 and j > 0:
            return False
        # If string is empty, check if the remaining pattern is all '*'
        if j == 0 and i > 0:
            for ri in range(1, i + 1):
                if p[ri - 1] != "*":
                    return False
            return True
        # If already computed, return the result from the memoization table
        if dp[i][j] != -1:
            return dp[i][j]
        # Matching characters or '?'
        if p[i - 1] == s[j - 1] or p[i - 1] == "?":
            dp[i][j] = self.__f(i - 1, j - 1, s, p, dp)
            return dp[i][j]
        # Handling '*': match 0 characters or 1 character
        if p[i - 1] == "*":
            dp[i][j] = self.__f(i - 1, j, s, p, dp) or self.__f(i, j - 1, s, p, dp)
            return dp[i][j]
        # If characters don't match, no match
        dp[i][j] = False
        return dp[i][j]

    def isMatch(self, s: str, p: str) -> bool:
        n: int = len(p)
        m: int = len(s)
        dp: list[list[int]] = [[-1 for col in range(m + 1)] for row in range(n + 1)]
        return self.__f(n, m, s, p, dp)

    def is_matched_tabulation(self, s: str, p: str) -> bool:
        n: int = len(p)
        m: int = len(s)
        dp: list[list[bool]] = [[False for col in range(m + 1)] for row in range(n + 1)]
        dp[0][0] = True
        # If pattern is empty, set the remaining string to True if all '*' in pattern
        for j in range(1, m + 1):
            dp[0][j] = False

        for i in range(1, n + 1):
            flag: bool = True
            for ri in range(1, i + 1):
                if p[ri - 1] != "*":
                    flag = False
                    break
            dp[i][0] = flag

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Matching characters or '?'
                if p[i - 1] == s[j - 1] or p[i - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                # Handling '*': match 0 characters or 1 character
                elif p[i - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                # If characters don't match, no match
                else:
                    dp[i][j] = False

        return dp[n][m]

    def is_matched_optimal(self, s: str, p: str) -> bool:
        n: int = len(p)
        m: int = len(s)
        dp: list[list[bool]] = [[False for col in range(m + 1)] for row in range(n + 1)]
        dp[0][0] = True
        prev: list[bool] = [False for col in range(m + 1)]
        cur: list[bool] = [False for col in range(m + 1)]
        prev[0] = True

        for i in range(1, n + 1):
            flag: bool = True
            for ri in range(1, i + 1):
                if p[ri - 1] != "*":
                    flag = False
                    break
            cur[0] = flag

            for j in range(1, m + 1):
                # Matching characters or '?'
                if p[i - 1] == s[j - 1] or p[i - 1] == "?":
                    cur[j] = prev[j - 1]
                # Handling '*': match 0 characters or 1 character
                elif p[i - 1] == "*":
                    cur[j] = prev[j] or cur[j - 1]
                # If characters don't match, no match
                else:
                    cur[j] = False
            prev = cur.copy()

        return prev[m]


if __name__ == "__main__":
    s: str = "aa"
    p: str = "*b"
    solution: Solution = Solution()
    print(solution.isMatch(s, p))
    print(solution.is_matched_tabulation(s, p))
    print(solution.is_matched_optimal(s, p))
