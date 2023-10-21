basket = {1, 2, 3, 44, 5, 5, 6, 3}
print(type(basket))
print(basket)

# By default sets element can be add or remove set is mutable

# frozen set is immutable
fs = frozenset(basket)
print(fs)

# Declare two set
x = {"a", "b", "c"}
y = {"a", "h", "g"}

# Union two set
xy = x | y
print(xy)

# Intersection
x_intersection_y = x & y
print(x_intersection_y)

# Difference
x_diif_y = x - y
print(x_diif_y)
y_diff_x = y - x
print(y_diff_x)

# Check if x is subset of y
print(x < y)
# Check if y is subset of x
print(x > y)
