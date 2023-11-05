"""Majority elements means a number appered more then n/2 times."""


class Solution:
    def __init__(self, arr) -> None:
        self.arr = arr

    def majority_element1(self) -> int:
        # Brute Force solution O(n^2) S O(1)
        for i in range(len(self.arr)):
            ct: int = 0
            for j in range(len(self.arr)):
                if self.arr[i] == self.arr[j]:
                    ct += 1

            if ct > len(self.arr) // 2:
                return self.arr[i]
        return -1

    def majority_element2(self) -> int:
        # Time O(nlog) Space O(n)
        count = {}
        for x in self.arr:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        for k, v in count.items():
            if v > len(self.arr) // 2:
                return k
        return -1

    def majority_element3(self):
        # Usng moore's voting algorithm
        ct: int = 0
        ele: int = self.arr[0]
        for x in self.arr:
            if ct == 0:
                ele = x
                ct += 1
            elif x == ele:
                ct += 1
            else:
                ct -= 1
        ct1: int = 0
        for x in self.arr:
            if x == ele:
                ct1 += 1

        if ct1 > len(self.arr) // 2:
            return ele
        return -1

    def print_arr(self):
        print(self.arr)


if __name__ == "__main__":
    arr = [2, 2, 3, 3, 1, 2, 2]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.majority_element3())
