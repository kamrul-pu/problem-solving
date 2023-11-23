"""
Find Maximum element in 2D matrix
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
    def find_element(self, target: int) -> bool:
        for row in range(self.n):
            low: int = 0
            high: int = self.m - 1
            if self.arr[row][low] <= target and target <= self.arr[row][high]:
                while low <= high:
                    mid: int = (low + high) // 2
                    if self.arr[row][mid] == target:
                        return True
                        # return (row, mid)
                    elif self.arr[row][mid] > target:
                        high = mid - 1
                    else:
                        low = mid + 1
            else:
                continue

        return False
        # return (-1, -1)

    @time_it
    def find_element_optimal(self, target: int) -> bool:
        low: int = 0
        high: int = self.n - 1
        while low <= high:
            mid: int = (low + high) // 2
            if self.arr[mid][0] <= target and target <= self.arr[mid][self.m - 1]:
                l: int = 0
                h: int = self.m - 1
                while l <= h:
                    m: int = (l + h) // 2
                    if self.arr[mid][m] == target:
                        # return True
                        return (mid, m)
                    elif self.arr[mid][m] > target:
                        h = m - 1
                    else:
                        l = m + 1
            elif target < self.arr[mid][0]:
                high = mid - 1
            else:
                low = mid + 1

        return False

    @time_it
    def find_element_optimal_2(self, target: int) -> bool:
        low: int = 0
        high: int = (self.n * self.m) - 1
        while low <= high:
            mid: int = (low + high) // 2
            row: int = mid // self.m
            col: int = mid % self.m
            if self.arr[row][col] == target:
                return True
            elif self.arr[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1

    def print_arr(self) -> None:
        for row in self.arr:
            print(row, sep=" ")


if __name__ == "__main__":
    arr: list[list[int]] = [
        [3, 4, 7, 9],
        [12, 13, 16, 18],
        [20, 21, 23, 29],
    ]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.find_element(target=23))
    print(solution.find_element_optimal(target=23))
    print(solution.find_element_optimal_2(target=23))
