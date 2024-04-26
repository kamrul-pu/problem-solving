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

        # Ensure nums1 is the smaller array for optimization
        if n > m:
            return self.__optimal(nums1=nums2, nums2=nums1)  # Swap if nums1 is larger

        low: int = 0
        high: int = n
        left: int = (n + m) // 2  # Total number of elements in the left half

        while low <= high:
            mid1: int = (low + high) // 2  # Partition point for nums1
            mid2: int = left - mid1  # Corresponding partition point for nums2

            # Determine the elements around the partition points
            r1 = (
                nums1[mid1] if mid1 < n else float("inf")
            )  # Right element of nums1 partition
            r2 = (
                nums2[mid2] if mid2 < m else float("inf")
            )  # Right element of nums2 partition
            l1 = (
                nums1[mid1 - 1] if mid1 - 1 >= 0 else float("-inf")
            )  # Left element of nums1 partition
            l2 = (
                nums2[mid2 - 1] if mid2 - 1 >= 0 else float("-inf")
            )  # Left element of nums2 partition

            # Check if the partitions are valid
            if l1 <= r2 and l2 <= r1:
                # If the total number of elements is odd, return the maximum of the left elements
                if (n + m) % 2 == 1:
                    return max(l1, l2)
                else:
                    # If the total number of elements is even, return the average of the middle elements
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1  # Adjust the partition in nums1 to the left
            else:
                low = mid1 + 1  # Adjust the partition in nums1 to the right

        return 0  # Default return value (should not reach here in valid scenarios)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Entry point for finding the median of two sorted arrays
        return self.__optimal(nums1=nums1, nums2=nums2)


if __name__ == "__main__":
    nums1: List[int] = [1, 3]
    nums2: List[int] = [2, 4]
    solution: Solution = Solution()
    print(solution.findMedianSortedArrays(nums1=nums1, nums2=nums2))
