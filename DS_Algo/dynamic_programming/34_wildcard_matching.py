"""
Given two strings pattern and str which may be of different size, You have to return 1 if the wildcard pattern i.e.
pattern, matches with str else return 0. All characters of the string str and pattern always belong to the Alphanumeric characters.

The wildcard pattern can include the characters ? and *
‘?’ – matches any single character.
‘*’ – Matches any sequence of characters (including the empty sequence).

Note: The matching should cover the entire str (not partial str).
"""


class Solution:
    def __f(self, i: int, j: int, p: str, s: str, dp: list[list[int]]) -> bool:
        # If both indices are at the start, we have a match (empty pattern and string).
        if i == 0 and j == 0:
            return True

        # If pattern is empty and string is not, no match can occur.
        if i == 0 and j > 0:
            return False

        # If string is empty but pattern is not, we need to check if the remaining pattern can match empty string.
        if j == 0 and i > 0:
            for k in range(1, i + 1):
                if p[k - 1] != "*":
                    return False
            return True

        # Return memoized result if it exists.
        if dp[i][j] != -1:
            return dp[i][j]

        # Check for character match or '?' wildcard.
        if p[i - 1] == s[j - 1] or p[i - 1] == "?":
            dp[i][j] = self.__f(i - 1, j - 1, p, s, dp)
            return dp[i][j]

        # Handle '*' wildcard which can match zero or more characters.
        if p[i - 1] == "*":
            dp[i][j] = self.__f(i - 1, j, p, s, dp) or self.__f(i, j - 1, p, s, dp)
            return dp[i][j]

        # If no conditions are met, return False.
        dp[i][j] = False
        return False

    def __tabulation(self, p: str, s: str, n: int, m: int) -> bool:
        # Create a DP table initialized to False.
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # Base case: empty pattern and empty string match.
        dp[0][0] = True

        # Handle patterns that can match an empty string.
        for i in range(1, n + 1):
            flag = True
            for k in range(1, i + 1):
                if p[k - 1] != "*":
                    flag = False
                    break
            dp[i][
                0
            ] = flag  # All characters in pattern must be '*' to match empty string.

        # Fill the DP table.
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Check for character match or '?' wildcard.
                if p[i - 1] == s[j - 1] or p[i - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                # Handle '*' wildcard.
                elif p[i - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False

        # The answer will be in the bottom-right cell of the DP table.
        return dp[n][m]

    def __optimized(self, p: str, s: str, n: int, m: int) -> bool:
        # Initialize two arrays for dynamic programming
        dp = [False] * (m + 1)
        cur = [False] * (m + 1)

        # Base case: empty pattern matches empty string
        dp[0] = True

        for i in range(1, n + 1):
            # Check if the current pattern can match an empty string
            flag = True
            for k in range(1, i + 1):
                if p[k - 1] != "*":
                    flag = False
                    break
            cur[0] = (
                flag  # Set cur[0] based on whether the pattern matches an empty string
            )

            # Fill the current row of the DP array
            for j in range(1, m + 1):
                # Check for character match or '?' wildcard
                if p[i - 1] == s[j - 1] or p[i - 1] == "?":
                    cur[j] = dp[j - 1]
                # Handle '*' wildcard, which can match zero or more characters
                elif p[i - 1] == "*":
                    cur[j] = dp[j] or cur[j - 1]
                else:
                    cur[j] = False

            # Copy the current results to dp for the next iteration
            dp = cur[:]

        # The final result will be in dp[m], indicating if the pattern matches the string
        return dp[m]

    def wildCard(self, pattern: str, string: str) -> bool:
        """
        Main function to match the string against the pattern using wildcard rules.

        Parameters:
        - pattern: The pattern string containing wildcards.
        - string: The input string to match against the pattern.

        Returns:
        - True if the pattern matches the string, False otherwise.
        """
        n = len(pattern)
        m = len(string)
        # Using the tabulation approach for the solution.
        # return self.__tabulation(pattern, string, n, m)
        return self.__optimized(pattern, string, n, m)


if __name__ == "__main__":
    s: str = "aa"
    p: str = "*b"
    solution: Solution = Solution()
    print(solution.wildCard(p, s))
