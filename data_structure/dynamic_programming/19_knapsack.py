"""0/1 knapsack problem solution."""

def knapsack(wt: list[int], val: list[int], i: int, W: int, memo={}) -> int:
    # Base case: If no items are left or the remaining capacity is 0, return 0
    if i == 0:
        if wt[i] <= W:
            return val[i]
        return 0

    # Memoization: Check if the result for the current state is already computed
    key: tuple[int] = (i, W)
    if key in memo:
        return memo[key]

    # Recursive calls to calculate the maximum value by either taking or not taking the current item
    not_take: int = 0 + knapsack(wt=wt, val=val, i=i - 1, W=W, memo=memo)
    take: int = float("-inf")
    if wt[i] <= W:
        take = val[i] + knapsack(wt=wt, val=val, i=i - 1, W=W - wt[i], memo=memo)

    # Store the result in the memo dictionary and return the maximum value
    memo[key] = max(take, not_take)
    return memo[key]


def knapsack_tabulation(wt: list[int], val: list[int], max_weight: int) -> int:
    n: int = len(wt)

    # Initialize a 2D array for dynamic programming (DP) with zeros
    dp: list[list[int]] = [[0 for col in range(max_weight + 1)] for row in range(n)]

    # Initialize the first row with the value of the first item for weights greater than or equal to its weight
    for w in range(wt[0], max_weight + 1):
        dp[0][w] = val[0]

    # Fill in the DP array using bottom-up approach
    for i in range(1, n):
        for w in range(max_weight + 1):
            # Calculate the maximum value by either taking or not taking the current item
            not_take: int = 0 + dp[i - 1][w]
            take: int = float("-inf")
            if wt[i] <= w:
                take = val[i] + dp[i - 1][w - wt[i]]

            # Update the DP array with the maximum value
            dp[i][w] = max(take, not_take)

    # The result is stored in the bottom-right corner of the DP array
    return dp[n - 1][max_weight]


def knapsack_optimal(wt: list[int], val: list[int], max_weight: int) -> int:
    n: int = len(wt)

    # Use a 1D array to store the DP values for the current row
    prev: list[int] = [0 for col in range(max_weight + 1)]

    # Initialize the first row with the value of the first item for weights greater than or equal to its weight
    for w in range(wt[0], max_weight + 1):
        prev[w] = val[0]

    # Fill in the DP array using bottom-up approach with optimized space complexity
    for i in range(1, n):
        for w in range(max_weight, -1, -1):
            # Calculate the maximum value by either taking or not taking the current item
            not_take: int = 0 + prev[w]
            take: int = float("-inf")
            if wt[i] <= w:
                take = val[i] + prev[w - wt[i]]

            # Update the DP array with the maximum value
            prev[w] = max(take, not_take)

    # The result is stored in the last element of the 1D DP array
    return prev[max_weight]


if __name__ == "__main__":
    # Example input data
    wt: list[int] = [3, 2, 5]
    val: list[int] = [30, 40, 60]
    n: int = len(wt)
    W: int = 6

    # Test each knapsack function and print the result
    max_val: int = knapsack(wt=wt, val=val, i=n - 1, W=W)
    print("Recursive with Memoization:", max_val)

    max_val_tabulation: int = knapsack_tabulation(wt=wt, val=val, max_weight=W)
    print("Tabulation:", max_val_tabulation)

    max_val_optimal: int = knapsack_optimal(wt=wt, val=val, max_weight=W)
    print("Optimal Space Complexity:", max_val_optimal)
