"""
Find the smallest divisors to a given threshold.
"""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr: list[int] = arr
        self.n = len(self.arr)

    def calc_div_sum(self, divisor: int, threshold: int) -> bool:
        sum: int = 0
        for i in range(self.n):
            div = (self.arr[i] // divisor) + (self.arr[i] % divisor != 0)
            sum += div

        return sum <= threshold

    def smallest_divisors(self, threshold: int) -> int:
        low: int = 1
        high: int = max(self.arr)
        for i in range(low, high + 1):
            if self.calc_div_sum(i, threshold):
                return i

        return -1

    def smallest_divisors_optimal(self, threshold: int) -> int:
        low: int = 1
        high: int = max(self.arr)
        ans: int = 123456789
        while low <= high:
            mid: int = (low + high) // 2
            if self.calc_div_sum(mid, threshold):
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    bloom_day = [1, 2, 5, 9]
    solution = Solution(bloom_day)
    solution.print_arr()
    print(solution.smallest_divisors(6))
    print(solution.smallest_divisors_optimal(6))
