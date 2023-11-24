"""Number of sub array with the sum k Brute force and optimal solution"""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def number_of_subarray(self, k: int) -> int:
        # Brute force solution
        count: int = 0
        n = len(self.arr)
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += self.arr[j]
                if sum == k:
                    count += 1

        return count

    def number_of_subarray_optimal(self, k) -> int:
        # optimal solution using dict
        preSum: int = 0
        count: int = 0
        pf = dict()
        pf[0] = 1

        for i in range(len(self.arr)):
            preSum += self.arr[i]
            remove: int = preSum - k
            if remove in pf:
                count += pf[remove]
            if preSum in pf:
                pf[preSum] += 1
            else:
                pf[preSum] = 1

        return count

    def print_arr(self):
        print(self.arr, sep=" ")
        print()


if __name__ == "__main__":
    arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.number_of_subarray(3))
    print(solution.number_of_subarray_optimal(3))
