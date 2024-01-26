"""Coin change problem. Number of ways to make target sum."""


def ways(i: int, amount: int, coins: list[int], memo={}) -> int:
    """
    Recursive function to find the number of ways to make the target sum using given coins.

    Args:
        i (int): Index of the current coin.
        amount (int): Remaining target sum.
        coins (list[int]): List of available coin denominations.
        memo (dict): Memoization dictionary to store already computed results.

    Returns:
        int: Number of ways to make the target sum.
    """
    if i == 0:
        # Base case: If only one coin remaining, check if it divides the remaining amount evenly.
        return int(amount % coins[i] == 0)

    key: tuple[int] = (i, amount)
    if key in memo:
        # If the result for this combination of parameters is already computed, return it.
        return memo[key]

    # Calculate the number of ways by either taking or not taking the current coin.
    not_take: int = ways(i=i - 1, amount=amount, coins=coins, memo=memo)
    take: int = 0
    if coins[i] <= amount:
        take = ways(i=i, amount=amount - coins[i], coins=coins, memo=memo)

    # Memoize the result and return.
    memo[key] = not_take + take
    return memo[key]


def ways_tabulation(coins: list[int], n: int, amount: int) -> int:
    """
    Dynamic programming solution using tabulation to find the number of ways to make the target sum.

    Args:
        coins (list[int]): List of available coin denominations.
        n (int): Number of different coin denominations.
        amount (int): Target sum.

    Returns:
        int: Number of ways to make the target sum.
    """
    # Initialize a 2D array to store the results of subproblems.
    dp: list[list[int]] = [
        [1 if col % coins[0] == 0 else 0 for col in range(amount + 1)]
        for row in range(n)
    ]

    # Iterate over each coin and target sum to fill in the table.
    for i in range(1, n):
        for t in range(amount + 1):
            not_take: int = dp[i - 1][t]
            take: int = 0
            if coins[i] <= t:
                take = dp[i][t - coins[i]]
            dp[i][t] = take + not_take

    # Return the result for the last coin and target sum.
    return dp[n - 1][amount]


def ways_optimal(coins: list[int], n: int, amount: int) -> int:
    """
    Optimized dynamic programming solution using only two arrays to find the number of ways to make the target sum.

    Args:
        coins (list[int]): List of available coin denominations.
        n (int): Number of different coin denominations.
        amount (int): Target sum.

    Returns:
        int: Number of ways to make the target sum.
    """
    # Initialize two arrays to store results of subproblems.
    prev: list[int] = [1 if col % coins[0] == 0 else 0 for col in range(amount + 1)]
    cur: list[int] = [0] * (amount + 1)

    # Iterate over each coin and target sum to fill in the arrays.
    for i in range(1, n):
        for t in range(amount + 1):
            not_take: int = prev[t]
            take: int = 0
            if coins[i] <= t:
                take = cur[t - coins[i]]
            cur[t] = take + not_take
        # Update the previous array with the current one.
        prev = cur

    # Return the result for the target sum.
    return prev[amount]


if __name__ == "__main__":
    # Example usage:
    coins: list[int] = [1, 2, 3]
    amount: int = 4
    n: int = len(coins)

    # Test each function and print the results.
    print(ways(i=n - 1, amount=amount, coins=coins))
    print(ways_tabulation(coins=coins, n=n, amount=amount))
    print(ways_optimal(coins=coins, n=n, amount=amount))
