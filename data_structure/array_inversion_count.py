"""Number of inversion available in this array."""


class Solution:
    def __init__(self, arr: list[int] = []) -> None:
        self.arr = arr
        self.count = 0

    def inversion_list(self) -> list[list[int]]:
        # TC = O(n^2) Space O(1)
        # For storing result we keep list of list O(n)
        n = len(self.arr)
        ans: list[list[int]] = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.arr[i] > self.arr[j]:
                    ans.append([self.arr[i], self.arr[j]])

        return ans

    def inversion_count(self) -> int:
        cnt: int = 0
        n = len(self.arr)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.arr[i] > self.arr[j]:
                    cnt += 1

        return cnt

    def merge(self, arr: list[int], low: int, mid: int, high: int) -> int:
        temp = []  # temporary array
        left = low  # starting index of left half of arr
        right = mid + 1  # starting index of right half of arr

        cnt = 0  # Modification 1: cnt variable to count the pairs

        # storing elements in the temporary array in a sorted manner
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                cnt += mid - left + 1  # Modification 2
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

        return cnt  # Modification 3

    def mergeSort(self, arr: list[int], low: int, high: int) -> int:
        cnt = 0
        if low >= high:
            return cnt
        mid = (low + high) // 2
        cnt += self.mergeSort(arr, low, mid)  # left half
        cnt += self.mergeSort(arr, mid + 1, high)  # right half
        cnt += self.merge(arr, low, mid, high)  # merging sorted halves
        return cnt

    def inversion_count_optimal(self) -> int:
        n = len(self.arr)
        return self.mergeSort(self.arr, 0, n - 1)

    def print_arr(self) -> None:
        print(self.arr, sep=" ", end="\n")


if __name__ == "__main__":
    arr = [5, 3, 2, 4, 1]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.inversion_list())
    print(soltuion.inversion_count())
    print(soltuion.inversion_count_optimal())
