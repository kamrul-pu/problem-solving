"""Array 4 Sum Solution."""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def sum_4_brute_force(self, target: int) -> list[list[int]]:
        # With duplicate result
        ans: list[list[int]] = []
        n = len(self.arr)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if (
                            self.arr[i] + self.arr[j] + self.arr[k] + self.arr[l]
                        ) == target:
                            temp = [self.arr[i], self.arr[j], self.arr[k], self.arr[l]]
                            ans.append(temp)

        return ans

    def sum_4_brute_force1(self, target: int) -> {int}:
        # without duplicate
        ans: {} = set()
        n = len(self.arr)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if (
                            self.arr[i] + self.arr[j] + self.arr[k] + self.arr[l]
                        ) == target:
                            temp = [self.arr[i], self.arr[j], self.arr[k], self.arr[l]]
                            temp.sort()
                            ans.add(tuple(temp))

        return ans

    def sum_4_better(self, target: int) -> {int}:
        # without duplicate
        ans: {} = set()
        n = len(self.arr)
        for i in range(n):
            for j in range(i + 1, n):
                temp = set()
                for k in range(j + 1, n):
                    fourth = target - (self.arr[i] + self.arr[j] + self.arr[k])

                    if fourth in temp:
                        combination = [self.arr[i], self.arr[j], self.arr[k], fourth]
                        combination.sort()
                        ans.add(tuple(combination))
                    temp.add(self.arr[k])

        return ans

    def sum_4_optimal(self, target: int) -> list[list[int]]:
        # first sort the array
        self.arr.sort()
        ans: list[list[int]] = []
        n = len(self.arr)
        for i in range(n):
            if i > 0 and self.arr[i] == self.arr[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and self.arr[j] == self.arr[j - 1]:
                    continue
                # declare 2 pointer
                k: int = j + 1
                l: int = n - 1
                while k < l:
                    sum: int = self.arr[i] + self.arr[j] + self.arr[k] + self.arr[l]
                    if sum > target:
                        l -= 1
                    elif sum < target:
                        k += 1
                    else:
                        ans.append([self.arr[i], self.arr[j], self.arr[k], self.arr[l]])
                        k += 1
                        l -= 1
                        # increase k pointer till they are same
                        while k < l and self.arr[k] == self.arr[k - 1]:
                            k += 1
                        # decrease l pointer while they are same
                        while k < l and self.arr[l] == self.arr[l + 1]:
                            l -= 1
        return ans

    def print_arr(self) -> None:
        print(self.arr, sep=" ")
        print()


if __name__ == "__main__":
    arr = [1, 0, -1, 0, -2, 2]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.sum_4_brute_force(0))
    print(solution.sum_4_brute_force1(0))
    print(solution.sum_4_better(0))
    print(solution.sum_4_optimal(0))
