"""
Given an array of positive integers nums, return the number of distinct prime factors in the product of the elements of nums.

Note that:

A number greater than 1 is called prime if it is divisible by only 1 and itself.
An integer val1 is a factor of another integer val2 if val2 / val1 is an integer.
"""

from typing import List


class Solution:
    def __prime_factors(self, num: int) -> int:
        """
        Count the number of distinct prime factors of a given number.

        Args:
            num (int): The number for which to count distinct prime factors.

        Returns:
            int: The count of distinct prime factors of the given number.
        """
        cnt: int = 0
        i: int = 2
        # Iterate through numbers up to the square root of num
        while i * i <= num:
            if num % i == 0:
                # Increment the count if i is a factor of num
                cnt += 1
                # Divide num by i repeatedly to get all occurrences of the factor
                while num % i == 0:
                    num //= i
            i += 1
        # If num is not 1, it means it's a prime number, so increment the count
        if num != 1:
            cnt += 1
        return cnt

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        """
        Count the number of distinct prime factors in the product of elements in the given list.

        Args:
            nums (List[int]): The list of positive integers.

        Returns:
            int: The number of distinct prime factors in the product of the elements of nums.
        """
        product: int = 1
        # Calculate the product of all elements in the list
        for num in nums:
            product *= num

        # Count the distinct prime factors in the product
        return self.__prime_factors(num=product)


if __name__ == "__main__":
    nums: List[int] = [2, 4, 3, 7, 10, 6]
    solution: Solution = Solution()
    print(solution.distinctPrimeFactors(nums=nums))
