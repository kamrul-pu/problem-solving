"""
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case,
both input and output will be given as a signed integer type. They should not affect your
implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0  # Initialize the variable to store the reversed bits
        for _ in range(32):  # Iterate 32 times (since it's a 32-bit integer)
            result = (result << 1) | (
                n & 1
            )  # Shift the result left by 1 and add the least significant bit of n
            n >>= 1  # Right shift n to consider the next bit
        return result  # Return the reversed bits


if __name__ == "__main__":
    n: int = 4
    solution: Solution = Solution()
    print(solution.reverseBits(n=n))
