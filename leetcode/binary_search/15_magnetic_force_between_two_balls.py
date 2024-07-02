"""
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls
if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at
position[i], Morty has m balls and needs to distribute the balls into the baskets such that the
minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.
"""

from typing import List


class Solution:
    def can_place(self, position: List[int], dist: int, m: int) -> bool:
        """
        Helper function to check if it's possible to place 'm' balls in 'position' array
        such that the minimum distance between any two balls is at least 'dist'.

        Args:
        - position: List of integers representing positions of empty baskets, sorted in non-decreasing order.
        - dist: Integer representing the minimum required distance between any two balls.
        - m: Integer representing the number of balls to place.

        Returns:
        - bool: True if it's possible to place 'm' balls with at least 'dist' distance apart, False otherwise.
        """
        cnt: int = 1  # Number of balls placed
        last: int = position[0]  # Position of the last placed ball

        for i in range(1, len(position)):
            if position[i] - last >= dist:
                cnt += 1
                last = position[i]

        return cnt >= m

    def maxDistance(self, position: List[int], m: int) -> int:
        """
        Function to find the maximum possible minimum distance between balls in the baskets.

        Args:
        - position: List of integers representing positions of empty baskets, sorted in non-decreasing order.
        - m: Integer representing the number of balls to place.

        Returns:
        - int: Maximum possible minimum distance between balls.
        """
        position.sort()  # Sort positions of baskets in non-decreasing order
        n: int = len(position)
        mn: int = position[0]  # Minimum position
        mx: int = position[n - 1]  # Maximum position
        lo, hi = 1, mx - mn + 1  # Binary search bounds
        ans: int = 1  # Result variable

        while lo <= hi:
            mid: int = (lo + hi) // 2  # Midpoint of current search range
            if self.can_place(position, mid, m):
                ans = max(ans, mid)  # Update answer if current mid can place 'm' balls
                lo = mid + 1  # Try for a larger minimum distance
            else:
                hi = mid - 1  # Try for a smaller minimum distance

        return ans


if __name__ == "__main__":
    position: List[int] = [5, 4, 3, 2, 1, 1000000000]
    m: int = 2
    solution: Solution = Solution()
    print(solution.maxDistance(position, m))
