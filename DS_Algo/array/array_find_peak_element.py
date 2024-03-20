""" Find peak Element in the sorted array."""


class Solution:
    def __init__(self, arr: list[int] = []) -> None:
        self.arr: list[int] = arr
        self.n: int = len(self.arr)

    def find_peak(self) -> int:
        ans: int = -1
        for i in range(self.n):
            if i == 0 and self.arr[i] > self.arr[i + 1]:
                return self.arr[i]
            elif i == self.n - 1 and self.arr[i] > self.arr[i - 1]:
                return self.arr[i]
            elif self.arr[i - 1] < self.arr[i] and self.arr[i] > self.arr[i + 1]:
                return self.arr[i]
        return ans

    def find_peak_optimal(self) -> int:
        # if one element return that
        if self.n == 1:
            return self.arr[0]
        # check the first element if it is greater then next
        if self.arr[0] > self.arr[1]:
            return self.arr[0]
        # check the last element is it greater than second last
        if self.arr[self.n - 1] > self.arr[self.n - 2]:
            return self.arr[self.n - 1]
        # perform binary search by elaminating first and last element
        low: int = 1
        high: int = self.n - 2
        while low <= high:
            mid: int = (low + high) // 2

            if self.arr[mid - 1] < self.arr[mid] and self.arr[mid] > self.arr[mid + 1]:
                return self.arr[mid]
            # elif self.arr[mid - 1] < self.arr[mid] < self.arr[mid + 1]:
            # elif (
            #     self.arr[mid - 1] > self.arr[mid] and self.arr[mid] < self.arr[mid + 1]
            # ):
            elif self.arr[mid] > self.arr[mid - 1]:
                # increasing order
                low = mid + 1
            else:
                # decreasing order
                high = mid - 1

        return -1

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
    # arr = [1, 2, 1, 3, 5, 6, 4]
    arr = [1, 2, 3, 4, 5]
    arr = [5, 4, 2, 3, 1]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.find_peak())
    print(soltuion.find_peak_optimal())
