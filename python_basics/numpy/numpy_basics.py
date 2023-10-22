import numpy as np

a = np.array([5, 6, 8])
print(a[0])

a = np.array([[1, 2], [3, 4]])
print(a.ndim)

print(a.itemsize)

print(a.dtype)

print(a.size)

print(a.shape)

a = np.zeros((3, 4))
print(a)

a = np.ones((3, 4))
print(a)

a = np.arange(10)

print(a)

# generate linspace from 1-5 and 10 points
ls = np.linspace(1, 5, 10)
print(ls)

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a.shape)  # row=3 col 2
a = a.reshape(2, 3)  # row=2 col=3
print(a.shape)
print(a)
# Flatten the array

# make the 2 d array to 1 d array
a = a.ravel()
print(a)

a = a.reshape(3, 2)

print(a)
print(a.min())
print(a.max())
print(a.sum())

print(a.sum(axis=0))  # Column wise

print(a.sum(axis=1))  # Axis =1 row wise

print(np.sqrt(a))

a = np.array(np.arange(1, 10).reshape(3, 3))
print(a)
