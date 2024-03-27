"""
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.
"""


class Solution:
    def __f(self, num: int) -> int:
        """
        Find the sum of proper divisors of the given number using an iterative approach.

        Args:
            num (int): The number to find proper divisors for.

        Returns:
            int: The sum of proper divisors of the given number.
        """
        result: int = 0
        i: int = 1
        # Iterate through numbers up to the square root of num
        while i * i <= num:
            # Check if i is a divisor of num
            if num % i == 0:
                result += i
                # If i is not the square root, add the quotient as well
                if num // i != i:
                    result += num // i
            i += 1

        return result - num

    def __perfect_optimal(self, num: int) -> int:
        """
        Check if the given number is a perfect number using a predefined list of known perfect numbers.

        Args:
            num (int): The number to check for perfection.

        Returns:
            bool: True if the number is perfect, False otherwise.
        """
        # Check if num is present in the predefined list of perfect numbers
        return num in [6, 28, 496, 8128, 33550336]

    def checkPerfectNumber(self, num: int) -> bool:
        """
        Check if the given number is a perfect number.

        Args:
            num (int): The number to check for perfection.

        Returns:
            bool: True if the number is perfect, False otherwise.
        """
        # Call either the __f method or the __perfect_optimal method based on the approach
        return self.__perfect_optimal(num=num)


if __name__ == "__main__":
    num: int = 28
    solution: Solution = Solution()
    # Check if the given number is a perfect number
    print(solution.checkPerfectNumber(num=num))
