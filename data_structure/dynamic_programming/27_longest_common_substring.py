"""Longest common substring problem using dynamic programming."""


def lcs(s1: str, s2: str) -> int:
    """
    Function to find the length of the Longest Common Substring (LCS)
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
    ans: int = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the current characters match, increment the LCS length with previous character result.
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                ans = max(ans, dp[i][j])

    return ans


def lcs_optimal(s1: str, s2: str) -> int:
    """
    Function to find the length of the Longest Common Substring (LCS)
    using the tabulation (bottom-up) dynamic programming approach.

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
    ans: int = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the current characters match, increment the LCS length with previous character result.
            if s1[i - 1] == s2[j - 1]:
                cur[j] = 1 + prev[j - 1]
                ans = max(ans, cur[j])
        prev = cur

    return ans


if __name__ == "__main__":
    s1: str = "abcd"
    s2: str = "abzd"
    print(lcs(s1, s2))
    print(lcs_optimal(s1, s2))
