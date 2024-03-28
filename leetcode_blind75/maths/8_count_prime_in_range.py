"""Count Prime in range."""

import random
from typing import List

N: int = int(1e3 + 7)


# Initialize a list to store whether each number is prime or not
prime: List[int] = [1] * N
# Set 0 and 1 as non-prime numbers
prime[0] = prime[1] = 0


def sieve_algo():
    # Iterate through numbers from 2 up to the square root of N
    for i in range(2, int(N**0.5) + 1):
        # If i is prime
        if prime[i]:
            # Mark all multiples of i as non-prime
            j: int = i * i
            while j < N:
                prime[j] = 0
                j += i


sieve_algo()

cnt: int = 0
for i in range(2, N):
    cnt = cnt + prime[i]
    prime[i] = cnt


class Solution:
    def __primes(self, l: int, r: int) -> int:
        """
        Count the number of prime numbers within a given range [l, r].

        Args:
            l (int): The left boundary of the range.
            r (int): The right boundary of the range.

        Returns:
            int: The count of prime numbers within the specified range.
        """
        cnt: int = 0
        for i in range(l, r + 1):
            if prime[i]:
                cnt += 1
        return cnt

    def count_primes(self, l: int, r: int) -> int:
        # return self.__primes(l=l, r=r)
        return prime[r] - prime[l - 1]


if __name__ == "__main__":
    solution: Solution = Solution()
    q: int = int(input())
    while q:
        l: int = random.randint(1, 100)
        r: int = random.randint(l + 1, 500)
        print(solution.count_primes(l=l, r=r))
        q -= 1
