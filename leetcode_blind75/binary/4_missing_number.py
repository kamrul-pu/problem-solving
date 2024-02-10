"""Missing number of an array."""

from typing import List


class Solution:
    # Function to find the missing number in the given list
    def __f(self, nums: List[int], n: int) -> int:
        # Calculate the sum of all numbers from 0 to n using the formula (n * (n + 1)) // 2
        result: int = (n * (n + 1)) // 2
        # Calculate the total sum of numbers in the given list
        total: int = sum(nums)
        # The missing number is the difference between the expected sum and the total sum
        return result - total

    def __missing_number_xor(self, nums: List[int], n: int) -> int:
        n: int = len(nums)
        missing: int = n
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    # Main function to find the missing number in the given list
    def missingNumber(self, nums: list[int]) -> int:
        n: int = len(nums)  # Get the length of the input list
        # return self.__f(nums, n)  # Call the helper function to find the missing number
        return self.__missing_number_xor(nums=nums, n=n)


if __name__ == "__main__":
    nums: List[int] = [3, 0, 1]  # Example input list
    solution: Solution = Solution()  # Create an instance of the Solution class
    print(
        solution.missingNumber(nums=nums)
    )  # Print the missing number in the given list
