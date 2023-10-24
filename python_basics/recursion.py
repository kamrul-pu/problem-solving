"""Recursion in python."""

import time
import sys

sys.setrecursionlimit(100000)


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " miliseconds")
        return result

    return wrapper


# find sum using iterative approach
@time_it
def find_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i

    return sum


# find sum using recursive approach
def find_sum_recursive(n):
    if n == 1:
        return 1
    return n + find_sum_recursive(n - 1)


if __name__ == "__main__":
    n = 70
    print(find_sum(n))
    start = time.time()
    print(find_sum_recursive(n))
    end = time.time()
    print("recursion tooks ", str((end - start) * 1000), "miliseconds")
