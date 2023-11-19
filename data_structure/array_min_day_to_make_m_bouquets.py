"""
Find nth root.
N = 3 M = 27 3sqrt(27) = 3  ans: 3X3X3 =27
N = 4 M = 69 4sqrt(69) = -1 
"""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr: list[int] = arr
        self.n = len(self.arr)

    def possible_buoquets(self, m: int, k: int, day: int) -> int:
        ct: int = 0
        number_of_buquets = 0
        for i in range(self.n):
            if self.arr[i] <= day:
                ct += 1
            else:
                number_of_buquets += ct // k
                ct = 0
        number_of_buquets += ct // k
        return number_of_buquets

    def days_to_make_bouquets(self, m: int, k: int) -> int:
        if m * k > self.n:
            return -1
        mn: int = min(self.arr)
        mx: int = max(self.arr)
        for day in range(mn, mx + 1):
            num_of_bouquotes = self.possible_buoquets(m, k, day)
            if num_of_bouquotes >= m:
                return day

        return -1

    def days_to_make_bouquets_optimal(self, m: int, k: int) -> int:
        if m * k > self.n:
            return -1
        low: int = min(self.arr)
        high: int = max(self.arr)
        ans: int = 123456789
        while low <= high:
            mid: int = (low + high) // 2
            number_of_bouquet = self.possible_buoquets(m, k, mid)
            if number_of_bouquet >= m:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1

        if ans == 123456789:
            return -1
        return ans

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    bloom_day = [7, 7, 7, 7, 13, 11, 12, 7]
    solution = Solution(bloom_day)
    solution.print_arr()
    # print(solution.days_to_make_bouquets(m=2, k=3))
    print(solution.days_to_make_bouquets_optimal(m=2, k=3))
