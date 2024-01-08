"""Reduce functions of python."""
import itertools

import functools


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


if __name__ == "__main__":
    # python code to demonstrate summation
    # using reduce() and accumulate()
    lis: list[int] = [1, 3, 4, 10, 4]

    print("The summation of list using accumulate is: ", end="")
    print(list(itertools.accumulate(lis, lambda x, y: x + y)))

    print("The summation of list using reduce is: ", end="")
    print(functools.reduce(lambda x, y: x + y, lis))

    # Note that the initializer, when not None, is used as the first value instead of the first value from iterable , and after the whole iterable.
    tup = (2, 1, 0, 2, 2, 0, 0, 2)
    print(reduce(lambda x, y: x + y, tup, 6))
