"""
Write a function that takes the binary representation of a positive integer and returns the number of
set bits
 it has (also known as the Hamming weight).
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize count to store the number of set bits (1s)
        count: int = 0

        # Iterate until n becomes 0 (all bits are processed)
        while n:
            # Check if the rightmost bit is 1 using bitwise AND operation
            # Increment count if it's 1
            count += n & 1

            # Right shift n by 1 bit to process the next bit
            n >>= 1

        # Return the total count of set bits
        return count


if __name__ == "__main__":
    n: int = 127
    solution: Solution = Solution()
    print(solution.hammingWeight(n=n))
