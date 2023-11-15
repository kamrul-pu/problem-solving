""" a[i]> 2 * arr[j]."""


class Solution:
    def __init__(self, arr: list[int] = []) -> None:
        self.arr = arr

    def first_and_last_occurance(self, target: int) -> list[int]:
        first: int = -1
        last: int = -1
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                if first == -1:
                    first = i
                last = i

        return [first, last]

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.first_and_last_occurance(2))
