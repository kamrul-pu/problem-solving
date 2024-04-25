"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

from typing import List


class Solution:
    def __f(self, nums1: List[int], nums2: List[int]) -> float:
        # Merging approach (Not optimized)
        n: int = len(nums1)
        m: int = len(nums2)

        # Merge both sorted arrays into a single temporary array
        temp: List[int] = [0] * (n + m)
        i: int = 0
        j: int = 0
        k: int = 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                temp[k] = nums1[i]
                i += 1
            else:
                temp[k] = nums2[j]
                j += 1
            k += 1

        # Append remaining elements from nums1 (if any)
        while i < n:
            temp[k] = nums1[i]
            i += 1
            k += 1

        # Append remaining elements from nums2 (if any)
        while j < m:
            temp[k] = nums2[j]
            j += 1
            k += 1

        # Calculate median based on the length of the merged array
        ln: int = len(temp)
        if ln % 2 == 1:
            return temp[ln // 2]
        return (temp[ln // 2] + temp[ln // 2 - 1]) / 2.0

    def __optimal(self, nums1: List[int], nums2: List[int]) -> float:
        # Optimized approach using binary search (O(log(min(n, m))))
        n: int = len(nums1)
        m: int = len(nums2)
        total: int = n + m
        half: int = total // 2

        # Ensure nums1 is the smaller array for optimization
        if m < n:
            nums1, nums2 = nums2, nums1
            n, m = m, n

        l, r = 0, n - 1
        while True:
            i: int = (l + r) // 2  # Partition point for nums1
            j: int = half - i - 2  # Partition point for nums2

            # Determine elements around partition points
            a_left: int = nums1[i] if i >= 0 else float("-inf")
            a_right: int = nums1[i + 1] if (i + 1) < n else float("inf")
            b_left: int = nums2[j] if j >= 0 else float("-inf")
            b_right: int = nums2[j + 1] if (j + 1) < m else float("inf")

            # Check if the partition is correct
            if a_left <= b_right and b_left <= a_right:
                # If total length is odd, return the minimum of the two middle elements
                if total % 2:
                    return min(a_right, b_right)
                # If total length is even, return the average of the two middle elements
                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            # Adjust partition based on comparison results
            elif a_left > b_right:
                r = i - 1  # Adjust partition in nums1 to the left
            else:
                l = i + 1  # Adjust partition in nums1 to the right

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Entry point for finding the median of two sorted arrays
        return self.__optimal(nums1=nums1, nums2=nums2)


if __name__ == "__main__":
    nums1: List[int] = [1, 3]
    nums2: List[int] = [2, 4]
    solution: Solution = Solution()
    print(solution.findMedianSortedArrays(nums1=nums1, nums2=nums2))
