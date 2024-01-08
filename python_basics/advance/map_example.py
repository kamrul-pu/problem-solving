"""Python Map functions."""


def addition(n):
    return n + n


if __name__ == "__main__":
    numbers: list[int] = [1, 2, 3, 4]
    result = map(addition, numbers)
    print(list(result))
    result = map(lambda x: x * x, numbers)
    print(list(result))
    numbers_1: list[int] = [1, 2, 3]
    numbers_2: list[int] = [4, 5, 6]
    result = map(lambda x, y: x + y, numbers_1, numbers_2)
    print(list(result))

    # List of strings
    l = ["sat", "bat", "cat", "mat"]

    # map() can listify the list of strings individually
    test = list(map(list, l))
    print(test)
