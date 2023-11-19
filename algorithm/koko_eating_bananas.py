"""
Find nth root.
N = 3 M = 27 3sqrt(27) = 3  ans: 3X3X3 =27
N = 4 M = 69 4sqrt(69) = -1 
"""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr: list[int] = arr
        self.n = len(self.arr)

    def time_take(self, hourly: int) -> int:
        total_hour: int = 0
        for i in range(self.n):
            total_hour += (self.arr[i] // hourly) + (self.arr[i] % hourly != 0)
        return total_hour

    def eat_banana(self, h: int) -> int:
        ct: int = 1
        while True:
            total = self.time_take(ct)
            if total > h:
                ct += 1
            else:
                return ct

    def eat_hourly(self, h: int) -> int:
        low: int = 1
        high: int = max(self.arr)
        ans: int = 12345678
        while low <= high:
            mid: int = (low + high) // 2
            total = self.time_take(mid)
            if total <= h:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    solution = Solution(piles)
    solution.print_arr()
    print(solution.eat_banana(8))
    print(solution.eat_hourly(8))
