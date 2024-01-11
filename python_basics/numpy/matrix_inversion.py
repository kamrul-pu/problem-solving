"""Inverse a matrix using numpy."""

import numpy as np

if __name__ == "__main__":
    arr = np.array([[1, 2], [5, 6]])
    inverse_arr = np.linalg.inv(arr)
    print("inverse array", inverse_arr)

    # inverse of 3X3 matrix
    arr = np.array([[1, 2, 3], [4, 9, 6], [7, 8, 9]])

    inverse_array = np.linalg.inv(arr)
    print("Inverse array is ")
    print(inverse_array)

    # Inverses of several matrices can
    # be computed at once
    A = np.array([[[1.0, 2.0], [3.0, 4.0]], [[1, 3], [3, 5]]])
    print(np.linalg.inv(A))
