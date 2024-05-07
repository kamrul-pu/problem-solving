"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""

import heapq
from typing import List


class MedianFinder:
    def __init__(self):
        # Initialize two heaps:
        # - self.small: Max heap to store the smaller half of the elements (negated values for max heap behavior)
        # - self.large: Min heap to store the larger half of the elements
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # Add the new number to the max heap (small)
        heapq.heappush(self.small, -1 * num)

        # Balance the heaps:
        # - If the largest value in self.small is greater than the smallest value in self.large,
        #   move the largest value from self.small to self.large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val: int = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Ensure that the difference in sizes between self.small and self.large is at most 1
        # If self.small is larger, move the largest value from self.small to self.large
        if len(self.small) > len(self.large) + 1:
            val: int = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # If self.large is larger, move the smallest value from self.large to self.small
        if len(self.large) > len(self.small) + 1:
            val: int = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # Determine the median based on the sizes of self.small and self.large
        if len(self.small) > len(self.large):
            return (
                -1 * self.small[0]
            )  # If self.small has more elements, return the largest value (negated) in self.small
        if len(self.large) > len(self.small):
            return self.large[
                0
            ]  # If self.large has more elements, return the smallest value in self.large

        # If the sizes of self.small and self.large are equal, calculate the median as the average
        # of the largest value in self.small (negated) and the smallest value in self.large
        return (-1 * self.small[0] + self.large[0]) / 2


if __name__ == "__main__":
    # Create an instance of MedianFinder
    median: MedianFinder = MedianFinder()

    # Add numbers to the data stream and find the median after each addition
    median.addNum(1)
    median.addNum(2)
    print(median.findMedian())

    median.addNum(3)
    print(median.findMedian())

    median.addNum(-5)
    print(median.findMedian())

    median.addNum(40)
    print(median.findMedian())
