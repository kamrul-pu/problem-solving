"""Divisors of a number."""

from typing import List


class Solution:
    def __divisors_brute(self, number: int) -> List[int]:
        """
        Find all divisors of a given number using a brute-force approach.

        Args:
            number (int): The number to find divisors for.

        Returns:
            List[int]: A list of divisors of the given number.
        """
        divisors: List[int] = []
        # Iterate through all numbers from 1 to the given number
        for i in range(1, number + 1):
            # Check if the current number divides the given number evenly
            if number % i == 0:
                # If it does, add it to the list of divisors
                divisors.append(i)

        return divisors

    def __divisors_better(self, number: int) -> List[int]:
        """
        Find all divisors of a given number using a more optimized approach.

        Args:
            number (int): The number to find divisors for.

        Returns:
            List[int]: A list of divisors of the given number.
        """
        divisors: List[int] = []
        i: int = 1
        # Iterate through all numbers from 1 to the square root of the given number
        while i * i <= number:
            # Check if the current number divides the given number evenly
            if number % i == 0:
                # If it does, add it to the list of divisors
                divisors.append(i)
                # Also add the quotient if it's not equal to the current divisor
                if number // i != i:
                    divisors.append(number // i)
            i += 1

        return divisors

    def all_divisors(self, number: int) -> List[int]:
        """
        Find all divisors of a given number.

        Args:
            number (int): The number to find divisors for.

        Returns:
            List[int]: A list of divisors of the given number.
        """
        # Use a better optimized approach to find divisors
        return self.__divisors_better(number=number)


if __name__ == "__main__":
    number: int = 36
    solution: Solution = Solution()
    divisors: List[int] = solution.all_divisors(number=number)
    print(divisors)
