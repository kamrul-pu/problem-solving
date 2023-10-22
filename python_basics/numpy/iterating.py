"""Iterating numpy array."""

import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)

for row in a:
    print(row)

for row in a:
    for col in row:
        print(col)

for cell in a.flatten():
    print(cell)

# using nd iter

# Iterrate over column
for x in np.nditer(a, order="C"):
    print(x)

# Iterating over row

for c in np.nditer(a, order="F"):
    print(c)

# passing flags

for x in np.nditer(a, order="F", flags=["external_loop"]):
    print(x)

for x in np.nditer(a, op_flags=["readwrite"]):
    x[...] = x * x

# Iter two array at the same time

a = np.arange(12).reshape(3, 4)
b = np.arange(3, 15, 4).reshape(3, 1)

for x, y in np.nditer([a, b]):
    print(x, y)
