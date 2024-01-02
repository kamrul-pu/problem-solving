"""Use yield instead of return."""


def simple_generator() -> int:
    yield 1
    yield 2
    yield 3


def next_square() -> int:
    i: int = 1

    while True:
        yield i * i
        i += 1


if __name__ == "__main__":
    for value in simple_generator():
        print(value)

    # x is a generator object
    x = simple_generator()

    # Iterating over the generator object using next

    # In Python 3, __next__()
    print(next(x))
    print(next(x))
    print(next(x))

    for num in next_square():
        if num > 100:
            break
        print(num)
