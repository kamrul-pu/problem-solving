"""
Given an integer numsay nums, return the number of reverse pairs in the numsay.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
"""

from typing import List


class Solution:
    def __count(self, nums: List[int], low: int, mid: int, high: int) -> int:
        cnt: int = 0
        right: int = mid + 1

        # Iterate over the elements in the left half
        for i in range(low, mid + 1):
            # Move the 'right' pointer until we find the condition nums[i] > 2 * nums[right]
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            # All elements from mid+1 to 'right-1' form reverse pairs with nums[i]
            cnt += right - (mid + 1)

        return cnt

    def __burte(self, nums: List[int]) -> int:
        n: int = len(nums)
        cnt: int = 0

        # Iterate over all pairs (i, j) where i < j and nums[i] > 2 * nums[j]
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] > 2 * nums[j]:
                    cnt += 1

        return cnt

    def merge(self, nums: List[int], low: int, mid: int, high: int) -> None:
        temp: List[int] = []
        left: int = low
        right: int = mid + 1

        # Merge the two halves into 'temp'
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        # Add remaining elements from the left half
        while left <= mid:
            temp.append(nums[left])
            left += 1

        # Add remaining elements from the right half
        while right <= high:
            temp.append(nums[right])
            right += 1

        # Copy sorted elements from 'temp' back to 'nums'
        for i in range(low, high + 1):
            nums[i] = temp[i - low]

    def merge_sort(self, nums: List[int], low: int, high: int) -> int:
        cnt: int = 0

        # If the subarray has more than one element
        if low < high:
            mid: int = (low + high) // 2

            # Recursively divide and merge sort the left half
            cnt += self.merge_sort(nums, low, mid)
            # Recursively divide and merge sort the right half
            cnt += self.merge_sort(nums, mid + 1, high)
            # Count reverse pairs across the two halves and merge them
            cnt += self.__count(nums, low, mid, high)
            self.merge(nums, low, mid, high)

        return cnt

    def reversePairs(self, nums: List[int]) -> int:
        """
        Calculate the number of reverse pairs in the array 'nums' using merge sort and counting approach.

        Parameters:
        - nums: The input list of integers.

        Returns:
        - int: The total number of reverse pairs in 'nums'.
        """
        # Choose either brute force or merge sort approach
        # return self.__brute(nums=nums)
        n: int = len(nums)
        return self.merge_sort(nums, 0, n - 1)


if __name__ == "__main__":
    nums: List[int] = [2, 4, 3, 5, 1]
    solution: Solution = Solution()
    print(solution.reversePairs(nums=nums))
