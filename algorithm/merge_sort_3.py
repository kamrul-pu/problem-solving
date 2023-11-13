def merge(arr: list[int], low: int, mid: int, high: int) -> int:
    temp = []  # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1  # starting index of right half of arr

    # storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # if elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # transfering all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def mergeSort(arr: list[int], low: int, high: int) -> int:
    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, low, mid)  # left half
        mergeSort(arr, mid + 1, high)  # right half
        merge(arr, low, mid, high)  # merging sorted halves


arr = [40, 25, 19, 12, 9, 6, 2]

mergeSort(arr, 0, len(arr) - 1)
print(arr)
