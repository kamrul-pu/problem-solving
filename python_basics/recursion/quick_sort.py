"""Quick Sort using Hoare Partition."""


def partition_index(arr: list[int], low: int, high: int) -> None:
    pivot: int = arr[low]
    i: int = low
    j: int = high

    while True:
        # find the element greater than or equal to pivot
        while arr[i] < pivot:
            i += 1
        # find the element greater than or equal to pivot
        while arr[j] > pivot:
            j -= 1

        # if two pointers met.
        if i >= j:
            return j

        # swap i and j element
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr: list[int], low: int, high: int) -> None:
    if low < high:
        # find the partition index
        pi = partition_index(arr, low, high)
        quick_sort(arr=arr, low=low, high=pi)
        quick_sort(arr=arr, low=pi + 1, high=high)


if __name__ == "__main__":
    arr: list[int] = [11, 9, 29, 7, 2, 15, 28]
    print("before sort: ", arr)
    # sort the array
    quick_sort(arr=arr, low=0, high=len(arr) - 1)
    print("after sort: ", arr)
    test_cases = [[10, 3, 15, 7, 8, 23, 98, 29], [], [3], [9, 8, 7, 2], [1, 2, 3, 4, 5]]
    for ar in test_cases:
        quick_sort(arr=ar, low=0, high=len(ar) - 1)
        print(ar)
