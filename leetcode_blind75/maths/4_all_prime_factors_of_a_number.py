"""All prime factors of a number."""

from typing import List


class Solution:
    def __prime(self, num: int) -> bool:
        """
        Check if a given number is prime.

        Args:
            num (int): The number to check for primality.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        # Check if the number is less than 2
        if num < 2:
            return False
        # Handle special cases for 2 and even numbers
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        # Iterate through odd numbers up to the square root of num
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def __prime_factors_brute(self, num: int) -> List[int]:
        """
        Find prime factors of a number using brute force approach.

        Args:
            num (int): The number for which to find prime factors.

        Returns:
            List[int]: List of prime factors of the given number.
        """
        factors: List[int] = []
        i: int = 2
        # Iterate through numbers up to the square root of num
        while i * i <= num:
            if num % i == 0:
                # If i is prime, add it to the factors list
                if self.__prime(num=i):
                    factors.append(i)
                # If num/i is prime and not equal to i, add it to factors list
                if num // i != i and self.__prime(num=num // i):
                    factors.append(num // i)
            i += 1

        return factors

    def __prime_factors_optimal(self, num: int) -> List[int]:
        """
        Find prime factors of a number using an optimal approach.

        Args:
            num (int): The number for which to find prime factors.

        Returns:
            List[int]: List of prime factors of the given number.
        """

        factors: List[int] = []
        i: int = 2
        # Iterate through numbers up to num
        while i <= num:
            if num % i == 0:
                # If i is a factor of num, add it to factors list
                factors.append(i)
                # Divide num by i repeatedly to get all occurrences of the factor
                while num % i == 0:
                    num //= i
            i += 1

        return factors

    def prime_factors(self, num: int) -> List[int]:
        """
        Find prime factors of a number.

        Args:
            num (int): The number for which to find prime factors.

        Returns:
            List[int]: List of prime factors of the given number.
        """
        # Use optimal method to find prime factors
        return self.__prime_factors_optimal(num=num)


if __name__ == "__main__":
    num: int = 780
    solution: Solution = Solution()
    # Find all prime factors of the given number
    p_factors: List[int] = solution.prime_factors(num=num)
    print(p_factors)
