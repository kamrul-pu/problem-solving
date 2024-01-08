"""Accessing numpy array. indexing array."""

import numpy as np

if __name__ == "__main__":
    arr: list[int] = np.array(
        [[-1, 2, 0, 4], [4, -0.5, 6, 0], [2.6, 0, 7, 8], [3, -7, 4, 2.0]]
    )
    print("Initial Array: \n", arr)
    sliced_arr = arr[:2, ::2]
    print("Array with first 2 rows and alternate columns (0 and 2):\n", sliced_arr)
    index_arr = arr[[1, 1, 0, 3], [3, 2, 1, 0]]
    print("Elements at indeices (1,3),(1,2),(0,1),(3,0):\n", index_arr)

    # Array basics operations
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[4, 3], [2, 1]])
    # Adding 1 to every element
    print("Adding 1 to every element:\n", a + 1)
    # Subtracting 2 from each element
    print("subtracting 2 from each element: ", b - 2)

    # Sum of array element
    # performing Unary operations
    print("Sum of all array element: ", a.sum())
    # Adding two arrays
    # Perfroming Binary operations
    print("Array Sum: ", a + b)
    # Printing type of arr object
    print("Array is of type: ", type(arr))

    # Printing array dimensions (axes)
    print("No. of dimensions: ", arr.ndim)

    # Printing shape of array
    print("Shape of array: ", arr.shape)

    # Printing size (total number of elements) of array
    print("Size of array: ", arr.size)

    # Printing type of elements in array
    print("Array stores elements of type: ", arr.dtype)
