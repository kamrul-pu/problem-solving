"""Find unique paths in grid."""


def find_unique_paths(i: int, j: int, dp: list[list[int]]) -> int:
    """
    Recursive function to find unique paths from (0, 0) to (i, j) in a grid.

    Args:
        i (int): Row index.
        j (int): Column index.
        dp (list[list[int]]): Memoization table to store computed results.

    Returns:
        int: Number of unique paths.
    """
    if i == 0 and j == 0:
        return 1
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    up: int = find_unique_paths(i=i - 1, j=j, dp=dp)
    left: int = find_unique_paths(i=i, j=j - 1, dp=dp)

    dp[i][j] = up + left
    return dp[i][j]


def find_path_tabulation(n: int, m: int) -> int:
    """
    Tabulation method to find unique paths from (0, 0) to (n-1, m-1) in a grid.

    Args:
        n (int): Number of rows.
        m (int): Number of columns.

    Returns:
        int: Number of unique paths.
    """
    dp: list[list[int]] = [[-1 for _ in range(m)] for row in range(n)]
    dp[0][0] = 1
    for row in range(n):
        for col in range(m):
            if row == 0 and col == 0:
                dp[row][col] = 1
            else:
                up: int = dp[row - 1][col] if row > 0 else 0
                left: int = dp[row][col - 1] if col > 0 else 0
                dp[row][col] = up + left

    return dp[n - 1][m - 1]


def find_path_optimal(n: int, m: int) -> int:
    """
    Optimal space method to find unique paths from (0, 0) to (n-1, m-1) in a grid.

    Args:
        n (int): Number of rows.
        m (int): Number of columns.

    Returns:
        int: Number of unique paths.
    """
    prev: list[int] = [0] * m
    for i in range(n):
        temp: list[int] = [0] * m
        for j in range(m):
            if i == 0 and j == 0:
                temp[j] = 1
            else:
                up: int = prev[j] if i > 0 else 0
                left: int = temp[j - 1] if j > 0 else 0
                temp[j] = up + left

        prev = temp

    return prev[m - 1]


if __name__ == "__main__":
    n: int = 3
    m: int = 4
    dp: list[list[int]] = [[-1 for _ in range(m)] for row in range(n)]
    print(dp)
    paths: int = find_unique_paths(i=n - 1, j=m - 1, dp=dp)
    print(paths)
    print(find_path_tabulation(n=n, m=m))
    print(find_path_optimal(n=n, m=m))
