"""Unbounded knapsack. Infinite supply of items."""


def knapsack(i: int, W: int, wt: list[int], val: list[int], dp: list[list[int]]) -> int:
    if i == 0:
        return (W // wt[0]) * val[0]

    if dp[i][W] != -1:
        return dp[i][W]

    not_take: int = 0 + knapsack(i=i - 1, W=W, wt=wt, val=val, dp=dp)
    take: int = 0
    if wt[i] <= W:
        take = val[i] + knapsack(i=i, W=W - wt[i], wt=wt, val=val, dp=dp)
    dp[i][W] = max(not_take, take)
    return dp[i][W]


def knapsack_tabulation(wt: list[int], n: int, W: int, val: list[int]) -> int:
    dp: list[list[int]] = [[0 for col in range(W + 1)] for row in range(n)]

    for w in range(W + 1):
        dp[0][w] = (w // wt[0]) * val[0]

    for i in range(1, n):
        for w in range(W + 1):
            not_take: int = 0 + dp[i - 1][w]
            take: int = 0
            if wt[i] <= w:
                take = val[i] + dp[i][w - wt[i]]
            dp[i][w] = max(not_take, take)

    return dp[n - 1][W]


def knapsack_optimal(wt: list[int], n: int, W: int, val: list[int]) -> int:
    prev: list[int] = [0 for col in range(W + 1)]

    for w in range(W + 1):
        prev[w] = (w // wt[0]) * val[0]

    for i in range(1, n):
        for w in range(W + 1):
            not_take: int = 0 + prev[w]
            take: int = 0
            if wt[i] <= w:
                take = val[i] + prev[w - wt[i]]
            prev[w] = max(not_take, take)

    return prev[W]


if __name__ == "__main__":
    wt: list[int] = [2, 4, 6]
    val: list[int] = [5, 11, 13]
    n: int = len(wt)
    max_weight: int = 1000
    dp: list[list[int]] = [[-1 for _ in range(max_weight + 1)] for row in range(n)]
    print(knapsack(i=n - 1, W=max_weight, wt=wt, val=val, dp=dp))
    print(knapsack_tabulation(wt=wt, n=n, W=max_weight, val=val))
    print(knapsack_optimal(wt=wt, n=n, W=max_weight, val=val))
