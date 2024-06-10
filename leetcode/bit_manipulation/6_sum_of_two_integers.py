"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Iterate until 'b' becomes 0
        while b != 0:
            # Calculate the carry using bitwise AND and left shift by 1
            carry = (a & b) << 1
            # Calculate the sum without considering the carry using bitwise XOR
            a = a ^ b
            # Update 'b' to hold the carry value for the next iteration
            b = carry
        # Return the final sum stored in 'a'
        return a


if __name__ == "__main__":
    a: int = 2
    b: int = 3
    solution: Solution = Solution()
    print(solution.getSum(a=a, b=b))
