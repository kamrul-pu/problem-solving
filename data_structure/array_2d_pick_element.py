"""
Find Pick element in 2D matrix
"""

import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " miliseconds")
        return result

    return wrapper


class Solution:
    def __init__(self, arr: list[list[int]]) -> None:
        self.arr: list[list[int]] = arr
        self.n = len(self.arr)
        self.m = len(self.arr[0])

    def max_relement_row(self, col: int) -> int:
        """Return the row index where the max value is available"""
        mx = -999999
        row: int = 0
        for i in range(self.n):
            if self.arr[i][col] > mx:
                mx = self.arr[i][col]
                row = i
        return row

    def find_pick_element(self) -> (int, int):
        ans: (int, int) = (-1, -1)
        low: int = 0
        high: int = self.m - 1

        while low <= high:
            mid: int = (low + high) // 2
            row = self.max_relement_row(col=mid)
            left: int = self.arr[row][mid - 1] if mid - 1 >= 0 else -1
            right: int = self.arr[row][mid + 1] if mid + 1 < self.m else -1
            if self.arr[row][mid] > left and self.arr[row][mid] > right:
                return (row, mid)
            elif self.arr[row][mid] < left:
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def print_arr(self) -> None:
        for row in self.arr:
            print(row, sep=" ")


if __name__ == "__main__":
    arr: list[list[int]] = [
        [4, 2, 5, 1, 4, 5],
        [2, 9, 3, 2, 3, 2],
        [1, 7, 6, 0, 1, 3],
        [3, 6, 2, 3, 7, 2],
    ]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.find_pick_element())
