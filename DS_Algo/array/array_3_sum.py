"""Array 3 Sum Solution."""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def _3_sum_brute(self) -> list[list[int]]:
        ans = set()
        n = len(self.arr)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.arr[i] + self.arr[j] + self.arr[k] == 0:
                        temp = [self.arr[i], self.arr[j], self.arr[k]]
                        temp.sort()
                        ans.add(tuple(temp))

        return ans

    def _3_sum_better(self) -> set:
        ans = set()
        n = len(self.arr)
        for i in range(n):
            temp = set()
            for j in range(i + 1, n):
                third = -(self.arr[i] + self.arr[j])
                if third in temp:
                    triple = [self.arr[i], self.arr[j], third]
                    triple.sort()
                    ans.add(tuple(triple))
                temp.add(self.arr[j])

        return ans

    def _3_sum_optimal(self) -> list[list[int]]:
        ans: list[list[int]] = []
        self.arr.sort()
        n: int = len(self.arr)
        for i in range(n):
            if i > 0 and self.arr[i] == self.arr[i - 1]:
                continue
            j: int = i + 1
            k: int = n - 1
            while j < k:
                sum: int = self.arr[i] + self.arr[j] + self.arr[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    ans.append([self.arr[i], self.arr[j], self.arr[k]])
                    j += 1
                    k -= 1

                    while j < k and self.arr[j] == self.arr[j - 1]:
                        j += 1
                    while j < k and self.arr[k] == self.arr[k + 1]:
                        k -= 1

        return ans

    def print_arr(self) -> None:
        print(self.arr, sep=" ")
        print()


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    solution = Solution(arr)
    solution.print_arr()
    print(solution._3_sum_brute())
    print(solution._3_sum_better())
    print(solution._3_sum_optimal())
