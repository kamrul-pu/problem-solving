"""Find Kth permutation."""


def find_permutation(n: int, k: int) -> str:
    fact: int = 1
    numbers: list[int] = []
    for i in range(1, n):
        fact = fact * i
        numbers.append(i)
    numbers.append(n)
    ans: str = ""
    k = k - 1
    while True:
        # ans = ans + str(numbers[k // fact])
        # numbers.pop(k // fact)
        ans = ans + str(numbers.pop(k // fact))

        if len(numbers) == 0:
            break
        k = k % fact
        fact = fact // len(numbers)

    return ans


if __name__ == "__main__":
    n: int = 4
    k: int = 17
    print(find_permutation(n=n, k=k))
