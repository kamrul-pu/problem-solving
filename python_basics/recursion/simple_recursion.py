"""Simple Recursion in python."""

a: int = 0


def func(n: int) -> None:
    if n < 1:
        return
    print(n, end=" ")
    func(n - 1)
    print(n, end=" ")


def print_names(i: int = 1, n: int = 0) -> None:
    if i > n:
        return
    print("Kamrul")
    print_names(i + 1, n)


def print_1_to_n(n: int) -> None:
    if n < 1:
        return
    print_1_to_n(n - 1)
    print(n)


def print_n_to_one(n: int) -> None:
    if n < 1:
        return
    print(n)
    print_n_to_one(n - 1)


def fact(n: int) -> int:
    if n < 1:
        return 1
    return n * fact(n - 1)


def fibo(n: int) -> int:
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


def sum_recur(i: int, sum: int) -> None:
    if i < 1:
        print(sum)
        return
    sum_recur(i - 1, sum + i)


def sum_r(n: int) -> int:
    if n == 0:
        return 0
    return n + sum_r(n - 1)


if __name__ == "__main__":
    func(10)
    print_names(n=5)
    print_1_to_n(10)
    print_n_to_one(10)
    print(fact(5))
    print(fibo(3))

    sum_recur(4, 0)
    print(sum_r(4))
