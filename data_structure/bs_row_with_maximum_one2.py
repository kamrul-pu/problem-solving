"""
Maximum rows having one.
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

    @time_it
    def find_max_one_brute(self) -> int:
        ones: int = 0
        max_row: int = -1
        for row in range(self.n):
            cnt: int = 0
            for col in range(self.m):
                cnt += self.arr[row][col]

            if cnt > ones:
                ones = cnt
                max_row = row

        return max_row

    @time_it
    def find_max_one_better(self) -> int:
        ones: int = 0
        max_row: int = -1
        for row in range(self.n):
            cnt: int = 0
            low: int = 0
            high: int = self.m - 1
            while low <= high:
                mid: int = (low + high) // 2
                if self.arr[row][mid] == 1:
                    cnt = max(cnt, self.m - mid)
                    high = mid - 1
                else:
                    low = mid + 1
            if cnt > ones:
                ones = cnt
                max_row = row

        return max_row

    def print_arr(
        self,
    ) -> None:
        for row in self.arr:
            print(row, sep=" ")


if __name__ == "__main__":
    arr: list[list[int]] = [
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
    ]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.find_max_one_brute())
    print(solution.find_max_one_better())
