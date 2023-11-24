"""Majority elements that appears more than n//3"""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def majority_element_optimal(self) -> list[int]:
        cnt1: int = 0
        cnt2: int = 0
        ele1: int = -1234567
        ele2: int = -1234567

        for i in range(len(self.arr)):
            if cnt1 == 0 and ele2 != self.arr[i]:
                cnt1 = 1
                ele1 = self.arr[i]
            elif cnt2 == 0 and ele1 != self.arr[i]:
                cnt2 = 1
                ele2 = self.arr[i]
            elif self.arr[i] == ele1:
                cnt1 += 1
            elif self.arr[i] == ele2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        ans: list[int] = []
        cnt1 = 0
        cnt2 = 0

        for i in range(len(self.arr)):
            if ele1 == self.arr[i]:
                cnt1 += 1
            if ele2 == self.arr[i]:
                cnt2 += 1

        mini: int = len(self.arr) // 3 + 1
        if cnt1 >= mini:
            ans.append(ele1)
        if cnt2 >= mini:
            ans.append(ele2)

        return ans

    def majority_element_better(self) -> list[int]:
        hsh = {}
        ans: list[int] = []
        n: int = len(self.arr)
        majority: int = n // 3
        for i in range(n):
            if self.arr[i] in hsh:
                hsh[self.arr[i]] += 1
            else:
                hsh[self.arr[i]] = 1

            freq = hsh.get(self.arr[i], 0)
            if freq > majority:
                ans.append(self.arr[i])

        return ans

    def majority_element_brute_force(self) -> list[int]:
        ans: list[int] = []
        n: int = len(self.arr)
        majority: int = n // 3
        for i in range(n):
            ct: int = 1
            for j in range(n):
                if i != j:
                    if self.arr[i] == self.arr[j]:
                        ct += 1
            if ct > majority and self.arr[i] not in ans:
                ans.append(self.arr[i])
            if len(ans) == majority:
                break

        return ans

    def print_arr(self) -> None:
        print(self.arr, sep=" ", end="")
        print()


if __name__ == "__main__":
    arr = [1, 1, 1, 3, 3, 2, 2, 2]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.majority_element_brute_force())
    print(solution.majority_element_better())
    print(solution.majority_element_optimal())
