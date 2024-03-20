"""Number of ways to climb stairs."""


def num_ways(n: int, memo: dict = {}) -> int:
    if n <= 1:
        return 1 if n >= 0 else 0
    if n not in memo:
        memo[n] = num_ways(n=n - 1, memo=memo) + num_ways(n=n - 2, memo=memo)

    return memo[n]


if __name__ == "__main__":
    # n: int = int(input("Enter the number of stairs: "))
    n = 10
    print("Number of ways to climb stairs:", num_ways(n=n))
