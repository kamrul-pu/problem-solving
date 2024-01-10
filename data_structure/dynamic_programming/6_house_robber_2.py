"""House Robber 2"""


def max_money_optimal(n: int, arr: list[int]) -> int:
    # Calculate the maximum sum of non-adjacent elements using an optimal approach.
    # Calculating by ignoring last element
    # First and last are adjacent.
    prev: int = arr[0]
    prev2: int = 0
    for i in range(1, n - 1):
        pick: int = arr[i] + prev2
        not_pick: int = 0 + prev
        cur: int = max(pick, not_pick)
        prev2 = prev
        prev = cur
    ans1: int = prev
    # calculating by ignoring first element.
    prev = arr[1]
    prev2 = 0
    for i in range(2, n):
        pick: int = arr[i] + prev2
        not_pick: int = 0 + prev
        cur: int = max(pick, not_pick)
        prev2 = prev
        prev = cur
    ans2: int = prev

    return max(ans1, ans2)


if __name__ == "__main__":
    arr: list[int] = [1, 5, 1, 2, 6]
    n: int = len(arr)
    print(max_money_optimal(n=n, arr=arr))
