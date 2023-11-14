def binary_search(arr: list[int], n: int, target: int) -> int:
    """Binary search Iterative way O(logn)"""
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr: list[int], low: int, high: int, target: int) -> int:
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)


arr = [3, 4, 6, 7, 9, 12, 16, 17]
# print(binary_search(arr, len(arr), 12))
print(binary_search_recursive(arr, 0, len(arr) - 1, 3))
