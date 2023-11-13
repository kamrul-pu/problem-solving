""" a[i]> s*arr[j]."""


class Solution:
    def __init__(self, arr: list[int] = []) -> None:
        self.arr = arr

    def reverse_pairs(self) -> list[int]:
        ans: list[list[int]] = []
        n = len(self.arr)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.arr[i] > 2 * self.arr[j]:
                    ans.append([self.arr[i], self.arr[j]])

        return ans

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [40, 25, 19, 12, 9, 6, 2]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.reverse_pairs())
