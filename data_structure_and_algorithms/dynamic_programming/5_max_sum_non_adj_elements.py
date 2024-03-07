cnt: int = 0


def max_sum(ind: int, arr: list[int], memo: dict = {}) -> None:
    # Calculate the maximum sum of non-adjacent elements using memoization.
    global cnt
    cnt += 1
    if ind == 0:
        return arr[ind]
    if ind < 0:
        return 0
    if ind in memo:
        return memo[ind]
    pick: int = arr[ind] + max_sum(ind=ind - 2, arr=arr)
    not_pick: int = 0 + max_sum(ind=ind - 1, arr=arr)
    memo[ind] = max(pick, not_pick)
    print("dict", memo)
    return memo[ind]


def max_sum_tabulation(n: int, arr: list[int]) -> int:
    # Calculate the maximum sum of non-adjacent elements using tabulation.
    dp: list[int] = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        take: int = arr[i] + (dp[i - 2] if i > 1 else 0)
        non_take: int = 0 + dp[i - 1]
        dp[i] = max(take, non_take)

    return dp[n - 1]


def max_sum_optimal(n: int, arr: list[int]) -> int:
    # Calculate the maximum sum of non-adjacent elements using an optimal approach.
    prev: int = arr[0]
    prev2: int = 0
    for i in range(1, n):
        pick: int = arr[i] + prev2
        not_pick: int = 0 + prev
        cur: int = max(pick, not_pick)
        prev2 = prev
        prev = cur

    return prev


if __name__ == "__main__":
    arr: list[int] = [2, 1, 4, 9, 9, 7, 8, 5, 10, 100, 20, 30]
    n: int = len(arr)
    print(max_sum(ind=n - 1, arr=arr))
    print("function called", cnt)
    print(max_sum_tabulation(n=n, arr=arr))
    print(max_sum_optimal(n=n, arr=arr))
