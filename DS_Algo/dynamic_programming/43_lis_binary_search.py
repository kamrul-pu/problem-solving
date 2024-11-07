"""Longest increasing subsequence using binary search."""

from typing import List
import bisect


class Solution:
    # Method to find the length of the longest increasing subsequence (LIS) using dynamic programming with binary search
    def __f(self, nums: List[int], n: int) -> int:
        # temp is used to store the increasing subsequence
        temp: List[int] = [nums[0]]  # Start by adding the first element of nums
        for i in range(1, n):
            # If the current number is greater than the last number in the temp list, append it
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                # Otherwise, find the first number in temp that is >= nums[i] using binary search
                # This is the position where nums[i] can replace a value
                index = bisect.bisect_left(temp, nums[i])
                # Replace the value at that index with nums[i], maintaining the property of the increasing subsequence
                temp[index] = nums[i]
        # The length of the temp list is the length of the longest increasing subsequence
        return len(temp)

    # Method to perform binary search to find the lower bound of the target element in the array
    def __lower_bound(self, nums: List[int], n: int, target: int) -> int:
        # Initialize answer with n (this will track the position where we can insert the target)
        ans: int = n
        low: int = 0  # Start of the array
        high: int = n - 1  # End of the array

        while low <= high:
            mid: int = (low + high) // 2  # Find the middle element
            if nums[mid] >= target:
                # If nums[mid] is greater than or equal to the target, we need to search the left part
                ans = mid  # Update answer with the current mid position
                high = mid - 1  # Move the high pointer to the left part of the array
            else:
                # If nums[mid] is less than target, the lower part doesn't work, so move low pointer to the right
                low = mid + 1
        # Return the lower bound index where target can be inserted or replaced
        return ans

    # Method to find LIS using binary search to optimize the process
    def __using_bs(self, nums: List[int], n: int) -> int:
        # temp is used to store the current longest increasing subsequence
        temp: List[int] = [nums[0]]  # Start by adding the first element of nums
        for i in range(1, n):
            # If the current number is greater than the last number in temp, append it
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                # Use the lower_bound helper method to find the index where nums[i] can replace an element in temp
                index = self.__lower_bound(temp, len(temp), nums[i])
                # Replace the element at that index with nums[i], maintaining the increasing subsequence property
                temp[index] = nums[i]
        # Return the length of the LIS (the length of the temp list)
        return len(temp)

    # Main method to return the length of the longest increasing subsequence
    def lis(self, nums: List[int]) -> int:
        n: int = len(nums)  # Length of the input array
        # Call the optimized method using binary search (you can also choose to use the dynamic programming method __f)
        # Return the result of the LIS computation
        return self.__using_bs(nums, n)


# Example usage
if __name__ == "__main__":
    # Test case: array of numbers
    nums: List[int] = [1, 7, 8, 4, 5, 6, -1, 9]

    # Create an instance of the Solution class
    solution: Solution = Solution()

    # Find the length of the longest increasing subsequence
    print(solution.lis(nums))  # Output the result (should be 4, LIS: [-1, 4, 5, 9])
