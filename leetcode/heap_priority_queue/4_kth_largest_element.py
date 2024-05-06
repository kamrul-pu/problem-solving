"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting
"""

import heapq
from typing import List


class Solution:
    def __using_sort(self, nums: List[int], k: int) -> int:
        # Helper function to find the kth largest element using sorting (not preferred)
        nums.sort(reverse=True)  # Sort the array in descending order
        return nums[k - 1]  # Return the kth largest element (0-based index)

    def __f(self, nums: List[int], k: int) -> int:
        # Helper function to find the kth largest element using a min-heap of size k
        min_heap: List[int] = []  # Min-heap to maintain the largest k elements

        # Push first k elements into the min-heap (negative values for max-heap behavior)
        for num in nums[:k]:
            heapq.heappush(min_heap, num)

        # Process remaining elements in the array
        for num in nums[k:]:
            # Push the current element into the min-heap if it's larger than the smallest element in the heap
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        # The root of the min-heap will be the kth largest element
        return min_heap[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Main method to find the kth largest element in the array
        # Use the optimized helper function __f to find the kth largest element
        return self.__f(nums=nums, k=k)


# Example usage:
if __name__ == "__main__":
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]  # Example input array
    k: int = 2  # Value of k for finding the kth largest element

    solution: Solution = Solution()  # Create an instance of the Solution class
    result: int = solution.findKthLargest(
        nums=nums, k=k
    )  # Find the kth largest element
    print(result)  # Print the result (kth largest element)
