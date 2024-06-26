"""
You are given a 0-indexed integer array nums. In one operation, you may do the following:

Choose two integers in nums that are equal.
Remove both integers from nums, forming a pair.
The operation is done on nums as many times as possible.

Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs
that are formed and answer[1] is the number of leftover integers in nums after doing the
operation as many times as possible.
"""

from collections import defaultdict
from typing import List, Dict


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # Length of the input array nums
        n: int = len(nums)

        # Dictionary to count occurrences of each number
        hsh: Dict[int, int] = defaultdict(int)

        # Count of pairs formed
        cnt: int = 0

        # Iterate through each number in nums
        for i in range(n):
            # Increment count of occurrences for nums[i]
            hsh[nums[i]] += 1

            # Check if the current number has appeared an even number of times (i.e., forms a pair)
            if hsh[nums[i]] % 2 == 0:
                cnt += 1

        # Calculate the number of leftover integers after forming pairs
        leftover: int = n - 2 * cnt

        # Return the result as a list [number of pairs, number of leftover integers]
        return [cnt, leftover]


nums: List[int] = [1, 3, 2, 1, 3, 2, 2]
solution: Solution = Solution()
print(solution.numberOfPairs(nums=nums))
