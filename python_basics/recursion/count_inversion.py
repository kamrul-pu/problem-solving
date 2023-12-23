"""Count inversion in an array. i<j and a[i]>a[j]"""


def find_inversions(arr: list[int], ans: list[tuple[int]]) -> int:
    cnt: int = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                cnt += 1
                ans.append((arr[i], arr[j]))

    return cnt


cnt: int = 0


def merge(arr: list[int], low: int, mid: int, high: int) -> None:
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
            global cnt
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


def find_inversions_cnt(arr: list[int], n: int) -> int:
    merge_sort(arr=arr, low=0, high=n - 1)
    return cnt


if __name__ == "__main__":
    arr: list[int] = [5, 3, 2, 4, 1]
    # ans: list[tuple[int]] = []
    # cnt: int = find_inversions(arr=arr, ans=ans)
    # print(ans, cnt)
    cnt: int = find_inversions_cnt(arr=arr, n=len(arr))
    print(cnt)
