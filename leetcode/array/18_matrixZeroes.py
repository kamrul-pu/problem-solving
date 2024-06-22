from typing import List


class Solution:
    def __mark_row(self, i: int, matrix: List[List[int]]) -> None:
        """Helper function to mark all elements in row i as '-inf'."""
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                matrix[i][j] = float("-inf")

    def __mark_col(self, j: int, matrix: List[List[int]]) -> None:
        """Helper function to mark all elements in column j as '-inf'."""
        for i in range(len(matrix)):
            if matrix[i][j] != 0:
                matrix[i][j] = float("-inf")

    def __brute(self, matrix: List[List[int]]) -> None:
        """Brute force approach to set zeroes."""
        n: int = len(matrix)
        m: int = len(matrix[0])
        # Mark rows and columns to be zeroed
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    self.__mark_row(i, matrix)
                    self.__mark_col(j, matrix)

        # Convert '-inf' marked cells back to 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == float("-inf"):
                    matrix[i][j] = 0

    def __better(self, matrix: List[List[int]]) -> None:
        """Better approach using additional space to mark rows and columns."""
        n: int = len(matrix)
        m: int = len(matrix[0])
        cols: List[bool] = [False] * m  # To mark columns that should be zeroed
        rows: List[bool] = [False] * n  # To mark rows that should be zeroed
        # Mark rows and columns to be zeroed
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    cols[j] = True
                    rows[i] = True

        # Set entire rows and columns to zero based on the marks
        for i in range(n):
            for j in range(m):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

    def __optimal(self, matrix: List[List[int]]) -> None:
        """Optimal approach using constant space."""
        n: int = len(matrix)
        m: int = len(matrix[0])
        col0: int = 1  # Variable to track if the first column needs to be zeroed
        # Step 1: Use the first row and first column as markers
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Marking the first element of the row
                    if j != 0:
                        matrix[0][j] = 0  # Marking the first element of the column
                    else:
                        col0 = 0  # Set col0 to 0 if the first column itself needs to be zeroed

        # Step 2: Zero out cells based on the markers in the first row and column
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Handle the first row and first column separately
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0  # Zero out the entire first row

        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0  # Zero out the entire first column

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Main function to set zeroes in the matrix.

        Args:
        - matrix: The matrix where zeroes need to be set (modified in place).
        """
        # Choose the optimal approach to set zeroes
        self.__optimal(matrix=matrix)
        # Alternatively, you can switch to other methods like self.__brute(matrix=matrix)
        # or self.__better(matrix=matrix) for different implementations.


# Example usage:
matrix: List[List[int]] = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
]
solution: Solution = Solution()
solution.setZeroes(matrix)
print(matrix)  # Output the modified matrix after setting zeroes
