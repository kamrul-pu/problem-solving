"""Find Median of row wise sorted matrix."""

from typing import List


class Solution:
    def __upper(self, arr: List[int], x: int) -> int:
        """
        Helper function to find the index of the first element greater than x in the sorted array arr.
        Uses binary search for efficiency.
        """
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] <= x:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    def __count(self, matrix: List[List[int]], mid: int) -> int:
        """
        Function to count the number of elements less than or equal to mid across all rows of the matrix.
        """
        count = 0
        for row in matrix:
            count += self.__upper(row, mid)
        return count

    def median(self, matrix: List[List[int]], R: int, C: int) -> int:
        """
        Function to find the median of the row-wise sorted matrix using binary search on possible median values.
        """
        req = (
            R * C
        ) // 2  # The required number of elements less than or equal to the median
        lo, hi = float("inf"), float("-inf")

        # Find the minimum and maximum values in the matrix
        for row in matrix:
            lo = min(lo, min(row))
            hi = max(hi, max(row))

        # Binary search for the median value
        while lo <= hi:
            mid = (lo + hi) // 2
            count = self.__count(matrix, mid)

            if count <= req:
                lo = (
                    mid + 1
                )  # If count of elements <= mid is less than required, search in the higher half
            else:
                hi = (
                    mid - 1
                )  # If count of elements <= mid is more than required, search in the lower half

        return lo  # lo will contain the median value after binary search


if __name__ == "__main__":
    matrix: List[List[int]] = [
        [1, 5, 7, 9, 11],
        [2, 3, 4, 5, 10],
        [9, 10, 12, 14, 16],
    ]
    R: int = len(matrix)  # Number of rows in the matrix
    C: int = len(matrix[0])  # Number of columns in the matrix
    solution: Solution = Solution()
    print(solution.median(matrix, R, C))
