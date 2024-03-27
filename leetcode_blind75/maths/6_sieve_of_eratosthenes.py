"""Sieve Of Eratosthenes."""

from typing import List

N: int = int(1e1 + 7)


class Solution:
    def __init__(self) -> None:
        """
        Initialize the Sieve of Eratosthenes algorithm to generate prime numbers up to a specified limit.
        """
        # Initialize a list to store whether each number is prime or not
        self.prime: List[int] = [True] * N
        # Set 0 and 1 as non-prime numbers
        self.prime[0] = self.prime[1] = False
        # Call the Sieve of Eratosthenes algorithm
        self.__sieve_algo()

    def __sieve_algo(self) -> None:
        """
        Apply the Sieve of Eratosthenes algorithm to mark non-prime numbers.
        """
        # Iterate through numbers from 2 up to the square root of N
        for i in range(2, int(N**0.5) + 1):
            # If i is prime
            if self.prime[i]:
                # Mark all multiples of i as non-prime
                j: int = i * i
                while j < N:
                    self.prime[j] = False
                    j += i

    def is_prime(self, n: int) -> bool:
        """
        Check if a given number is prime.

        Args:
            n (int): The number to check for primality.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        return self.prime[n]


if __name__ == "__main__":
    solution: Solution = Solution()
    print(solution.is_prime(n=2))
    print(solution.is_prime(7))
