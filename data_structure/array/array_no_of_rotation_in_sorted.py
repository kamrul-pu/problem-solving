""" Find element in the rotated sorted array."""


class Solution:
    def __init__(self, arr: list[int] = []) -> None:
        self.arr: list[int] = arr
        self.n: int = len(self.arr)

    def find_rotation(self) -> int:
        mn: int = 1234567890
        left: int = 0
        right: int = self.n - 1
        rotation: int = 0
        while left <= right:
            if self.arr[left] < self.arr[right] and self.arr[left] < mn:
                mn = self.arr[left]
                rotation = left
            else:
                if self.arr[right] < mn:
                    mn = self.arr[right]
                    rotation = right
            left += 1
            right -= 1

        return rotation

    def find_rotation_optimal(self) -> int:
        rotation: int = 0
        mn: int = 1234567890
        low: int = 0
        high: int = self.n - 1
        while low <= high:
            mid: int = (low + high) // 2
            if self.arr[low] <= self.arr[high]:
                if self.arr[low] < mn:
                    # rotation = low
                    return low
                return rotation

            if self.arr[low] <= self.arr[mid]:
                # left half is sorted
                if self.arr[low] < mn:
                    mn = self.arr[low]
                    rotation = low
                low = mid + 1
            else:
                # right half is sorted
                if self.arr[mid] < mn:
                    mn = self.arr[mid]
                    rotation = mid
                high = mid - 1

        return rotation

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 3, 3, 4, 5, 6]
    arr = [5, 6, 1, 2, 3, 4]
    soltuion = Solution(arr)
    soltuion.print_arr()
    print(soltuion.find_rotation())
    print(soltuion.find_rotation_optimal())
