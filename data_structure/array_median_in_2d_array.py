"""
Find Median of 2d array.
"""


class Solution:
    def __init__(self, arr: list[list[int]]) -> None:
        self.arr: list[list[int]] = arr
        self.n = len(self.arr)
        self.m = len(self.arr[0])

    def min_max(self) -> (int, int):
        mn: int = 99999
        mx: int = -99999
        for i in range(self.n):
            mn = min(self.arr[i][0], mn)
            mx = max(self.arr[i][self.m - 1], mx)

        return (mn, mx)

    def upper_bound(self, row: int, target: int) -> int:
        n = self.m
        ans = n
        low: int = 0
        high: int = n - 1

        while low <= high:
            mid = (low + high) // 2
            if self.arr[row][mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def calculate_smaller_count(self, num: int) -> int:
        cnt: int = 0
        for i in range(self.n):
            cnt += self.upper_bound(row=i, target=num)

        return cnt

    def median(self) -> int:
        mn, mx = self.min_max()
        low: int = mn
        high: int = mx
        required: int = (self.n * self.m) // 2
        while low <= high:
            mid: int = (low + high) // 2
            smaller_equals = self.calculate_smaller_count(mid)
            if smaller_equals <= required:
                low = mid + 1
            else:
                high = mid - 1

        return low

    def print_arr(self) -> None:
        for row in self.arr:
            print(row, sep=" ")


if __name__ == "__main__":
    arr: list[list[int]] = [
        [1, 5, 7, 9, 11],
        [2, 3, 4, 5, 10],
        [9, 10, 12, 14, 16],
    ]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.median())
