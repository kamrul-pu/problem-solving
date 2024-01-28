"""Distinct subsequences 1D Array Optimization."""


def f(i: int, j: int, s1: str, s2: str, dp: list[list[int]]) -> int:
    """Recursive function to compute the number of distinct subsequences."""
    if j == 0:
        return 1
    if i == 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s1[i - 1] == s2[j - 1]:
        dp[i][j] = f(i - 1, j - 1, s1, s2, dp) + f(i - 1, j, s1, s2, dp)
        return dp[i][j]

    dp[i][j] = f(i - 1, j, s1, s2, dp)
    return dp[i][j]


def distinct_subsequence(s1: str, s2: str) -> int:
    """Wrapper function for the recursive approach."""
    n: int = len(s1)
    m: int = len(s2)
    dp: list[list[int]] = [[-1 for col in range(m + 1)] for row in range(n + 1)]
    return f(i=n, j=m, s1=s1, s2=s2, dp=dp)


def distinct_subsequence_tabulation(s: str, t: str) -> int:
    """Tabulation approach to compute the number of distinct subsequences."""
    n: int = len(s)
    m: int = len(t)
    dp: list[list[int]] = [[0 for col in range(m + 1)] for row in range(n + 1)]

    # Base case: if the second string is empty, there is always one subsequence (empty string).
    for i in range(n + 1):
        dp[i][0] = 1

    # Build the table using dynamic programming.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]


def distinct_subsequence_optimal(s: str, t: str) -> int:
    """Optimized space complexity approach to compute the number of distinct subsequences."""
    n: int = len(s)
    m: int = len(t)
    prev: list[int] = [0 for col in range(m + 1)]
    cur: list[int] = [0 for col in range(m + 1)]
    prev[0] = 1
    cur[0] = 1

    # Build the array using dynamic programming with optimal space complexity.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                cur[j] = prev[j - 1] + prev[j]
            else:
                cur[j] = prev[j]

        prev = cur.copy()

    return prev[m]


if __name__ == "__main__":
    s1: str = "babgbag"
    s2: str = "bag"
    n = len(s1)
    print(distinct_subsequence(s1=s1, s2=s2))
    print(distinct_subsequence_tabulation(s1, s2))
    print(distinct_subsequence_optimal(s1, s2))
