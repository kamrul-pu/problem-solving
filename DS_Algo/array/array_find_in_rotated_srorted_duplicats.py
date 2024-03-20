""" Find element in the rotated sorted array."""


class Solution:
    def __init__(self, arr: list[int] = []) -> None:
        self.arr: list[int] = arr
        self.n: int = len(self.arr)

    def find_element(self, target: int) -> bool:
        low: int = 0
        high: int = self.n - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == target:
                return True

            if self.arr[low] == self.arr[mid] == self.arr[high]:
                low += 1
                high -= 1
                continue
            # find the sorted portion
            if self.arr[low] <= target:
                # left part is sorted
                if self.arr[low] <= target and target <= self.arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # right part is sorted
                if self.arr[mid] <= target and target <= self.arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 3, 3, 4, 5, 6]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.find_element(3))
