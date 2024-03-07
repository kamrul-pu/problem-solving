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

    def lower_bound(self, x: int) -> int:
        n: int = len(self.arr)
        ans: int = n
        low: int = 0
        high: int = n - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] >= x:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1

        return ans

    def upper_bound(self, x: int) -> int:
        n: int = len(self.arr)
        ans: int = n
        low: int = 0
        high: int = n - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] > x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def first_last_occurance_by_lb_hb(self, x: int) -> list[int]:
        n: int = len(self.arr)
        lb = self.lower_bound(x)
        if lb == n or self.arr[lb] != x:
            return [-1, -1]
        up = self.upper_bound(x)
        return [lb, up - 1]

    def find_first(self, x: int) -> int:
        n: int = len(self.arr)
        ans: int = -1
        low: int = 0
        high: int = n - 1

        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == x:
                ans = mid
                high = mid - 1
            elif self.arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def find_last(self, x: int) -> int:
        n: int = len(self.arr)
        ans: int = -1
        low: int = 0
        high: int = n - 1

        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == x:
                ans = mid
                low = mid + 1
            elif self.arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def first_last_occurance_2(self, x: int) -> int:
        first: int = self.find_first(x)
        if first == -1:
            return [-1, -1]
        last: int = self.find_last(x)
        return [first, last]

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.first_and_last_occurance(2))
    print(soltuion.lower_bound(9))
    print(soltuion.upper_bound(9))
    print(soltuion.first_last_occurance_by_lb_hb(12))
    print(soltuion.first_last_occurance_2(12))
