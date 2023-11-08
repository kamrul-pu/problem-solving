"""Leaders mean the all right most element should be smaller."""
import array


class Solution:
    def __init__(self, arr) -> None:
        self.arr = arr

    def sprial_traversal(self):
        n = len(self.arr)
        m = len(self.arr[0])
        left: int = 0
        right: int = m - 1
        top: int = 0
        bottom: int = n - 1

        while left <= right and top <= bottom:
            # traverse left to right
            for i in range(left, right + 1):
                print(self.arr[top][i], end=" ")
            top += 1
            # traverse top to bottom
            for i in range(top, bottom + 1):
                print(self.arr[i][right], end=" ")
            right -= 1
            # traverse right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    print(self.arr[bottom][i], end=" ")
                bottom -= 1
            # traverse bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    print(self.arr[i][left], end=" ")

                left += 1

    def print_arr(self) -> None:
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                print(self.arr[i][j], end=" ")
            print()
        print()


if __name__ == "__main__":
    n: int = 4
    m: int = 4
    arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    solution = Solution(arr)
    solution.print_arr()
    solution.sprial_traversal()
