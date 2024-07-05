"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

from typing import List


class Solution:
    def __brute(self, nums1: List[int], nums2: List[int]) -> float:
        n: int = len(nums1)
        m: int = len(nums2)
        i: int = 0
        j: int = 0
        nums: List[int] = []

        # Merge both sorted arrays into a single sorted array
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        # Add remaining elements from nums1
        while i < n:
            nums.append(nums1[i])
            i += 1

        # Add remaining elements from nums2
        while j < m:
            nums.append(nums2[j])
            j += 1

        l: int = n + m  # Total length of merged array
        mid: int = l // 2  # Middle index of merged array

        # Determine median based on whether total length is even or odd
        if l % 2 == 0:
            return (nums[mid] + nums[mid - 1]) / 2.0  # Average of two middle elements
        else:
            return nums[mid]  # Middle element

    def __better(self, nums1: List[int], nums2: List[int]) -> float:
        n: int = len(nums1)
        m: int = len(nums2)
        i: int = 0
        j: int = 0
        l: int = n + m
        ind2: int = l // 2
        ind1: int = ind2 - 1
        cnt: int = 0
        el1: int = -1
        el2: int = -1

        # Traverse both arrays to find the median elements
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                if cnt == ind1:
                    el1 = nums1[i]
                if cnt == ind2:
                    el2 = nums1[i]
                i += 1
            else:
                if cnt == ind1:
                    el1 = nums2[j]
                if cnt == ind2:
                    el2 = nums2[j]
                j += 1
            cnt += 1

        # Handle remaining elements in nums1
        while i < n:
            if cnt == ind1:
                el1 = nums1[i]
            if cnt == ind2:
                el2 = nums1[i]
            i += 1
            cnt += 1

        # Handle remaining elements in nums2
        while j < m:
            if cnt == ind1:
                el1 = nums2[j]
            if cnt == ind2:
                el2 = nums2[j]
            j += 1
            cnt += 1

        # Determine median based on whether total length is even or odd
        if l % 2 == 0:
            return (el1 + el2) / 2.0  # Average of two median elements
        else:
            return el2  # Median element

    def __optimal(self, nums1: List[int], nums2: List[int]) -> float:
        n1: int = len(nums1)
        n2: int = len(nums2)
        n: int = n1 + n2

        # Ensure nums1 is smaller or equal in size compared to nums2
        if n1 > n2:
            return self.__optimal(nums2, nums1)

        low, high = 0, n1
        left: int = (n1 + n2 + 1) // 2

        # Binary search to find the correct partitioning of nums1 and nums2
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1  # Calculating mid2 based on mid1

            # Initialize variables to represent left and right elements of the partitions
            l1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            r1 = nums1[mid1] if mid1 < n1 else float("inf")
            l2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
            r2 = nums2[mid2] if mid2 < n2 else float("inf")

            # Check conditions for finding the correct partition
            if l1 <= r2 and l2 <= r1:
                # Found the correct partition
                if n % 2 == 1:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # Adjusting the binary search range
                high = mid1 - 1
            else:
                # Adjusting the binary search range
                low = mid1 + 1

        return 0.0  # Default return if arrays are empty or no median found

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Uncomment the desired method below to use for finding median
        # return self.__brute(nums1, nums2)
        # return self.__better(nums1, nums2)
        return self.__optimal(nums1, nums2)


if __name__ == "__main__":
    nums1: List[int] = [1, 3]
    nums2: List[int] = [2, 4]
    solution: Solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))
