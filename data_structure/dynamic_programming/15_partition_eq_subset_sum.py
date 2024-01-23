"""Make two partition whose sum is equal."""


def subset_sum_optimal(arr: list[int], n: int, k: int) -> bool:
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

    return prev[k]


def can_parition(arr: list[int], n: int) -> bool:
    s: int = sum(arr)
    if s % 2 == 1:
        return False

    s //= 2

    return subset_sum_optimal(arr=arr, n=n, k=s)


if __name__ == "__main__":
    arr: list[int] = [2, 3, 3, 3, 4, 5]
    print(can_parition(arr=arr, n=len(arr)))
