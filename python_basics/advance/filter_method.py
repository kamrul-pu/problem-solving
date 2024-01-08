"""Python filter function."""


def fun(variable) -> bool:
    letters: list[chr] = ["a", "e", "i", "o", "u"]
    return variable in letters


# sequence
sequence = ["g", "e", "e", "j", "k", "s", "p", "r"]

filtered = filter(fun, sequence)
print("the filtered letters are:")
for s in filtered:
    print(s)

# filter with lambda
seq: list[int] = [0, 1, 2, 3, 4, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result: list[int] = filter(lambda x: x % 2 == 0, seq)
print(list(result))


def is_multiple_of_3(num) -> bool:
    return num % 3 == 0


numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result: list[int] = list(filter(lambda x: is_multiple_of_3(x), numbers))
print(result)
