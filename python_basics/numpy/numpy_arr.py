"""Python Program for creating arrays using numpy."""

import numpy as np

if __name__ == "__main__":
    # Creating a rank 1 Array
    arr = np.array([1, 2, 3])
    print("Array with rank 1: \n", arr)
    # array with rank 2
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print("Array with rank 2: \n", arr)
    # Creating an array from tuple.
    arr = np.array((1, 2, 3))
    print("\nArray created using passed tuple:\n", arr)
