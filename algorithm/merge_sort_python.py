class MergeSort:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def merge(self, low: int, mid: int, high: int) -> None:
        temp: list[int] = []
        left = low
        right = mid + 1
        while left <= mid and right <= high:
            if self.arr[left] <= self.arr[right]:
                temp.append(self.arr[left])
                left += 1
            else:
                temp.append(self.arr[right])
                right += 1

        while left <= mid:
            temp.append(self.arr[left])
            left += 1
        while right <= high:
            temp.append(self.arr[right])

        for i in range(low, high + 1):
            self.arr[i] = temp[i - low]

    def merge_sort(self, low: int, high: int) -> None:
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)


arr = [40, 25, 19, 12, 13, 33]

ms = MergeSort(arr=arr)
ms.merge_sort(0, len(arr) - 1)
print(arr)
