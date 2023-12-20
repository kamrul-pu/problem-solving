"""Quick Sort Algorithm."""


def partition_index(arr: list[int], low: int, high: int) -> int:
    pivot: int = arr[low]
    i: int = low
    j: int = high
    while i < j:
        while i < high and arr[i] <= pivot:
            i += 1

        while j > low and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr: list[int], low: int, high: int) -> None:
    if low < high:
        pi = partition_index(arr=arr, low=low, high=high)
        quick_sort(arr=arr, low=low, high=pi - 1)
        quick_sort(arr=arr, low=pi + 1, high=high)


if __name__ == "__main__":
    arr: list[int] = [11, 9, 29, 7, 2, 15, 28]
    print("before sort: ", arr)
    # sort the array
    quick_sort(arr=arr, low=0, high=len(arr) - 1)
    print("after sort: ", arr)
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5],
        [4, 6, 2, 5, 7, 9, 1, 3],
    ]
    for ar in test_cases:
        quick_sort(arr=ar, low=0, high=len(ar) - 1)
        print(ar)
