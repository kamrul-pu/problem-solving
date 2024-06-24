"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:s
"""

from typing import List


class Solution:
    def __ncr(self, n: int, r: int) -> int:
        """Helper function to compute nCr (binomial coefficient)"""
        if r > n - r:
            r = (
                n - r
            )  # Optimize to calculate faster by choosing the smaller of r or n-r
        numerator = 1
        denominator = 1
        for i in range(r):
            numerator *= n - i
            denominator *= i + 1
        return numerator // denominator  # Return the computed binomial coefficient

    def get_row(self, n: int) -> List[int]:
        """Function to get the nth row of Pascal's Triangle"""
        result: List[int] = []
        ans: int = 1
        result.append(
            ans
        )  # Start with the first element of each row, which is always 1

        for i in range(1, n):
            ans = (
                ans * (n - i) // i
            )  # Calculate each subsequent element using the formula
            result.append(ans)  # Append the computed element to the current row list

        return result  # Return the completed row of Pascal's Triangle

    def generate(self, numRows: int) -> List[List[int]]:
        """Function to generate Pascal's Triangle up to numRows"""
        ans: List[List[int]] = []
        for i in range(1, numRows + 1):
            ans.append(
                self.get_row(i)
            )  # Generate each row and append to the result list
        return ans  # Return the entire Pascal's Triangle as a list of lists

    def get_rc(self, r: int, c: int) -> int:
        """Function to get the value at row r, column c in Pascal's Triangle"""
        return self.__ncr(
            r - 1, c - 1
        )  # Return the binomial coefficient for row r and column c


if __name__ == "__main__":
    n: int = 5
    solution: Solution = Solution()

    # Generate and print Pascal's Triangle up to numRows = 5
    print(solution.generate(n))

    # Example usage: Get value at row 5, column 3 in Pascal's Triangle
    print(solution.get_rc(5, 3))

    # Example usage: Get the 5th row of Pascal's Triangle
    print(solution.get_row(n=5))
