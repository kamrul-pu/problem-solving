"""Number of available subarray with the given xor k"""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def sub_array_count(self, k: int) -> int:
        ct = 0
        n = len(self.arr)
        for i in range(n):
            xor: int = 0
            for j in range(i, n):
                xor ^= self.arr[j]
                if xor == k:
                    ct += 1

        return ct

    def sub_array_count_optimal(self, k: int) -> int:
        ct: int = 0
        xr: int = 0
        n = len(self.arr)
        hsh = dict()
        hsh[xr] = 1
        for i in range(n):
            xr ^= self.arr[i]
            x = xr ^ k
            ct += hsh.get(x, 0)
            if xr in hsh:
                hsh[xr] += 1
            else:
                hsh[xr] = 1
        return ct

    def print_arr(self) -> None:
        print(self.arr, sep=" ")
        print()


if __name__ == "__main__":
    arr = [4, 2, 2, 6, 4]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.sub_array_count(6))
    print(solution.sub_array_count_optimal(6))
