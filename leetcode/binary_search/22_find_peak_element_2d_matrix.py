"""
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
"""

from typing import List


class Solution:
    def __valid(self, mat: List[List[int]], r: int, c: int) -> bool:
        """
        Helper function to check if mat[r][c] is a peak element.
        A peak element is greater than all of its adjacent neighbors (top, bottom, left, right).
        """
        val: int = mat[r][c]
        n: int = len(mat)
        m: int = len(mat[0])

        # Check all four possible adjacent neighbors
        if (
            (r - 1 >= 0 and mat[r - 1][c] > val)
            or (r + 1 < n and mat[r + 1][c] > val)
            or (c - 1 >= 0 and mat[r][c - 1] > val)
            or (c + 1 < m and mat[r][c + 1] > val)
        ):
            return False

        return True

    def __brute(self, mat: List[List[int]]) -> List[int]:
        """
        Brute-force approach to find a peak element by checking each element in the matrix.
        """
        n: int = len(mat)
        m: int = len(mat[0])

        for r in range(n):
            for c in range(m):
                if self.__valid(mat, r, c):
                    return [r, c]
        return []

    def __better(self, mat: List[List[int]]) -> List[int]:
        """
        Better brute-force approach by iterating and keeping track of the maximum element found.
        """
        n: int = len(mat)
        m: int = len(mat[0])
        mx: int = float("-inf")
        ans: List[int] = [-1, -1]

        # Iterate through each element and update the maximum found so far
        for r in range(n):
            for c in range(m):
                if mat[r][c] > mx:
                    mx = mat[r][c]
                    ans[0] = r
                    ans[1] = c

        return ans

    def __max_ele(self, mat, n, m, mid) -> int:
        """
        Helper function to find the row index of the maximum element in the mid column.
        """
        mx: int = -1
        ind: int = -1

        # Iterate through each row in the given column (mid) and find the maximum element
        for r in range(n):
            if mat[r][mid] > mx:
                mx = mat[r][mid]
                ind = r

        return ind

    def __optimal(self, mat: List[List[int]]) -> List[int]:
        """
        Optimized approach using binary search to find a peak element.
        """
        n: int = len(mat)
        m: int = len(mat[0])
        lo, hi = 0, m - 1

        while lo <= hi:
            mid: int = (lo + hi) // 2

            # Find the row index of the maximum element in the mid column
            row: int = self.__max_ele(mat, n, m, mid)

            # Determine the values of the left and right adjacent elements
            left: int = mat[row][mid - 1] if mid - 1 >= 0 else -1
            right: int = mat[row][mid + 1] if mid + 1 < m else -1

            # Check if mat[row][mid] is a peak element
            if left < mat[row][mid] > right:
                return [row, mid]
            elif mat[row][mid] < left:
                hi = mid - 1
            else:
                lo = mid + 1

        return [-1, -1]

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """
        Main function to find a peak element in the matrix using the optimal approach.
        """
        # Uncomment the desired approach to find the peak element
        # return self.__brute(mat)
        # return self.__better(mat)
        return self.__optimal(mat)


if __name__ == "__main__":
    matrix: List[List[int]] = [[10, 20, 15], [21, 30, 14], [7, 16, 32]]
    solution: Solution = Solution()
    result: List[int] = solution.findPeakGrid(mat=matrix)
    print(result)
