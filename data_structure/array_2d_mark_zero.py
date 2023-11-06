"""Leaders mean the all right most element should be smaller."""


class Solution:
    def mark_row(self, arr: list[list[int]], i: int, m: int):
        for j in range(m):
            arr[i][j] = -1

    def mark_col(self, arr: list[list[int]], j: int, n: int):
        for i in range(n):
            arr[i][j] = -1

    def mark_zero(self, arr: list[list[int]], n: int, m: int):
        # mark -1 where to place zero
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    self.mark_row(arr, i, m)
                    self.mark_col(arr, j, n)
        # mark zero to the respected area
        for i in range(n):
            for j in range(m):
                if arr[i][j] == -1:
                    arr[i][j] = 0

    def mark_zero_better(self, arr: list[list[int]], n: int, m: int):
        # make a list and mark where to place zero
        row = [0] * n
        col = [0] * m
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        # now mark the zero
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    arr[i][j] = 0

    def print_arr(self, arr) -> None:
        for i in range(len(arr)):
            print(arr[i], sep=" ", end="\n")
        print()


if __name__ == "__main__":
    n: int = 4
    m: int = 4
    arr = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
    ]
    solution = Solution()
    solution.print_arr(arr)
    solution.mark_zero_better(arr, n, m)
    solution.print_arr(arr)
