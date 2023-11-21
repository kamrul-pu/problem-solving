"""
Painters Partition./ Split array -largest sum 
"""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr: list[int] = arr
        self.n = len(self.arr)

    def number_of_painters(self, allowed: int) -> int:
        painter: int = 1
        given: int = 0
        for i in range(self.n):
            if given + self.arr[i] <= allowed:
                given += self.arr[i]
            else:
                painter += 1
                given = self.arr[i]

        return painter

    def painters_partition(self, k: int) -> int:
        low: int = max(self.arr)
        high: int = sum(self.arr)
        for i in range(low, high + 1):
            painter = self.number_of_painters(i)
            if painter == k:
                return i
        return -1

    def painters_partition_optimal(self, k: int) -> int:
        low: int = max(self.arr)
        high: int = sum(self.arr)

        while low <= high:
            mid: int = (low + high) // 2
            painter = self.number_of_painters(mid)
            if painter > k:
                low = mid + 1
            else:
                high = mid - 1

        return low

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [10, 20, 30, 40]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.painters_partition(2))
    print(solution.painters_partition(2))
