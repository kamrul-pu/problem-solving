""" a[i]> 2 * arr[j]."""


class Solution:
    def __init__(self, arr: list[int] = []) -> None:
        self.arr: list[int] = arr
        self.n: int = len(self.arr)

    def find_element(self, x: int) -> int:
        for i in range(self.n):
            if self.arr[i] == x:
                return i

        return -1

    def find_element_better(self, x: int) -> int:
        low: int = 0
        high: int = self.n - 1

        while low <= high:
            if self.arr[low] == x:
                return low
            elif self.arr[high] == x:
                return high
            else:
                low += 1
                high -= 1

        return -1

    def find_elemenet_optimal(self, x: int) -> int:
        low: int = 0
        high: int = self.n - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == x:
                return mid
            # identify the sorted portion
            if self.arr[low] <= self.arr[mid]:
                # left part is sorted
                if self.arr[low] <= x and x <= self.arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # right part is sorted
                if self.arr[mid] <= x and x <= self.arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.find_element(10))
    print(soltuion.find_element_better(10))
    print(soltuion.find_elemenet_optimal(9))
