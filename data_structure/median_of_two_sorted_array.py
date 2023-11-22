"""
Median Of two sorted array.
"""

import heapq


class Solution:
    def __init__(self, arr1: list[int], arr2: list[int]) -> None:
        self.arr1: list[int] = arr1
        self.arr2: list[int] = arr2
        self.n = len(self.arr1)
        self.m = len(self.arr2)
        self.arr: list[int] = [0] * (self.n + self.m)
        self.size = len(self.arr)

    def merge_two_arr(self):
        i: int = 0
        j: int = 0
        k: int = 0
        while i < self.n and j < self.m:
            if self.arr1[i] < self.arr2[j]:
                self.arr[k] = self.arr1[i]
                i += 1
            else:
                self.arr[k] = self.arr2[j]
                j += 1
            k += 1
        while i < self.n:
            self.arr[k] = self.arr1[i]
            i += 1
            k += 1
        while j < self.m:
            self.arr[k] = self.arr2[j]
            j += 1
            k += 1

    def find_median(self) -> int:
        if self.size % 2 == 0:
            # even number of elements
            ind_1: int = self.size // 2
            ind_2: int = (self.size // 2) - 1
            return (self.arr[ind_1] + self.arr[ind_2]) // 2
        else:
            # odd number of elements
            return self.arr[self.size // 2]

    def find_median_better(self) -> int:
        n: int = self.n + self.m
        ind_1: int = n // 2
        ind_2: int = ind_1 - 1
        cnt: int = 0
        element_1: int = -1
        element_2: int = -1
        i: int = 0
        j: int = 0

        while i < self.n and j < self.m:
            if self.arr1[i] < self.arr2[j]:
                if cnt == ind_1:
                    element_1 = self.arr1[i]
                if cnt == ind_2:
                    element_2 = self.arr1[i]
                i += 1
            else:
                if cnt == ind_1:
                    element_1 = self.arr2[j]
                if cnt == ind_2:
                    element_2 = self.arr2[j]
                j += 1
            cnt += 1

        while i < self.n:
            if cnt == ind_1:
                element_1 = self.arr1[i]
            if cnt == ind_2:
                element_2 = self.arr1[i]
            i += 1
            cnt += 1
        while j < self.m:
            if cnt == ind_1:
                element_1 = self.arr2[j]
            if cnt == ind_2:
                element_2 = self.arr2[j]
            j += 1
            cnt += 1

        if n % 2 == 0:
            return (element_1 + element_2) // 2
        return element_1

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    # arr = [1, 13, 17, 23]
    arr1 = [1, 3, 4, 7, 10, 12]
    arr2: list[int] = [2, 3, 6, 15]
    solution = Solution(arr1, arr2)
    solution.print_arr()
    solution.merge_two_arr()
    solution.print_arr()
    print(solution.find_median())
    print(solution.find_median_better())
