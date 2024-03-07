"""Count partitions with given differencesubsets with sum k."""


def generate_subset(arr: list[int], i: int, target: int, memo={}) -> int:
    if i == 0:
        if target == 0 and arr[0] == 0:
            return 2
        if target == 0 or target == arr[0]:
            return 1
        return 0
    key: tuple[int] = (i, target)
    if key in memo:
        return memo[key]
    take: int = (
        generate_subset(arr=arr, i=i - 1, target=target - arr[i], memo=memo)
        if arr[i] <= target
        else 0
    )
    not_take: int = generate_subset(arr=arr, i=i - 1, target=target, memo=memo)
    memo[key] = take + not_take
    return memo[key]


def number_of_subset(arr: list[int], n: int, d: int) -> int:
    total: int = sum(arr)
    if total - d < 0 or (total - d) % 2 == 1:
        return 0
    return generate_subset(arr=arr, i=n - 1, target=(total - d) // 2, memo={})


def number_of_subset_tabulation(arr: list[int], n: int, d: int) -> int:
    total: int = sum(arr)
    if total - d < 0 or (total - d) % 2 == 1:
        return 0
    target: int = (total - d) // 2
    dp: list[list[int]] = [[0 for col in range(target + 1)] for row in range(n)]
    if arr[0] == 0:
        dp[0][0] = 2
    else:
        dp[0][0] = 1

    if arr[0] != 0 and arr[0] <= target:
        dp[0][arr[0]] = 1

    for i in range(1, n):
        for t in range(1, target + 1):
            take: int = dp[i - 1][t - arr[i]] if arr[i] <= t else 0
            not_take: int = dp[i - 1][t]

            dp[i][t] = take + not_take

    return dp[n - 1][target]


def number_of_subset_optimal(arr: list[int], n: int, d: int) -> int:
    total: int = sum(arr)
    if total - d < 0 or (total - d) % 2 == 1:
        return 0
    target: int = (total - d) // 2
    prev: list[int] = [0 for _ in range(target + 1)]
    cur: list[int] = [0 for _ in range(target + 1)]
    if arr[0] == 0:
        prev[0] = 2
    else:
        prev[0] = 1

    if arr[0] != 0 and arr[0] <= target:
        prev[arr[0]] = 1

    for i in range(1, n):
        for t in range(1, target + 1):
            not_take: int = prev[t]
            take: int = 0
            if arr[i] <= t:
                take = prev[t - arr[i]]

            cur[t] = take + not_take

        prev = cur.copy()

    return prev[target]


if __name__ == "__main__":
    arr: list[int] = [5, 2, 6, 4]
    n: int = len(arr)
    target: int = 3
    print(number_of_subset(arr=arr, n=n, d=target))
    print(number_of_subset_tabulation(arr=arr, n=n, d=target))
    print(number_of_subset_optimal(arr=arr, n=n, d=target))
