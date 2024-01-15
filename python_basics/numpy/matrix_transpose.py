"""Transpose of a matrix."""
import numpy as np
import math

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(matrix)
    print("\n")
    print(np.transpose(matrix))
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(matrix.T)
    matrix: list[list[int]] = [
        [7, 8, 9],
        [6, 1, 2],
        [5, 4, 3],
    ]
    n: int = len(matrix)
    normal: int = 0
    for i in range(n):
        for j in range(n):
            normal += matrix[i][j] * matrix[i][j]

    normal = int(math.sqrt(normal))
    print(normal)
    trace: int = 0
    for i in range(n):
        trace += matrix[i][i]
    print(trace)
