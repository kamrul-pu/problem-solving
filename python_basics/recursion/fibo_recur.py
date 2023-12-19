"""Fibonacci using recursion."""


def fibo(n: int) -> int:
    if n <= 1:
        return n
    print("n value before call last", n)
    last: int = fibo(n - 1)
    print("n value after last call and before second last", n)
    second_last: int = fibo(n - 2)
    return last + second_last


fibonacci: int = fibo(5)
print(fibonacci)
