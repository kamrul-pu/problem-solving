"""Number of available subarray with the given xor k"""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def repeating_missing_brute(self, n: int) -> list[int]:
        # TC = O(n^2)
        # Space O(1)
        repeating = -1
        missing = -1
        for i in range(1, n + 1):
            cnt: int = 0
            for j in range(n):
                if self.arr[j] == i:
                    cnt += 1
            if cnt == 2:
                repeating = i
            elif cnt == 0:
                missing = i
            if missing != -1 and repeating != -1:
                break

        return [repeating, missing]

    def repating_missing_better(self, n: int) -> list[int]:
        # TC = O(2n) Space O(n)
        hsh: list[int] = [0] * (n + 1)
        for i in range(n):
            hsh[self.arr[i]] += 1

        repeating: int = -1
        missing: int = -1
        for i in range(1, n + 1):
            if hsh[i] == 2:
                repeating = i
            elif hsh[i] == 0:
                missing = i

            if missing != -1 and repeating != -1:
                break

        return [repeating, missing]

    def repeating_missing_optimal_1(self, n: int) -> list[int]:
        # s - sn =x-y
        # s^2 - s^2n
        sn: int = (n * (n + 1)) // 2  # sum of n natural numbers
        s2n: int = (n * (n + 1) * (2 * n + 1)) // 6
        s: int = 0
        s2: int = 0
        for i in range(n):
            s += self.arr[i]
            s2 += self.arr[i] * self.arr[i]
        x_y: int = s - sn  # x-y
        x2_y2: int = s2 - s2n  # x^2-y^2
        x2_y2 = x2_y2 // x_y
        x: int = (x_y + x2_y2) // 2
        y: int = x - x_y

        return [x, y]

    def repeating_missing_optimal_2(self, n: int) -> list[int]:
        xr: int = 0
        for i in range(n):
            xr ^= self.arr[i]
            xr ^= i + 1
        number: int = xr & ~(xr - 1)
        zero: int = 0
        one: int = 0
        for i in range(n):
            # part of one
            if self.arr[i] & number != 0:
                one ^= self.arr[i]
            # part of zero
            else:
                zero ^= self.arr[i]

        for i in range(1, n + 1):
            # part of one
            if i & number != 0:
                one ^= i
            # part of zero
            else:
                zero ^= i
        cnt: int = 0
        for i in range(n):
            if self.arr[i] == zero:
                cnt += 1

        if cnt == 2:
            return [zero, one]
        return [one, zero]

    def print_arr(self) -> None:
        print("array :", self.arr1, sep=" ")
        print()


if __name__ == "__main__":
    n: int = 6
    arr = [4, 3, 6, 2, 1, 1]
    solution = Solution(arr)
    print(solution.repeating_missing_brute(n))
    print(solution.repating_missing_better(n))
    print(solution.repeating_missing_optimal_1(n))
    print(solution.repeating_missing_optimal_2(n))
