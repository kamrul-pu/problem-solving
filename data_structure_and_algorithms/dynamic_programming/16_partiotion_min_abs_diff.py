"""Partition a set into two subsets with minimum absolute sum difference."""

INT_MAX: int = float("inf")


def subset_sum_optimal(arr: list[int], n: int, k: int) -> list[bool]:
    prev: list[bool] = [False for _ in range(k + 1)]

    prev[0] = True
    if arr[0] <= k:
        prev[arr[0]] = True

    for i in range(1, n):
        cur: list[bool] = [False for _ in range(k + 1)]
        cur[0] = True
        for target in range(1, k + 1):
            not_take: bool = prev[target]
            take: bool = False
            if arr[i] <= target:
                take = prev[target - arr[i]]
            cur[target] = take or not_take

        prev = cur

    return prev


def min_subset_sum_diff(arr: list[int], n: int) -> int:
    total: int = sum(arr)
    can_partition: list[bool] = subset_sum_optimal(arr=arr, n=n, k=total)

    mini: int = INT_MAX

    for s1 in range(total // 2):
        if can_partition[s1] == True:
            s2: int = total - s1
            mini = min(mini, abs(s1 - s2))

    return mini


if __name__ == "__main__":
    arr: list[int] = [3, 2, 7]
    n: int = len(arr)
    mini: int = min_subset_sum_diff(arr=arr, n=n)
    print(mini)
