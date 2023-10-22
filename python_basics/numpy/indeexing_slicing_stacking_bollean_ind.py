import numpy as np

a = np.array([4, 5, 6])
a[0:2]

a = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])
# row 1 col 2
print(a[1, 2])
# row 0-1, col=2
print(a[0:2, 2])

a = np.arange(6).reshape(3, 2)
b = np.arange(6, 12).reshape(3, 2)

# vertical stack

ab_vertical = np.vstack((a, b))
print(ab_vertical)

# Horizontal stack
ab_horizontal = np.hstack((a, b))
print(ab_horizontal)

a = np.arange(30).reshape(2, 15)

# Horizontal split
hs = np.hsplit(a, 3)
print(hs)

# Vertical split
vs = np.vsplit(a, 2)
print(vs)

# Boolean Indexing
a = np.arange(12).reshape(3, 4)

# Create boolean indexing
b = a > 4  # if element is greater than 4 fill True else False
print(b)
# if b is true then get element
c = a[b]
print(c)

# if true then fill with -1

d = a[b] = -1
print(d)
