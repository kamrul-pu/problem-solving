"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to limit the result to 32 bits
        MASK = 0xFFFFFFFF

        # Perform the addition while ensuring it remains within 32 bits
        while b != 0:
            # Calculate the sum without considering the carry
            sum_without_carry = (a ^ b) & MASK
            # Calculate the carry using bitwise AND and left shift by 1
            carry = ((a & b) << 1) & MASK
            # Update 'a' and 'b' for the next iteration
            a, b = sum_without_carry, carry

        # If 'a' exceeds 32 bits, convert it to negative equivalent in 32 bits
        if a > 0x7FFFFFFF:
            a = ~(a ^ MASK)

        return a


if __name__ == "__main__":
    a: int = 2
    b: int = 3
    solution: Solution = Solution()
    print(solution.getSum(a=a, b=b))
