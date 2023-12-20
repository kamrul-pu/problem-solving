def merge(arr: list[int], low: int, mid: int, high: int) -> None:
    temp: list[int] = []
    left: int = low
    right: int = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
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


def merge_sort(arr: list[int], low: int, high: int) -> None:
    # if single element then return
    if low >= high:
        return
    # find mid
    mid: int = (low + high) // 2
    # divide the left portion
    merge_sort(arr=arr, low=low, high=mid)
    # divide the right protion
    merge_sort(arr=arr, low=mid + 1, high=high)
    # merge the halves
    merge(arr=arr, low=low, mid=mid, high=high)


arr: list[int] = [3, 2, 4, 1, 3]

merge_sort(arr=arr, low=0, high=len(arr) - 1)

print("after sorted array is: ", arr)
