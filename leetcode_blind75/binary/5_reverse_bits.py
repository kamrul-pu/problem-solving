"""Reverse of an integers bits."""


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
    n = 43261596  # Given decimal number
    solution = Solution()  # Create an instance of the Solution class
    print(solution.reverseBits(n))  # Print the result of reversing the bits of n
