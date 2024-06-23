"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Determine the dimensions of the matrix
        n: int = len(matrix)  # Number of rows
        m: int = len(matrix[0])  # Number of columns

        # Initialize boundaries for the spiral traversal
        left, right, top, bottom = 0, m - 1, 0, n - 1

        # Initialize list to store the elements in spiral order
        ans: List[int] = []

        # Traverse the matrix in spiral order
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom along the rightmost column
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Check if there are remaining rows to traverse
            if top <= bottom:
                # Traverse from right to left along the bottom row
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # Check if there are remaining columns to traverse
            if left <= right:
                # Traverse from bottom to top along the leftmost column
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans


if __name__ == "__main__":
    # Example usage
    matrix: List[List[int]] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    solution: Solution = Solution()
    print(solution.spiralOrder(matrix=matrix))
