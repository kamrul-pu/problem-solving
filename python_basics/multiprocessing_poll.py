"""
Multiprocessing pool.
Distributing work load. -> Map
Aggregation of work. -> Reduce
This is also called parallel process.
Pool perform better in heavy load
for small load serial processing is good
"""


import time
from multiprocessing import Pool


def f(n):
    sum = 0
    for x in range(1000):
        sum += x * x
    return sum


if __name__ == "__main__":
    t1 = time.time()
    # Create a pool
    p = Pool()
    pool_result = p.map(f, range(10000))
    p.close()
    p.join()
    # print("pool result", pool_result)
    print("pool took", (time.time() - t1) * 1000, "miliseconds")

    t2 = time.time()

    result = []
    for x in range(10000):
        result.append(f(x))
    print("seriali processing took: ", (time.time() - t2) * 1000, "miliseconds")
