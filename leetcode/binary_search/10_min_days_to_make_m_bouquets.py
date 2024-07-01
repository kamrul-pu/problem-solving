"""
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden.
If it is impossible to make m bouquets return -1.
"""

from typing import List


class Solution:
    def __f(self, bloomDay: List[int], m: int, k: int, day: int) -> bool:
        """
        Helper function to check if it's possible to make at least `m` bouquets
        with `k` adjacent flowers each, using flowers that have bloomed by `day`.

        Args:
        - bloomDay: List of integers representing the days when flowers bloom.
        - m: Integer, the number of bouquets to make.
        - k: Integer, the number of adjacent flowers required for each bouquet.
        - day: Integer, the current day being tested.

        Returns:
        - bool: True if it's possible to make at least `m` bouquets, False otherwise.
        """
        cnt: int = 0  # Counter for adjacent flowers that have bloomed by `day`
        total: int = 0  # Counter for total number of bouquets that can be made
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                cnt += 1  # Increment count if flower at index `i` can be used
            else:
                total += (
                    cnt // k
                )  # Calculate number of bouquets that can be made so far
                cnt = (
                    0  # Reset count since consecutive flowers are required for bouquets
                )
        total += cnt // k  # Final calculation for remaining flowers
        return total >= m  # Return True if enough bouquets can be made

    def __brute(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        Brute-force approach to find the minimum number of days needed to make `m` bouquets
        using `k` adjacent flowers each from the garden.

        Args:
        - bloomDay: List of integers representing the days when flowers bloom.
        - m: Integer, the number of bouquets to make.
        - k: Integer, the number of adjacent flowers required for each bouquet.

        Returns:
        - Integer: The minimum number of days needed, or -1 if it's impossible.
        """
        n: int = len(bloomDay)
        if m * k > n:
            return -1  # If it's impossible to make `m` bouquets, return -1
        mn: int = bloomDay[0]
        mx: int = bloomDay[0]
        for i in range(1, n):
            mn = min(mn, bloomDay[i])  # Find the minimum bloom day
            mx = max(mx, bloomDay[i])  # Find the maximum bloom day

        for i in range(mn, mx + 1):
            if self.__f(bloomDay, m, k, i):
                return i  # Return the day if it's possible to make `m` bouquets

        return -1  # Return -1 if no valid day is found within the range

    def __optimal(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        Optimal approach using binary search to find the minimum number of days needed
        to make `m` bouquets using `k` adjacent flowers each from the garden.

        Args:
        - bloomDay: List of integers representing the days when flowers bloom.
        - m: Integer, the number of bouquets to make.
        - k: Integer, the number of adjacent flowers required for each bouquet.

        Returns:
        - Integer: The minimum number of days needed, or -1 if it's impossible.
        """
        n: int = len(bloomDay)
        if m * k > n:
            return -1  # If it's impossible to make `m` bouquets, return -1
        mn: int = bloomDay[0]
        mx: int = bloomDay[0]
        for i in range(1, n):
            mn = min(mn, bloomDay[i])  # Find the minimum bloom day
            mx = max(mx, bloomDay[i])  # Find the maximum bloom day
        ans: int = mx
        lo, hi = mn, mx

        while lo <= hi:
            mid: int = (lo + hi) // 2
            if self.__f(bloomDay, m, k, mid):
                ans = min(ans, mid)  # Update answer if current mid day is valid
                hi = mid - 1  # Adjust high bound to search for potentially smaller days
            else:
                lo = mid + 1  # Adjust low bound to search for larger days

        return ans

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        Main function to find the minimum number of days needed to make `m` bouquets
        using `k` adjacent flowers each from the garden.

        Args:
        - bloomDay: List of integers representing the days when flowers bloom.
        - m: Integer, the number of bouquets to make.
        - k: Integer, the number of adjacent flowers required for each bouquet.

        Returns:
        - Integer: The minimum number of days needed, or -1 if it's impossible.
        """
        # Uncomment to use the brute-force approach
        # return self.__brute(bloomDay, m, k)

        # Use the optimal binary search approach
        return self.__optimal(bloomDay, m, k)


if __name__ == "__main__":
    bloomDay: List[int] = [7, 7, 7, 7, 12, 7, 7]
    m: int = 2
    k: int = 3
    solution: Solution = Solution()
    print(solution.minDays(bloomDay, m, k))
