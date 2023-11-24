""" Find element in the rotated sorted array."""


class Solution:
    def __init__(self, arr: list[int] = []) -> None:
        self.arr: list[int] = arr
        self.n: int = len(self.arr)

    def find_min(self) -> int:
        mn: int = 1234567890
        left: int = 0
        right: int = self.n - 1
        while left <= right:
            mn = min(self.arr[left], self.arr[right], mn)
            left += 1
            right -= 1

        return mn

    def find_min_optimal(self) -> int:
        mn: int = 1234567890
        low: int = 0
        high: int = self.n - 1
        while low <= high:
            # identify the sorted portion
            mid: int = (low + high) // 2
            # add more optimization, if low less than high then it is already sorted
            # we can break the loop
            if self.arr[low] <= self.arr[high]:
                mn = min(mn, self.arr[low])
                break

            if self.arr[low] <= self.arr[mid]:
                # left portion is sorted may contains answer, update mn
                mn = min(mn, self.arr[low])
                # eleminate the left sorted area
                low = mid + 1
            else:
                # right part is sorted
                mn = min(mn, self.arr[mid])
                high = mid - 1

        return mn

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 3, 3, 4, 5, 6]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.find_min())
    print(soltuion.find_min_optimal())
