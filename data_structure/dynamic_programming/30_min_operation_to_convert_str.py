"""Minimum Insertion/Deletions to convert string A to String B. """


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


def min_insertion_deletion(s1: str, s2: str) -> int:
    n: int = len(s1)
    m: int = len(s2)
    lcs_len: int = lcs(s1, s2)
    return n + m - 2 * lcs_len


if __name__ == "__main__":
    s1: str = "abcd"
    s2: str = "anc"
    print(min_insertion_deletion(s1, s2))
