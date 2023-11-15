def is_prime_brute_force(n: int) -> bool:
    if n < 2:
        return False
    # is_prime = True
    for i in range(2, n):
        if n % 2 == 0:
            return False

    return True


print(is_prime_brute_force(2))
print(is_prime_brute_force(5))

# using sieve algorithm pre computation technique
N: int = 100
is_prime: list[bool] = [True] * N
is_prime[0] = is_prime[1] = False

for i in range(2, int(N**0.5) + 1):
    if is_prime[i] == True:
        for j in range(i * 2, N, i):
            is_prime[j] = False

t: int = int(input("Number of test case: "))
while t:
    x: int = int(input("Enter Number to check: "))
    print(f"{x} is prime" if is_prime[x] else f"{x} is not prime")
    t -= 1