"""Subset Sum equals to target sum."""


def generate_subset(
    arr: list[int], i: int, n: int, subsets: list[list[int]], subset: list[int]
) -> None:
    if i == n:
        subsets.append(subset.copy())
        return
    # take the ith element
    subset.append(arr[i])
    generate_subset(arr=arr, i=i + 1, n=n, subsets=subsets, subset=subset)
    # back track remove the element
    subset.pop()
    # ignore the ith element
    generate_subset(arr=arr, i=i + 1, n=n, subsets=subsets, subset=subset)


def subset_sum(arr: list[int], i: int, n: int, k: int, sum: int) -> bool:
    if i == n:
        print("curr sum", sum)
        return sum == k
    sum += arr[i]
    if subset_sum(arr=arr, i=i + 1, n=n, k=k, sum=sum):
        return True
    sum -= arr[i]
    if subset_sum(arr=arr, i=i + 1, n=n, k=k, sum=sum):
        return True

    return False


def subset_sum_2(arr: list[int], i: int, target: int, dp) -> bool:
    if target == 0:
        return True
    if i == 0:
        return arr[0] == target
    if dp[i][target] != -1:
        return dp[i][target]
    # considering current index
    take: bool = (
        subset_sum_2(arr=arr, i=i - 1, target=target - arr[i], dp=dp)
        if target >= arr[i]
        else False
    )

    # not considering current value
    not_take: bool = subset_sum_2(arr=arr, i=i - 1, target=target, dp=dp)
    dp[i][target] = take or not_take
    return dp[i][target]


def subset_sum_tabulation(arr: list[int], n: int, k: int) -> bool:
    dp: list[list[bool]] = [[False for c in range(k + 1)] for r in range(n)]
    for i in range(n):
        dp[i][0] = True
    dp[0][arr[0]] = True
    for i in range(1, n):
        for target in range(1, k + 1):
            # considering current index
            take: bool = dp[i - 1][target - arr[i]] if target >= arr[i] else False

            # not considering current value
            not_take: bool = dp[i - 1][target]
            dp[i][target] = take or not_take

    return dp[n - 1][k]


def subset_sum_optimal(arr: list[int], n: int, k: int) -> bool:
    prev: list[bool] = [False for _ in range(k + 1)]

    if arr[0] <= k:
        prev[arr[0]] = True
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

    return prev[k]


if __name__ == "__main__":
    arr: list[int] = [1, 2, 3, 4]
    n: int = len(arr)
    subsets: list[list[int]] = []
    generate_subset(arr=arr, i=0, n=n, subsets=subsets, subset=[])
    print(subsets)
    print(subset_sum(arr=arr, i=0, n=n, k=8, sum=0))
    dp: list[list[int]] = [[-1 for col in range(100)] for _ in range(n)]
    print(subset_sum_2(arr=arr, i=n - 1, target=8, dp=dp))
    print(subset_sum_tabulation(arr=arr, n=n, k=11))
    print(subset_sum_optimal(arr=arr, n=n, k=11))
