"""Median of two sorted array."""

from typing import List


class Solution:
    def __f(self, nums1: List[int], n: int, nums2: List[int], m: int) -> float:
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

        while i < n:
            temp[k] = nums1[i]
            i += 1
            k += 1
        while j < m:
            temp[k] = nums2[j]
            j += 1
            k += 1

        ln: int = len(temp)
        if ln % 2 == 1:
            return temp[ln // 2]

        return (temp[ln // 2] + temp[ln // 2 - 1]) / 2.0

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n: int = len(nums1)
        m: int = len(nums2)
        return self.__f(nums1, n, nums2, m)


if __name__ == "__main__":
    nums1: List[int] = [1, 3]
    nums2: List[int] = [2]
    solution: Solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))
