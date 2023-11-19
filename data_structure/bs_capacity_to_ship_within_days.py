"""
Find the least capacity to ship packages within D days.
"""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr: list[int] = arr
        self.n = len(self.arr)

    def days_required(self, capacity) -> int:
        day: int = 1
        loaded: int = 0
        for i in range(self.n):
            if loaded + self.arr[i] > capacity:
                day += 1
                loaded = self.arr[i]
            else:
                loaded += self.arr[i]

        return day

    def find_capacity(self, days: int) -> int:
        low: int = max(self.arr)
        high: int = sum(self.arr)
        for i in range(low, high + 1):
            days_required = self.days_required(capacity=i)
            if days_required <= days:
                return i
        return -1

    def find_calapity_optimal(self, days: int) -> int:
        ans: int = 123456789
        low: int = max(self.arr)
        high: int = sum(self.arr)

        while low <= high:
            mid: int = (low + high) // 2
            days_required = self.days_required(capacity=mid)
            if days_required <= days:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    solution = Solution(weights)
    solution.print_arr()
    print(solution.find_capacity(5))
    print(solution.find_calapity_optimal(5))
