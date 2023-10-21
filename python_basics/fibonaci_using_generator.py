"""Generate fibonacci series using generator."""


def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for f in fibo():
    if f > 50:
        break
    print(f)
