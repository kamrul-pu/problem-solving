"""Shortest common Supersequence problem."""


def lcs(s1: str, s2: str) -> int:
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


def shortest_common_super_seq(s1: str, s2: str) -> int:
    # get the length of string 1 and 2
    n: int = len(s1)
    m: int = len(s2)
    # calculate length of lcs
    lcs_len: int = lcs(s1, s2)
    # result will be total length - lcs (common subsequence length.)
    return (n + m) - lcs_len


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
        # take the string and go diagonal.
        if s1[i - 1] == s2[j - 1]:
            ans += s1[i - 1]
            i -= 1
            j -= 1
        # go top so take left string
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
            ans += s1[i]
        # go left take the top string
        else:
            j -= 1
            ans += s2[j]
    while i > 0:
        ans += s1[i - 1]
        i -= 1
    while j > 0:
        ans += s2[j - 1]
        j -= 1

    return ans[::-1]


if __name__ == "__main__":
    s1: str = "brute"
    s2: str = "groot"
    # s1 = "bleed"
    # s2 = "blue"
    print(shortest_common_super_seq(s1, s2))
    print(get_lcs(s1, s2))
