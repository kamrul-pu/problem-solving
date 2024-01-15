"""Transpose of a matrix."""
import numpy as np

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(matrix)
    print("\n")
    print(np.transpose(matrix))
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(matrix.T)
