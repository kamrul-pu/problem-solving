""" a[i]> 2 * arr[j]."""


class Solution:
    def __init__(self, arr: list[int] = []) -> None:
        self.arr = arr

    def ceil(self, target: int) -> int:
        n = len(self.arr)
        ans = -1
        low: int = 0
        high: int = n - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] >= target:
                ans = self.arr[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def floor(self, target: int) -> int:
        ans: int = -1
        n = len(self.arr)
        low: int = 0
        high: int = n - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] <= target:
                ans = self.arr[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.ceil(10))
    print(soltuion.floor(10))
