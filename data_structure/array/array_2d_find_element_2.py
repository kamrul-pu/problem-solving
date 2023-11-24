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
    def find_element(self, target: int) -> (int, int):
        for row in range(self.n):
            low: int = 0
            high: int = self.m - 1
            if self.arr[row][low] <= target and target <= self.arr[row][high]:
                while low <= high:
                    mid: int = (low + high) // 2
                    if self.arr[row][mid] == target:
                        # return True
                        return (row, mid)
                    elif self.arr[row][mid] > target:
                        high = mid - 1
                    else:
                        low = mid + 1

        return (-1, -1)

    @time_it
    def find_element_optimal(self, target: int) -> (int, int):
        row: int = 0
        col: int = self.m - 1
        while row < self.n and col >= 0:
            if self.arr[row][col] == target:
                return (row, col)
            elif self.arr[row][col] > target:
                col -= 1
            else:
                row += 1

        return (-1, -1)

    def print_arr(self) -> None:
        for row in self.arr:
            print(row, sep=" ")


if __name__ == "__main__":
    arr: list[list[int]] = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.find_element(target=14))
    print(solution.find_element_optimal(target=14))
    # check for every element
    for row in arr:
        for item in row:
            print(solution.find_element_optimal(item))
