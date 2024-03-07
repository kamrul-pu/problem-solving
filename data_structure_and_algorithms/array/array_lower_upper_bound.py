""" a[i]> 2 * arr[j]."""


class Solution:
    def __init__(self, arr: list[int] = []) -> None:
        self.arr = arr

    def lower_bound(self, target: int) -> int:
        n = len(self.arr)
        ans = n
        low: int = 0
        high: int = n - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def upper_bound(self, target: int) -> int:
        n = len(self.arr)
        ans = n
        low: int = 0
        high: int = n - 1

        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.lower_bound(8))
    print(soltuion.upper_bound(8))
