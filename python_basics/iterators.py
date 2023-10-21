a = ["Hey", "bro", "you", "r", "awesome"]

# Traverse the list using loop
for i in a:
    print(i)

# Use iterator to traverse the list
itr = iter(a)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr))
# print(dir(itr))

# Reverse iterator
itr = reversed(a)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr))
