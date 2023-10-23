"""Binary Search."""
import numpy as np
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + "took " + str((end - start) * 1000) + " miliseconds")
        return result

    return wrapper


@time_it
def linear_search(numbers: list[int], to_find: int):
    for index, element in enumerate(numbers):
        if element == to_find:
            return index

    return -1


@time_it
def binary_search(numbers: list[int], to_find: int):
    low = 0
    high = len(numbers) - 1

    while high - low > 1:
        mid = (low + high) // 2
        if numbers[mid] < to_find:
            low = mid + 1
        else:
            high = mid

    if numbers[low] == to_find:
        return low
    elif numbers[high] == to_find:
        return high
    else:
        return -1


def binary_search_recursive(numbers: list[int], to_find: int, low: int, high: int):
    if high < low:
        return -1
    mid = (low + high) // 2
    if numbers[mid] == to_find:
        return mid
    if numbers[mid] < to_find:
        # low = mid + 1
        return binary_search_recursive(numbers, to_find, mid + 1, high)
    else:
        # high = mid
        return binary_search_recursive(numbers, to_find, low, mid)


if __name__ == "__main__":
    # numbers = [12, 15, 17, 19, 21, 24, 45, 68]
    # numbers = range(1, 1000001)
    numbers = np.arange(1, 1000001)
    to_find = 5678
    index = linear_search(numbers=numbers, to_find=to_find)
    print(f"Number {to_find} found at index {index} using linear search")

    index = binary_search(numbers=numbers, to_find=to_find)
    print(f"Number {to_find} found at index {index} using binary search")

    index = binary_search_recursive(
        numbers=numbers, to_find=to_find, low=0, high=len(numbers) - 1
    )
    print(f"Number {to_find} found at index {index} using binary search recursive")
