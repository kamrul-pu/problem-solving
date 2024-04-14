"""Counting number of bits from 0 to n."""

from typing import List


class Solution:
    # Function to count the number of '1' bits in an integer using Brian Kernighan's Algorithm
    def __hammingWeight(self, n: int) -> int:
        count: int = 0
        while n:
            n &= n - 1
            count += 1
        return count

    # Function to count the number of bits for each number from 0 to n
    def __f(self, n: int) -> List[int]:
        ans: List[int] = []
        for i in range(n + 1):
            bits: int = self.__hammingWeight(
                n=i
            )  # Count the number of '1' bits in the binary representation of i
            ans.append(bits)  # Add the count to the answer list
        return ans

    # Optimal function to count the number of bits for each number from 0 to n
    def __get_bits_optimal(self, n: int) -> List[int]:
        dp: List[int] = [0] * (
            n + 1
        )  # Initialize an array to store the counts of bits for each number
        offset: int = 1  # Initialize the offset value to 1
        for i in range(1, n + 1):
            if offset * 2 == i:  # If i is a power of 2, update the offset value
                offset = i
            dp[i] = (
                1 + dp[i - offset]
            )  # Calculate the number of bits for the current number using the offset
        return dp

    # Main function to count the number of bits for each number from 0 to n
    def countBits(self, n: int) -> List[int]:
        return self.__get_bits_optimal(
            n=n
        )  # Call the optimal function to calculate the counts


if __name__ == "__main__":
    n: int = 10  # Example input value
    solution: Solution = Solution()  # Create an instance of the Solution class
    print(
        solution.countBits(n=n)
    )  # Print the counts of bits for each number from 0 to n
