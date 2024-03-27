"""Check prime number."""


class Solution:
    def __prime_optimal(self, num: int) -> bool:
        """
        Check if the given number is a prime number.

        Args:
            num (int): The number to check for primality.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        # Check if the number is less than 2
        if num < 2:
            return False
        # Handle special cases for 2 and odd numbers
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        # Iterate through odd numbers up to the square root of num
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def __prime(self, num: int) -> bool:
        """
        Check if the given number is a prime number.

        Args:
            num (int): The number to check for primality.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        # Check if the number is less than or equal to 1
        if num <= 1:
            return False

        i: int = 2
        # Iterate through numbers up to the square root of num
        while i * i < num:
            # Check if i is a factor of num
            if num % i == 0:
                return False
            i += 1

        return True

    def is_prime(self, num: int) -> bool:
        """
        Check if the given number is a prime number.

        Args:
            num (int): The number to check for primality.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        # Call the __prime method to check for primality
        # return self.__prime(num=num)
        return self.__prime_optimal(num=num)


if __name__ == "__main__":
    num: int = 7
    solution: Solution = Solution()
    # Check if the given number is prime
    print(solution.is_prime(num=num))
