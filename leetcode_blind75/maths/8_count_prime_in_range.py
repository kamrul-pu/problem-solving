"""Count Prime in range."""

from typing import List

N: int = int(1e3 + 7)


# Initialize a list to store whether each number is prime or not
prime: List[int] = [True] * N
# Set 0 and 1 as non-prime numbers
prime[0] = prime[1] = False


def sieve_algo():
    # Iterate through numbers from 2 up to the square root of N
    for i in range(2, int(N**0.5) + 1):
        # If i is prime
        if prime[i]:
            # Mark all multiples of i as non-prime
            j: int = i * i
            while j < N:
                prime[j] = False
                j += i


class Solution:
    def count_primes(self, l: int, r: int) -> int:
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


if __name__ == "__main__":
    sieve_algo()
    solution: Solution = Solution()
    l: int = 2
    r: int = 100
    print(solution.count_primes(l=l, r=r))
