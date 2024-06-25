"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

from typing import List


class Solution(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        # Initialize pointers for nums1, nums2, and the merged array index
        i: int = m - 1
        # Pointer for nums1 (starting from the end of valid nums1 elements)
        j: int = n - 1  # Pointer for nums2 (starting from the end of nums2)
        k: int = m + n - 1
        # Pointer for the merged array (starting from the end of nums1 + nums2)

        # Merge nums1 and nums2 from the end to the beginning
        while j >= 0:
            # If there are elements left in nums1 and nums1's current element is greater than nums2's current element
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]  # Place nums1's current element in the merged array
                i -= 1  # Move pointer i to the left in nums1
            else:
                nums1[k] = nums2[j]  # Place nums2's current element in the merged array
                j -= 1  # Move pointer j to the left in nums2
            k -= 1  # Move pointer k to the left in the merged array


# Example usage:
nums1: List[int] = [4, 5, 6, 0, 0, 0]  # nums1 with extra space at the end
m: int = 3  # Number of valid elements in nums1
nums2: List[int] = [1, 2, 3]  # nums2
n: int = 3  # Number of elements in nums2

solution: Solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)  # Output the merged and sorted nums1 array
