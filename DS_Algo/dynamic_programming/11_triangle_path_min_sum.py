"""Minimum Path Sum in a Triangle"""


def min_path_sum(
    i: int, j: int, n: int, m: int, triangle: list[list[int]], dp=list[list[int]]
) -> int:
    """Recursive approach with memoization"""
    # Base case: reach the bottom of the triangle
    if i == n - 1:
        return triangle[i][j]
    # Check if the result for the current position is already calculated
    if dp[i][j] != -1:
        return dp[i][j]
    # Calculate the sum for moving down and diagonally, and store the minimum
    down: int = triangle[i][j] + min_path_sum(
        i=i + 1, j=j, n=n, m=m, triangle=triangle, dp=dp
    )
    diagonal: int = triangle[i][j] + min_path_sum(
        i=i + 1, j=j + 1, n=n, m=m, triangle=triangle, dp=dp
    )
    dp[i][j] = min(down, diagonal)
    return dp[i][j]


def min_path_tabulation(n: int, m: int, triangle: list[list[int]]) -> int:
    """Tabulation approach for dynamic programming"""
    # Initialize the dp table with the bottom row of the triangle
    dp: list[list[int]] = [[0 for col in range(m)] for row in range(n)]
    for j in range(m):
        dp[n - 1][j] = triangle[n - 1][j]

    # Fill in the dp table from bottom to top
    for i in range(n - 2, -1, -1):
        for j in range(i, -1, -1):
            d: int = triangle[i][j] + dp[i + 1][j]
            dg: int = triangle[i][j] + dp[i + 1][j + 1]
            dp[i][j] = min(d, dg)

    return dp[0][0]


def min_path_optimal(n: int, m: int, triangle: list[list[int]]) -> int:
    """Optimized space complexity using only two rows"""
    # Initialize the current row with the bottom row of the triangle
    prev: list[int] = [0] * m
    for j in range(m):
        prev[j] = triangle[n - 1][j]

    # Update the row iteratively from bottom to top
    for i in range(n - 2, -1, -1):
        cur: list[int] = [0] * (i + 1)
        for j in range(i, -1, -1):
            d: int = triangle[i][j] + prev[j]
            dg: int = triangle[i][j] + prev[j + 1]
            cur[j] = min(d, dg)
        prev = cur

    return prev[0]


if __name__ == "__main__":
    # Example triangle
    triangle: list[list[int]] = [
        [1],
        [2, 3],
        [3, 6, 7],
        [8, 9, 6, 10],
    ]
    n: int = len(triangle)
    m: int = len(triangle[n - 1])
    # Initialize memoization table with -1
    dp: list[list[int]] = [[-1 for col in range(m)] for row in range(n)]
    # Calculate and print results using different approaches
    mn_path: int = min_path_sum(i=0, j=0, n=n, m=m, triangle=triangle, dp=dp)
    print("Minimum Path Sum (Recursive with Memoization):", mn_path)
    print(
        "Minimum Path Sum (Tabulation):",
        min_path_tabulation(n=n, m=m, triangle=triangle),
    )
    print(
        "Minimum Path Sum (Optimized Space):",
        min_path_optimal(n=n, m=m, triangle=triangle),
    )
