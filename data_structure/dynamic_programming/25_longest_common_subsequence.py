"""Longest Common Subsequence Dynamic programming solution."""


def f(i: int, j: int, s1: str, s2: str, dp: list[list[int]]) -> int:
    """
    Helper function for the recursive solution to find the length of the
    Longest Common Subsequence (LCS) using dynamic programming.

    Args:
        i1 (int): Current index in the first string.
        j (int): Current index in the second string.
        s1 (str): First input string.
        s2 (str): Second input string.
        dp (list[list[int]]): Memoization table to store already computed results.

    Returns:
        int: Length of LCS for the current pair of substrings.
    """
    # Base case: If either of the strings is empty, LCS is 0.
    if i == 0 or j == 0:
        return 0

    # If the result is already computed, return it from the memoization table.
    if dp[i][j] != -1:
        return dp[i][j]

    # If the current characters match, increment the LCS length.
    if s1[i - 1] == s2[j - 1]:
        dp[i][j] = 1 + f(i - 1, j - 1, s1, s2, dp)
        return dp[i][j]

    # If the current characters don't match, choose the maximum LCS from
    # excluding one character from either of the strings.
    dp[i][j] = max(f(i - 1, j, s1, s2, dp), f(i, j - 1, s1, s2, dp))
    return dp[i][j]


def lcs(s1: str, s2: str) -> int:
    """
    Top-level function to find the length of the Longest Common Subsequence (LCS)
    using the recursive solution with memoization.

    Args:
        s1 (str): First input string.
        s2 (str): Second input string.

    Returns:
        int: Length of LCS for the input strings.
    """
    n1: int = len(s1)
    n2: int = len(s2)
    dp: list[list[int]] = [[-1 for col in range(n2 + 1)] for row in range(n1 + 1)]
    return f(n1, n2, s1, s2, dp)


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
        prev = cur

    return prev[m]


if __name__ == "__main__":
    s1: str = "adcbc"
    s2: str = "dcadb"
    print(lcs(s1=s1, s2=s2))
    print(lcs_tabulation(s1, s2))
    print(lcs_optimal(s1, s2))
