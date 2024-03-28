"""
The goal is to find the total number of subarrays in the given array whose sum equals the target value k.

Approach:
- Initialize variables to keep track of the result, prefix sum, and a defaultdict to store the frequency of prefix sums.
- Initialize the prefix sum to 0 and add it to the defaultdict with a frequency of 1, denoting an empty subarray.
- Iterate through the elements of the nums array.
- Update the prefix sum by adding the current element.
- Calculate the difference between the current prefix sum and the target value k to find the complement.
- Increment the result by the frequency of the complement prefix sum in the defaultdict.
- Increment the frequency of the current prefix sum in the defaultdict.
- Return the result.

Explanation:
- We use a prefix sum approach to efficiently compute the sum of subarrays.
- The defaultdict is used to store the frequency of prefix sums encountered so far.
- As we iterate through the nums array, we update the prefix sum by adding each element.
- For each prefix sum encountered, we calculate the complement (prefix_sum - k) to check if there exists a subarray with a sum of k.
- We increment the result by the frequency of the complement prefix sum stored in the defaultdict, indicating the number of subarrays found.
- Finally, we update the frequency of the current prefix sum in the defaultdict.
- By the end of the iteration, the result will contain the total number of subarrays with a sum equal to k.

Time Complexity Analysis:
- The algorithm has a time complexity of O(n), where n is the length of the nums array.
- This is because we iterate through the nums array once and perform constant-time operations within each iteration.
"""

from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize variables
        result: int = 0
        prefix_sum: int = 0
        # Use defaultdict to store the frequency of prefix sums
        d: DefaultDict = defaultdict(int)
        # Initialize the prefix sum to 0 and add it to the defaultdict with a frequency of 1
        d[0] = 1

        # Iterate through the elements of the nums array
        for num in nums:
            # Update the prefix sum by adding the current element
            prefix_sum += num
            # Calculate the complement (prefix_sum - k) to find subarrays with sum k
            complement: int = prefix_sum - k
            # Increment the result by the frequency of the complement prefix sum
            result += d[complement]
            # Increment the frequency of the current prefix sum
            d[prefix_sum] += 1

        # Return the result
        return result


if __name__ == "__main__":
    # Test the subarraySum function
    nums: List[int] = [1, 2, 3]
    k: int = 3
    solution: Solution = Solution()
    print(solution.subarraySum(nums=nums, k=k))
