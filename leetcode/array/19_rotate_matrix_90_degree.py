from typing import List


class Solution:
    def __brute(self, matrix: List[List[int]]) -> None:
        """
        Brute force approach to rotate the matrix by 90 degrees clockwise.
        Uses an additional matrix 'ans' to store rotated values temporarily.
        """
        n: int = len(matrix)
        ans: List[List[int]] = [[0 for _ in range(n)] for _ in range(n)]

        # Iterate through each element in the matrix
        for i in range(n):
            for j in range(n):
                # Place the rotated value in 'ans' matrix
                ans[j][n - i - 1] = matrix[i][j]

        # Copy values from 'ans' matrix back to original matrix
        for i in range(n):
            for j in range(n):
                matrix[i][j] = ans[i][j]

    def __reverse(self, matrix: List[List[int]], i: int) -> None:
        """
        Helper function to reverse elements in a row 'i' of the matrix.
        """
        n: int = len(matrix)
        l: int = 0
        r: int = n - 1
        while l < r:
            # Swap elements symmetrically across the row
            matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1

    def __optimal(self, matrix: List[List[int]]) -> None:
        """
        Optimal approach to rotate the matrix by 90 degrees clockwise in place.
        Transpose the matrix and then reverse each row.
        """
        n: int = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n - 1):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row of the matrix
        for i in range(n):
            self.__reverse(matrix, i)

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the matrix by 90 degrees clockwise in place.

        Args:
        - matrix: The n x n matrix to be rotated (modified in place).
        """
        # Choose the optimal approach to rotate the matrix
        self.__optimal(matrix=matrix)
        # Alternatively, you can switch to self.__brute(matrix=matrix) for a less efficient approach.


if __name__ == "__main__":
    # Example usage
    matrix: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution: Solution = Solution()
    solution.rotate(matrix=matrix)
    print(matrix)  # Output the rotated matrix
