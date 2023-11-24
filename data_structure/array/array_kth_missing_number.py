"""
Array Kth Missing number solution.
"""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr: list[int] = arr
        self.n = len(self.arr)

    def find_missing_number(self, k: int) -> int:
        for i in self.arr:
            if i <= k:
                k += 1
            else:
                break

        return k

    def find_missing_optimal(self, k: int) -> int:
        low: int = 0
        high: int = self.n - 1
        while low <= high:
            mid: int = (low + high) // 2
            if (self.arr[mid] - (mid + 1)) > k:
                high = mid - 1
            else:
                low = mid + 1

        # more: int = k - (self.arr[high] - (high + 1))
        # return self.arr[high] + more
        # return k + high + 1
        return low + k

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [2, 3, 4, 7, 11]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.find_missing_number(5))
    print(solution.find_missing_optimal(5))
