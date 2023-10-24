"""Fibonacci using Recursion"""


def fibo_iter(n: int):
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        res = a + b
        a = b
        b = res

    return b


def fibo(n: int):
    if n == 0 or n == 1:
        return n

    return fibo(n - 1) + fibo(n - 2)


if __name__ == "__main__":
    print(fibo(6))
    print(fibo(10))
    print(fibo_iter(10))
