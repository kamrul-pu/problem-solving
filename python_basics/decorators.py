"""Decorators in python."""
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " miliseconds")
        return result

    return wrapper


@time_it
def calc_square(numbers: list[int]):
    result = []
    for number in numbers:
        result.append(number * number)

    return result


@time_it
def calc_cube(numbers: list[int]):
    result = []
    for number in numbers:
        result.append(number * number * number)

    return result


array = range(1, 1000)
out_score = calc_square(numbers=array)

out_cube = calc_cube(numbers=array)
