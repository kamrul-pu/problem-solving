"""
Smallest prime factors prime factorization.
"""

import random
from typing import List

N: int = 101


class Solution:
    def __init__(self) -> None:
        """
        Initialize the Solution class with the smallest prime factors for numbers up to N.
        """
        # Initialize a list to store the smallest prime factors for numbers up to N
        self.spf: List[int] = [i for i in range(N)]
        # Iterate through numbers from 2 up to the square root of N
        for i in range(2, int(N**0.5) + 1):
            # If the current number is a prime number
            if self.spf[i] == i:
                # Mark all multiples of the prime number with the prime number itself
                for j in range(i * i, N, i):
                    if self.spf[j] == j:
                        self.spf[j] = i

    def prime_factors(self, num: int) -> List[int]:
        """
        Find the prime factors of a given number using the smallest prime factors approach.

        Args:
            num (int): The number for which to find the prime factors.

        Returns:
            List[int]: List of prime factors of the given number.
        """
        factors: List[int] = []
        # Iterate until the number becomes 1
        while num != 1:
            # Append the smallest prime factor of num to the factors list
            factors.append(self.spf[num])
            # Divide num by its smallest prime factor
            num //= self.spf[num]

        return factors


if __name__ == "__main__":
    solution: Solution = Solution()
    q: int = random.randint(1, 15)
    # Generate random queries
    while q:
        num: int = random.randint(2, 100)
        print(f"prime factors of {num} are: ", end="")
        # Print the prime factors of each random number
        print(solution.prime_factors(num=num))
        q -= 1
