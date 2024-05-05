"""
Design a class to find the kth largest element in a stream. Note that it is
the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth
largest element in the stream.
"""

import heapq

from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        # Initialize the min-heap with the first k elements from nums
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Push the new value to the min-heap
        heapq.heappush(self.min_heap, val)

        # If the size of the min-heap exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        # Return the smallest element (kth largest) in the min-heap
        return self.min_heap[0]


# Example usage:
if __name__ == "__main__":
    k: int = 3
    nums: List[int] = [4, 5, 8, 2]

    # Initialize KthLargest object with k and nums
    kth_largest = KthLargest(k, nums)

    # Add new elements and get the kth largest element
    print(kth_largest.add(3))  # Should return 4
    print(kth_largest.add(5))  # Should return 5
    print(kth_largest.add(10))  # Should return 5
    print(kth_largest.add(9))  # Should return 8
    print(kth_largest.add(4))  # Should return 8
