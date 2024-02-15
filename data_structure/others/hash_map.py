def get_hash(key: str):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100


a = ["kamrul", "Hasan", "Python", "Programmer"]

for item in a:
    print(f"index of {item} is: ", get_hash(item))


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key: str, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key: str):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key: str):
        h = self.get_hash(key)
        self.arr[h] = None


ht = HashTable()
# set value by key
ht["Kamrul"] = "Python"
ht["Hasan"] = "Programmer"

print(ht["Kamrul"])
print(ht["Hasan"])

print(ht["Python"])

# Delete item
del ht["Kamrul"]

print(ht["Kamrul"])
