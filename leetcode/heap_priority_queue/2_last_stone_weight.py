"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash
them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""

import heapq
from typing import List


class Solution:
    def __f(self, stones: List[int]) -> int:
        # Approach using sorting and iterative smashing
        stones.sort()  # Sort the stones initially
        while len(stones) > 1:
            x, y = stones.pop(), stones.pop()  # Get the two heaviest stones
            if x != y:
                stones.append(x - y)  # Smash the stones and get the new weight
                stones.sort()  # Sort the stones after each smash to maintain order

        return (
            stones[0] if stones else 0
        )  # Return the last stone's weight (or 0 if no stones left)

    def lastStoneWeight(self, stones: List[int]) -> int:
        # return self.__f(stones=stones)
        # Transform stones into a max-heap (use negative values for max-heap behavior)
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)  # Convert list to a heap in-place

        # Process stones until there is one stone left in the heap
        while len(max_heap) > 1:
            # Extract the two largest stones (negative values)
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)

            # Calculate the new stone weight by smashing the two stones
            if stone1 != stone2:
                new_stone = stone1 - stone2
                # Push the new stone (negative value for max-heap behavior)
                heapq.heappush(max_heap, -new_stone)

        # Check if there's any stone left in the heap (the last stone weight)
        # Return the last stone's weight (or 0 if no stones left)
        return -max_heap[0] if max_heap else 0


if __name__ == "__main__":
    stones: List[int] = [2, 7, 4, 1, 8, 1]
    # stones = [1]
    solution: Solution = Solution()
    print(solution.lastStoneWeight(stones=stones))
