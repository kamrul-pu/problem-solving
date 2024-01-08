"""Array Creating using numpy."""

import numpy as np

if __name__ == "__main__":
    # Creating a 3X4 array with all zeros
    c = np.zeros((3, 4), dtype="int8")
    print("An array initialized with all zeros:\n", c)

    # Create a constant value array of complex type
    d = np.full((3, 3), 6, dtype="complex")
    print("An array initialized with all 6s.Array type is complex:\n", d)
    e = np.random.random((2, 2))
    print("A random array:\n", e)
    # Create a sequence of integers from 0 to 30 with steps of 5
    f = np.arange(0, 31, 5)
    print("A sequential array with steps of 5:\n", f)
    # Create a sequence of 10 values in range 0 to 5
    g = np.linspace(0, 5, 10)
    print("A sequential array with 10 values between 0 and 5:\n", g)

    # Reshaping 3X4 array to 2X2X3 array
    arr = np.array([[1, 2, 3, 4], [5, 2, 4, 2], [1, 2, 0, 1]])
    new_arr = arr.reshape(2, 2, 3)
    print("Original array:\n", arr)
    print("-----------------------")
    print("Reshaped array:\n", new_arr)
    flat_arr = arr.flatten()
    print("Flattened array:\n", flat_arr)

    a = np.array([[1, 4, 2], [3, 4, 6], [0, -1, 5]])

    # sorted array
    print("Array elements in sorted order:\n", np.sort(a, axis=None))

    # sort array row-wise
    print("Row-wise sorted array:\n", np.sort(a, axis=1))

    # specify sort algorithm
    print(
        "Column wise sort by applying merge-sort:\n",
        np.sort(a, axis=0, kind="mergesort"),
    )

    # Example to show sorting of structured array
    # set alias names for dtypes
    dtypes = [("name", "S10"), ("grad_year", int), ("cgpa", float)]

    # Values to be put in array
    values = [
        ("Hrithik", 2009, 8.5),
        ("Ajay", 2008, 8.7),
        ("Pankaj", 2008, 7.9),
        ("Aakash", 2009, 9.0),
    ]

    # Creating array
    arr = np.array(values, dtype=dtypes)
    print("\nArray sorted by names:\n", np.sort(arr, order="name"))

    print(
        "Array sorted by graduation year and then cgpa:\n",
        np.sort(arr, order=["grad_year", "cgpa"]),
    )

    a = np.array([[1, 2, 3], [4, 5, 6]])
    Sqrt = np.sqrt(a)
    print("Square root of array 1 element:\n", Sqrt)

    trans_arr = a.T
    print("Transpose of array", trans_arr)
