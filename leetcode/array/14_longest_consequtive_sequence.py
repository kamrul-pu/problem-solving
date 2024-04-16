"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

from typing import List, Set


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the input list `nums` into a set for O(1) average-time lookup
        nums_set: Set[int] = set(nums)
        longest: int = 0

        # Iterate through each number in the input list `nums`
        for num in nums:
            # Check if the current number `num` is the start of a new consecutive sequence
            if num - 1 not in nums_set:
                length: int = 0

                # Increment the length while the consecutive sequence continues
                while num + length in nums_set:
                    length += 1

                # Update the `longest` variable with the maximum length found
                longest = max(longest, length)

        # Return the length of the longest consecutive sequence found
        return longest


if __name__ == "__main__":
    # Example usage
    nums: List[int] = [100, 4, 200, 1, 3, 2]
    solution: Solution = Solution()

    # Find the length of the longest consecutive sequence in `nums`
    print(solution.longestConsecutive(nums=nums))
