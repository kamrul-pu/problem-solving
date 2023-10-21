import os

file_path = os.path.realpath("data_structure/poem.txt")
print(file_path)

count_dict = dict()

with open(file=file_path, mode="r") as f:
    for line in f:
        words = line.split(" ")
        for word in words:
            word = word.replace("\n", "")
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 1

print(count_dict)
