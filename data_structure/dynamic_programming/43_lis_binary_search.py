"""Longest Increasing Subsequence. LIS using Binary Search."""

from typing import List


def lower_bound(arr: List[int], n: int, target: int) -> int:
    ans = n
    low: int = 0
    high: int = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def lis_using_binary_search(arr: List[int], n: int) -> int:
    temp: List[int] = [arr[0]]
    for i in range(1, n):
        if arr[i] > temp[-1]:
            temp.append(arr[i])
        else:
            ind: int = lower_bound(temp, len(temp), arr[i])
            temp[ind] = arr[i]

    return len(temp)


def get_lis(arr: List[int]) -> int:
    n: int = len(arr)
    return lis_using_binary_search(arr, n)


if __name__ == "__main__":
    arr: List[int] = [1, 7, 8, 4, 5, 6, -1, 9]
    print(get_lis(arr))
