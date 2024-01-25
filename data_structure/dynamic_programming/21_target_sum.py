"""Count partitions with given differencesubsets with sum k.
SImilar problem like chaning sings + or - makes a target."""


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
    print(number_of_subset_optimal(arr=arr, n=n, d=target))
