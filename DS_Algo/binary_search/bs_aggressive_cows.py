"""
Aggressive cows minimum distance between cows is maximum.
"""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr: list[int] = arr
        self.n = len(self.arr)

    def can_place_cows(self, cows: int, distance: int) -> bool:
        cp: int = 1
        last_cow: int = self.arr[0]
        for i in range(1, self.n):
            if (self.arr[i] - last_cow) >= distance:
                cp += 1
                last_cow = self.arr[i]
            if cp == cows:
                break
        return cp == cows

    def max_distance(self, cows: int) -> int:
        ans: int = -1
        mx: int = self.arr[self.n - 1] - self.arr[0]
        for i in range(1, mx + 1):
            can_place = self.can_place_cows(cows, i)
            if can_place:
                ans = max(ans, i)
            else:
                break

        return ans

    def max_distance_optimal(self, cows: int) -> int:
        ans: int = -1
        low: int = 1
        high: int = self.arr[-1] - self.arr[0]

        while low <= high:
            mid: int = (low + high) // 2
            can_place = self.can_place_cows(cows, mid)
            if can_place:
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1

        # return ans
        return high

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [0, 3, 4, 7, 9, 10]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.max_distance(4))
    print(solution.max_distance_optimal(4))
