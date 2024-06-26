"""
There is an integer array ‘A’ of size ‘N’.

Number of inversions in an array can be defined as the number of pairs of ‘i’, ‘j’ such that ‘i’ < ‘j’ and ‘A[i]’ > ‘A[j]’.

You must return the number of inversions in the array.
"""

from typing import *


def brute(a: List[int], n: int) -> int:
    cnt: int = 0
    for i in range(0, n - 1, 1):
        for j in range(i + 1, n, 1):
            if a[i] > a[j]:
                cnt += 1

    return cnt


def merge(arr: list[int], low: int, mid: int, high: int) -> int:
    cnt: int = 0
    temp: list[int] = []
    left: int = low
    right: int = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        # right is smaller
        else:
            temp.append(arr[right])
            cnt += mid - left + 1
            right += 1
    # check if the elements still in the left portion
    while left <= mid:
        temp.append(arr[left])
        left += 1
    # check if the element still in the right portion
    while right <= high:
        temp.append(arr[right])
        right += 1

    # copy the element to the original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return cnt


def merge_sort(arr: list[int], low: int, high: int) -> int:
    cnt: int = 0
    # if single element then return
    if low >= high:
        return cnt
    # find mid
    mid: int = (low + high) // 2
    # divide the left portion
    cnt += merge_sort(arr=arr, low=low, high=mid)
    # divide the right protion
    cnt += merge_sort(arr=arr, low=mid + 1, high=high)
    # merge the halves
    cnt += merge(arr=arr, low=low, mid=mid, high=high)
    return cnt


def numberOfInversions(a: List[int], n: int) -> int:
    # Write your code here.
    # return brute(a=a, n=n)
    return merge_sort(a, 0, n - 1)


a: List[int] = [5, 3, 2, 1, 4]
n: int = 5
print(numberOfInversions(a=a, n=n))
