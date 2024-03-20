"""Minimum path sum in grid."""

INT_MAX: int = float("inf")


def min_path_sum(i: int, j: int, grid: list[list[int]], dp: list[list[int]]) -> int:
    if i == 0 and j == 0:
        return grid[i][j]
    if i < 0 or j < 0:
        return INT_MAX
    if dp[i][j] != -1:
        return dp[i][j]
    up: int = grid[i][j] + min_path_sum(i=i - 1, j=j, grid=grid, dp=dp)
    left: int = grid[i][j] + min_path_sum(i=i, j=j - 1, grid=grid, dp=dp)
    dp[i][j] = min(up, left)

    return dp[i][j]


def min_path_sum_tabulation(n: int, m: int, grid: list[list[int]]) -> int:
    dp: list[list[int]] = [[0 for _ in range(m)] for row in range(n)]
    dp[0][0] = grid[0][0]
    for r in range(n):
        for c in range(m):
            if r == 0 and c == 0:
                dp[r][c] = grid[r][c]
            else:
                up: int = grid[r][c] + (dp[r - 1][c] if r > 0 else INT_MAX)
                left: int = grid[r][c] + (dp[r][c - 1] if c > 0 else INT_MAX)
                dp[r][c] = min(up, left)

    return dp[n - 1][m - 1]


def min_path_sum_optimal(n: int, m: int, grid: list[list[int]]) -> int:
    temp: list[int] = [0] * m
    for r in range(n):
        cur: list[int] = [0] * m
        for c in range(m):
            if r == 0 and c == 0:
                cur[c] = grid[r][c]
            else:
                up: int = grid[r][c] + (temp[c] if r > 0 else INT_MAX)
                left: int = grid[r][c] + (cur[c - 1] if c > 0 else INT_MAX)
                cur[c] = min(up, left)
        temp = cur

    return temp[m - 1]


if __name__ == "__main__":
    grid: list[list[int]] = [
        [5, 9, 6],
        [11, 5, 2],
    ]
    n: int = len(grid)
    m: int = len(grid[0])
    dp: list[list[int]] = [[-1 for _ in range(m)] for row in range(n)]
    min_path: int = min_path_sum(i=n - 1, j=m - 1, grid=grid, dp=dp)
    print(min_path)
    print(min_path_sum_tabulation(n=n, m=m, grid=grid))
    print(min_path_sum_optimal(n=n, m=m, grid=grid))
