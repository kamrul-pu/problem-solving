"""Number of inversion available in this array."""


class Solution:
    def __init__(self, arr: list[int] = []) -> None:
        self.arr = arr

    def inversion_list(self) -> list[list[int]]:
        # TC = O(n^2) Space O(1)
        # For storing result we keep list of list O(n)
        n = len(self.arr)
        ans: list[list[int]] = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.arr[i] > self.arr[j]:
                    ans.append([self.arr[i], self.arr[j]])

        return ans

    def inversion_count(self) -> int:
        cnt: int = 0
        n = len(self.arr)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.arr[i] > self.arr[j]:
                    cnt += 1

        return cnt

    def print_arr(self) -> None:
        print(self.arr, sep=" ", end="\n")


if __name__ == "__main__":
    arr = [5, 3, 2, 4, 1]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.inversion_list())
    print(soltuion.inversion_count())
