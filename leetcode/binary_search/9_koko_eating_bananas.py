"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile
of bananas and eats k bananas from that pile. If the pile has less than k bananas,
she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""

import math
from typing import List


class Solution:
    def __brute(self, piles: List[int], h: int) -> int:
        """
        Brute-force approach to find the minimum eating speed k using iterative checking.

        Args:
        - piles: List of integers representing piles of bananas.
        - h: Integer representing the maximum hours Koko has before the guards return.

        Returns:
        - Integer: The minimum eating speed k that allows Koko to finish all bananas within h hours.
        """
        n: int = len(piles)
        k: int = 1

        # Iteratively check eating speeds starting from k=1 upwards
        while True:
            time_taken: int = 0

            # Calculate total time taken to eat all bananas at current speed k
            for i in range(n):
                time_taken += math.ceil(piles[i] / k)

            # If total time taken is within h hours, return k as the answer
            if time_taken <= h:
                return k
            k += 1  # Increment k and repeat the check

    def __f(self, piles: List[int], n: int, k: int) -> int:
        """
        Helper function to calculate the total time taken to eat all bananas at a given eating speed k.

        Args:
        - piles: List of integers representing piles of bananas.
        - n: Integer representing the number of piles.
        - k: Integer representing the eating speed.

        Returns:
        - Integer: Total time taken to eat all bananas at speed k.
        """
        time_taken: int = 0
        for pile in piles:
            time_taken += math.ceil(pile / k)
        return time_taken

    def __optimal(self, piles: List[int], h: int) -> int:
        """
        Optimal approach using binary search to find the minimum eating speed k.

        Args:
        - piles: List of integers representing piles of bananas.
        - h: Integer representing the maximum hours Koko has before the guards return.

        Returns:
        - Integer: The minimum eating speed k that allows Koko to finish all bananas within h hours.
        """
        n: int = len(piles)
        lo, hi = 1, max(piles)  # Set initial bounds for binary search
        ans: int = hi

        # Binary search to find the minimum k
        while lo <= hi:
            mid: int = (lo + hi) // 2
            time: int = self.__f(piles, n, mid)  # Calculate time taken at mid speed

            if time <= h:
                ans = min(ans, mid)  # Update answer if current mid speed is valid
                hi = (
                    mid - 1
                )  # Adjust high bound to search for potentially smaller speeds
            else:
                lo = mid + 1  # Adjust low bound to search for larger speeds

        return ans

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Main function to find the minimum eating speed k using the optimal approach.

        Args:
        - piles: List of integers representing piles of bananas.
        - h: Integer representing the maximum hours Koko has before the guards return.

        Returns:
        - Integer: The minimum eating speed k that allows Koko to finish all bananas within h hours.
        """
        # Uncomment to use the brute-force approach
        # return self.__brute(piles, h)

        # Use the optimal binary search approach
        return self.__optimal(piles, h)


if __name__ == "__main__":
    piles: List[int] = [3, 6, 7, 11]
    h: int = 8
    solution: Solution = Solution()
    print(solution.minEatingSpeed(piles=piles, h=h))
