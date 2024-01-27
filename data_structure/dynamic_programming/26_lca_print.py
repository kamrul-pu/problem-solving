"""Print Longest Common Subsequence Dynamic programming solution."""


def get_lcs(s1: str, s2: str) -> str:
    """
    Function to find the length of the Longest Common Subsequence (LCS)
    using the tabulation (bottom-up) dynamic programming approach.

    Args:
        s1 (str): First input string.
        s2 (str): Second input string.

    Returns:
        str: LCS  the strings.
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

    ans: str = ""
    i: int = n
    j: int = m
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            ans += s1[i - 1]
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ans[::-1]


if __name__ == "__main__":
    s1: str = "abcde"
    s2: str = "bdgek"
    print(get_lcs(s1, s2))
