"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.
"""

from typing import List


class Solution:
    def __brute(self, arr: List[int], k: int) -> int:
        """
        Brute-force approach to find the kth missing positive integer from the sorted array.

        Args:
        - arr: List of integers sorted in strictly increasing order.
        - k: Integer, the kth missing positive integer to find.

        Returns:
        - int: The kth missing positive integer.
        """
        n: int = len(arr)
        for i in range(n):
            if arr[i] <= k:
                k += 1
            else:
                break
        return k

    def __optimal(self, arr: List[int], k: int) -> int:
        """
        Optimized binary search approach to find the kth missing positive integer from the sorted array.

        Args:
        - arr: List of integers sorted in strictly increasing order.
        - k: Integer, the kth missing positive integer to find.

        Returns:
        - int: The kth missing positive integer.
        """
        n: int = len(arr)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid: int = (lo + hi) // 2
            missing: int = arr[mid] - (
                mid + 1
            )  # Number of missing integers up to index mid
            if missing < k:
                lo = (
                    mid + 1
                )  # If there are fewer missing than k, search in the right half
            else:
                hi = (
                    mid - 1
                )  # If there are more or equal missing than k, search in the left half
        # kth missing number is also
        # return k + hi + 1
        # The kth missing positive integer will be after the last position checked
        return lo + k

    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Main function to find the kth missing positive integer using the optimal approach.

        Args:
        - arr: List of integers sorted in strictly increasing order.
        - k: Integer, the kth missing positive integer to find.

        Returns:
        - int: The kth missing positive integer.
        """
        # Uncomment to use the brute-force approach
        # return self.__brute(arr, k)

        # Use the optimal binary search approach
        return self.__optimal(arr, k)


if __name__ == "__main__":
    arr: List[int] = [2, 3, 4, 7, 11]
    k: int = 5
    solution: Solution = Solution()
    print(solution.findKthPositive(arr, k))
