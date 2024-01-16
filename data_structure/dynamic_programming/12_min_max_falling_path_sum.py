"""Maximum/ Minimum falling path sum."""

# Constants for representing positive and negative infinity
INT_MAX: int = float("inf")
INT_MIN: int = float("-inf")

# Global counter variable for tracking recursive calls
cnt: int = 0


# Recursive function to find the maximum falling path sum
def max_path_sum(
    i: int, j: int, grid: list[list[int]], n: int, m: int, dp: list[list[int]]
) -> int:
    global cnt
    cnt += 1

    # Base case: if the column index is out of bounds
    if j < 0 or j >= m:
        return INT_MIN

    # Base case: if it's the first row, return the value in the current cell
    if i == 0:
        return grid[i][j]

    # If the result for the current cell is already computed, return it
    if dp[i][j] != -1:
        return dp[i][j]

    # Calculate the maximum falling path sum recursively
    s: int = grid[i][j] + max_path_sum(i=i - 1, j=j, grid=grid, n=n, m=m, dp=dp)
    ld: int = grid[i][j] + max_path_sum(i=i - 1, j=j - 1, grid=grid, n=n, m=m, dp=dp)
    rd: int = grid[i][j] + max_path_sum(i=i - 1, j=j + 1, grid=grid, n=n, m=m, dp=dp)
    dp[i][j] = max(s, ld, rd)

    return dp[i][j]


# Function using tabulation to find the maximum falling path sum
def max_path_sum_tabulation(n: int, m: int, grid: list[list[int]]) -> int:
    dp: list[list[int]] = [[0 for _ in range(m)] for row in range(n)]

    # Initialize the first row of the dp table with values from the grid
    for j in range(m):
        dp[0][j] = grid[0][j]

    # Fill in the dp table iteratively
    for i in range(1, n):
        for j in range(m):
            up: int = grid[i][j] + dp[i - 1][j]
            ld: int = grid[i][j] + (dp[i - 1][j - 1] if j - 1 >= 0 else INT_MIN)
            rd: int = grid[i][j] + (dp[i - 1][j + 1] if j + 1 < m else INT_MIN)

            dp[i][j] = max(up, ld, rd)

    # Find the maximum value in the last row of the dp table
    maxi: int = INT_MIN
    for j in range(m):
        maxi = max(maxi, dp[n - 1][j])

    return maxi


# Function using optimal space to find the maximum falling path sum
def max_path_sum_optimal(n: int, m: int, grid: list[list[int]]) -> int:
    prev: list[int] = [0] * m

    # Initialize the 'prev' array with values from the first row of the grid
    for j in range(m):
        prev[j] = grid[0][j]

    # Iterate through the grid and update the 'prev' array with maximum falling path sum
    for i in range(1, n):
        cur: list[int] = [0] * m
        for j in range(m):
            up: int = grid[i][j] + prev[j]
            ld: int = grid[i][j] + prev[j - 1] if j - 1 >= 0 else INT_MIN
            rd: int = grid[i][j] + prev[j + 1] if j + 1 < m else INT_MIN
            cur[j] = max(up, ld, rd)
        prev = cur

    # Find the maximum value in the last row of the dp table
    maxi: int = INT_MIN
    for j in range(m):
        maxi = max(maxi, prev[j])

    return maxi


if __name__ == "__main__":
    # Example grid for testing
    grid: list[list[int]] = [
        [1, 2, 10, 4],
        [100, 3, 2, 1],
        [1, 1, 20, 2],
        [1, 2, 2, 1],
    ]
    n: int = len(grid)
    m: int = len(grid[0])

    # Variables for tracking results
    mps: int = INT_MIN
    dp: list[list[int]] = [[-1 for col in range(m)] for row in range(n)]

    # Calculate the maximum falling path sum using recursion for each starting column
    for j in range(m):
        mps = max(mps, max_path_sum(i=n - 1, j=j, grid=grid, n=n, m=m, dp=dp))

    # Print the final result and the number of recursive calls
    print("Final Maximum Falling Path Sum:", mps)
    print("Number of Recursive Calls:", cnt)

    # Test the tabulation function
    print("Tabulation Result:", max_path_sum_tabulation(n=n, m=m, grid=grid))

    # Test the optimal space function
    print("Optimal Space Result:", max_path_sum_optimal(n=n, m=m, grid=grid))
