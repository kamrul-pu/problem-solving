"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""


class Solution:
    def __brute(self, x: int) -> int:
        ans: int = 1

        # Iterate through numbers from 1 to x-1
        for i in range(1, x):
            # Check if i*i is less than or equal to x
            if i * i <= x:
                ans = i  # Update ans if i*i is valid square root
            else:
                break  # Break the loop if i*i exceeds x

        return ans

    def __optimal(self, x: int) -> int:
        ans: int = x
        lo, hi = 1, x

        # Binary search to find the integer square root
        while lo <= hi:
            mid: int = (lo + hi) // 2
            if mid * mid <= x:
                ans = mid  # Update ans if mid*mid is valid square root
                lo = mid + 1  # Move lo to search for a larger square root
            else:
                hi = mid - 1  # Move hi to search for a smaller square root

        return ans

    def mySqrt(self, x: int) -> int:
        """
        Main function to compute the integer square root of x.

        Args:
        - x: Non-negative integer for which square root needs to be computed.

        Returns:
        - Integer square root of x, rounded down to the nearest integer.
        """
        # Uncomment to use brute-force approach
        # return self.__brute(x)

        # Use optimal approach for efficient computation
        return self.__optimal(x)


if __name__ == "__main__":
    x: int = 35
    solution: Solution = Solution()
    print(solution.mySqrt(x))
