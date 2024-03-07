def rod_cutting(i: int, n: int, price: list[int], memo={}) -> int:
    # Base case: if the rod length is 0, return 0
    if i == 0:
        return n * price[0]

    # Check if the result for the current parameters is already memoized
    if (i, n) in memo:
        return memo[(i, n)]

    # Option 1: Do not take the current piece of the rod
    not_take: int = 0 + rod_cutting(i=i - 1, n=n, price=price, memo=memo)

    # Option 2: Take the current piece of the rod if it fits
    take: int = float("-inf")
    rod_length: int = i + 1
    if rod_length <= n:
        take = price[i] + rod_cutting(i=i, n=n - rod_length, price=price, memo=memo)

    # Memoize the result and return the maximum of the two options
    memo[(i, n)] = max(take, not_take)
    return memo[(i, n)]


def rod_cutting_tabulation(price: list[int], n: int, N: int) -> int:
    # Initialize a table for dynamic programming
    dp: list[list[int]] = [[0 for col in range(N + 1)] for row in range(n)]

    # Fill in the base case for the smallest rod length
    for i in range(N + 1):
        dp[0][i] = price[0] * i

    # Fill in the DP table using bottom-up approach
    for i in range(1, n):
        for c in range(N + 1):
            # Option 1: Do not take the current piece of the rod
            not_take: int = 0 + dp[i - 1][c]

            # Option 2: Take the current piece of the rod if it fits
            take: int = float("-inf")
            rod_length: int = i + 1
            if rod_length <= c:
                take = price[i] + dp[i][c - rod_length]

            # Store the maximum of the two options in the table
            dp[i][c] = max(take, not_take)

    # Return the result for the maximum rod length and total available length
    return dp[n - 1][N]


def rod_cutting_optimal(price: list[int], n: int, N: int) -> int:
    # Initialize a 1D array to store the optimal values for each subproblem
    prev: list[int] = [price[0] * col for col in range(N + 1)]

    # Fill in the 1D array using bottom-up approach
    for i in range(1, n):
        for c in range(N + 1):
            # Option 1: Do not take the current piece of the rod
            not_take: int = 0 + prev[c]

            # Option 2: Take the current piece of the rod if it fits
            take: int = float("-inf")
            rod_length: int = i + 1
            if rod_length <= c:
                take = price[i] + prev[c - rod_length]

            # Store the maximum of the two options in the array
            prev[c] = max(take, not_take)

    # Return the result for the maximum rod length and total available length
    return prev[N]


if __name__ == "__main__":
    # Example usage
    price: list[int] = [2, 5, 7, 8, 10]
    N: int = 5
    n: int = len(price)

    # Print results from different approaches
    print(rod_cutting(i=n - 1, n=N, price=price))
    print(rod_cutting_tabulation(price=price, n=n, N=N))
    print(rod_cutting_optimal(price=price, n=n, N=N))
