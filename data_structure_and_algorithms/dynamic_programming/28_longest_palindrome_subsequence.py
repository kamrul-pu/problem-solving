"""Longest Palindrome Subsequence solution using dynamic programming."""


def lcs_tabulation(s1: str, s2: str) -> int:
    """
    Function to find the length of the Longest Common Subsequence (LCS)
    using the tabulation (bottom-up) dynamic programming approach.

    Args:
        s1 (str): First input string.
        s2 (str): Second input string.

    Returns:
        int: Length of LCS for the input strings.
    """
    n: int = len(s1)
    m: int = len(s2)
    dp: list[list[int]] = [[0 for col in range(m + 1)] for row in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the current characters match, increment the LCS length.
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # If the current characters don't match, choose the maximum LCS
                # from excluding one character from either of the strings.
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


def lcs_optimal(s1: str, s2: str) -> int:
    """
    Function to find the length of the Longest Common Subsequence (LCS)
    using an optimized space (rolling array) dynamic programming approach.

    Args:
        s1 (str): First input string.
        s2 (str): Second input string.

    Returns:
        int: Length of LCS for the input strings.
    """
    n: int = len(s1)
    m: int = len(s2)
    prev: list[int] = [0 for col in range(m + 1)]
    cur: list[int] = [0 for col in range(m + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the current characters match, increment the LCS length.
            if s1[i - 1] == s2[j - 1]:
                cur[j] = 1 + prev[j - 1]
            else:
                # If the current characters don't match, choose the maximum LCS
                # from excluding one character from either of the strings.
                cur[j] = max(prev[j], cur[j - 1])

        # Update the previous array for the next iteration.
        prev = cur.copy()

    return prev[m]


if __name__ == "__main__":
    s1: str = "bbabcbcab"
    s2: str = s1[::-1]

    print(lcs_tabulation(s1, s2))
    print(lcs_optimal(s1, s2))
