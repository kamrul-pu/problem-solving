"""Contains duplicate in an array."""

from typing import List


class Solution:
    # Function to check if the list contains any duplicates
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Convert the list to a set to remove duplicates
        nums_set = set(nums)
        # If the length of the original list is not equal to the length of the set,
        # it means there were duplicates in the original list
        return len(nums) != len(nums_set)


# Main function to test the containsDuplicate function
if __name__ == "__main__":
    # Test input list
    nums: List[int] = [1, 2, 3, 1]
    # Create an instance of the Solution class
    solution: Solution = Solution()
    # Call the containsDuplicate function and print the result
    print(solution.containsDuplicate(nums=nums))
