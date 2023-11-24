""" Find single element in the sorted array."""


class Solution:
    def __init__(self, arr: list[int] = []) -> None:
        self.arr: list[int] = arr
        self.n: int = len(self.arr)

    def find_single_element(self) -> int:
        if self.n == 1:
            return self.arr[0]
        for i in range(self.n):
            if i == 0:
                if self.arr[i] != self.arr[i + 1]:
                    return self.arr[i]
            elif i == self.n - 1:
                if self.arr[i] != self.arr[i - 1]:
                    return self.arr[i]
            else:
                if self.arr[i] != self.arr[i + 1] and self.arr[i] != self.arr[i - 1]:
                    return self.arr[i]

        return -1

    def find_single_element_optimal(self) -> int:
        if self.n == 1:
            return self.arr[0]
        if self.arr[0] != self.arr[1]:
            return self.arr[0]
        if self.arr[self.n - 1] != self.arr[self.n - 2]:
            return self.arr[self.n - 1]

        low: int = 1
        high: int = self.n - 2
        while low <= high:
            mid: int = (low + high) // 2
            if (
                self.arr[mid] != self.arr[mid - 1]
                and self.arr[mid] != self.arr[mid + 1]
            ):
                return self.arr[mid]

            if (mid % 2 == 1 and self.arr[mid - 1] == self.arr[mid]) or (
                mid % 2 == 0 and self.arr[mid] == self.arr[mid + 1]
            ):
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.find_single_element())
    print(soltuion.find_single_element_optimal())
