from time import time, sleep
from typing import List
from numba import njit


def f1():
    l: List[int] = []
    for x in range(10):
        for y in range(1000):
            for z in range(10000):
                if (x + y + z) / 10 == x:
                    l.append(x)
    return l


@njit
def f2():
    l: List[int] = []
    for x in range(10):
        for y in range(1000):
            for z in range(10000):
                if (x + y + z) / 10 == x:
                    l.append(x)
    return l


# start = time()
# f1()
# print(f"Finished after {round(time()-start, 2)} seconds")

start = time()
f2()
print(f"Finished after {round(time()-start, 2)} seconds")
