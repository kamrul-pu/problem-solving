"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

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
        # Initialize 'missing' to n, which is the maximum possible number
        missing: int = n
        # Iterate through each index and element in the 'nums' list
        for i, num in enumerate(nums):
            # Update 'missing' by performing XOR operation with the index and element
            # This effectively cancels out pairs of numbers and leaves the missing number
            missing ^= i ^ num
        # Return the final missing number
        return missing

    def __missing_2(self, nums: List[int]) -> int:
        # Get the length of the input list
        n: int = len(nums)
        # Initialize 'res' to 'n', which is the maximum possible number
        res: int = n
        # Iterate through each index in the range from 0 to 'n-1'
        for i in range(n):
            # Update 'res' by adding the difference between the current index 'i'
            # and the value at index 'i' in 'nums'
            res += i - nums[i]
        # Return 'res', which holds the missing number after iterating through the entire list
        return res

    # Main function to find the missing number in the given list
    def missingNumber(self, nums: list[int]) -> int:
        n: int = len(nums)  # Get the length of the input list
        # return self.__f(nums, n)  # Call the helper function to find the missing number
        return self.__missing_number_xor(nums=nums, n=n)


if __name__ == "__main__":
    nums: List[int] = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    solution: Solution = Solution()
    print(solution.missingNumber(nums=nums))
