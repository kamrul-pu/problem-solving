"""
Given an array arr, replace every element in that array with the greatest
element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Replace every element in arr with the greatest element among the elements to its right,
        and replace the last element with -1. Return the modified array arr.
        """
        n: int = len(arr)  # Get the length of the array arr
        maxi: int = (
            -1
        )  # Initialize maxi to -1, which will eventually be the last element

        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            cur: int = arr[i]  # Current element arr[i]
            arr[i] = (
                maxi  # Replace arr[i] with the current maxi (greatest element to its right)
            )
            maxi = max(
                maxi, cur
            )  # Update maxi to be the maximum of its current value and cur

        return arr  # Return the modified array arr


# Example usage:
if __name__ == "__main__":
    arr: List[int] = [17, 18, 5, 4, 6, 1]
    solution: Solution = Solution()
    print(solution.replaceElements(arr=arr))  # Output: [18, 6, 6, 6, 1, -1]
