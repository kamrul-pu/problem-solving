"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize a list 'dp' to store the count of 1's for each number from 0 to n
        dp: List[int] = [0] * (n + 1)

        # Initialize 'offset' to track the power of 2
        offset: int = 1

        # Iterate from 1 to n
        for i in range(1, n + 1):
            # If the current index is a power of 2, update 'offset'
            if offset * 2 == i:
                offset = i

            # Calculate the count of 1's using the previously computed values
            # by adding 1 to the count of 1's for the number at index 'i - offset'
            dp[i] = 1 + dp[i - offset]

        # Return the list 'dp' containing the count of 1's for each number from 0 to n
        return dp


if __name__ == "__main__":
    n: int = 7
    solution: Solution = Solution()
    result: List[int] = solution.countBits(n=n)
    print(result)
