"""Matrix Operations using numpy."""

import numpy as np

if __name__ == "__main__":
    X = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    Y = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]
    # Add matrix
    result = np.array(X) + np.array(Y)
    print(result)
    print(type(result))
    # Subtract matrix
    result = np.array(Y) - np.array(X)
    print(result)
    print(np.sum(X, axis=0))
    print(np.sum(X, axis=1))
    print(np.array(X).T)
    # Multiplication
    result = np.array(X) * np.array(Y)
    print(result)
