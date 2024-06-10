"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution:
    def reverse(self, x: int) -> int:
        # Initialize a boolean variable to track if the input number is negative
        negative: bool = False

        # Check if the input number is negative
        if x < 0:
            negative = True
            x *= -1  # Make the number positive for easier manipulation

        # Initialize a variable to store the reversed number
        reversed_num: int = 0

        # Iterate until the input number becomes zero
        while x:
            # Extract the last digit of the input number and append it to the reversed number
            reversed_num = reversed_num * 10 + x % 10

            # Remove the last digit from the input number
            x //= 10

        # Check if the reversed number exceeds the 32-bit signed integer range
        if reversed_num > 0x7FFFFFFF:
            return 0  # If so, return 0

        # If the original number was negative, make the reversed number negative
        return reversed_num * -1 if negative else reversed_num


if __name__ == "__main__":
    x: int = -123
    solution: Solution = Solution()
    print(solution.reverse(x=x))
