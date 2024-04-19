from collections import deque
from typing import Deque, List


class Solution:
    def __brute(self, nums: List[int], k: int) -> List[int]:
        # This method implements the brute-force approach to find the maximum sliding window
        n: int = len(nums)
        l: int = 0
        r: int = l + k - 1
        ans: List[int] = []
        while r < n:
            # Calculate the maximum value in the current window [l, r]
            ans.append(max(nums[l : r + 1]))
            l += 1
            r += 1
        return ans

    def __better(self, nums: List[int], k: int) -> List[int]:
        # This method implements a more optimized approach to find the maximum sliding window
        n: int = len(nums)
        l: int = 0
        r: int = l + k - 1
        ans: List[int] = []
        mi: int = 0
        mx: int = float("-inf")

        # Initialize the maximum and its index for the first window [0, k-1]
        for i in range(k):
            if nums[i] > mx:
                mx = nums[i]
                mi = i
        ans.append(mx)
        l += 1
        r += 1

        # Iterate through the rest of the array to find maximum values in subsequent windows
        while r < n:
            # Update the maximum value and its index efficiently
            if mi >= l and r - l + 1 > 1 and nums[r] > mx:
                mx = nums[r]
                mi = r
            elif mi >= l and r - l + 1:
                pass  # No need to update maximum if the maximum index is within the current window
            else:
                # If maximum index is out of the current window, recalibrate the maximum
                mx = float("-inf")
                for i in range(l, r + 1):
                    if nums[i] > mx:
                        mx = nums[i]
                        mi = i
            ans.append(mx)
            l += 1
            r += 1

        return ans

    def __optimal(self, nums: List[int], k: int) -> List[int]:
        # This method implements the optimal approach using a deque to find the maximum sliding window
        ans: List[int] = []
        q: Deque[int] = deque()
        l = r = 0

        # Iterate through the array using pointers l and r for the sliding window
        while r < len(nums):
            # Maintain the deque such that it stores indices of elements in decreasing order of nums values

            # Remove indices from the back of the deque if their corresponding values are less than nums[r]
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Append the current index r to the deque
            q.append(r)

            # Remove the leftmost index from the deque if it's out of the current window [l, r]
            if l > q[0]:
                q.popleft()

            # If the window size has reached k, start collecting maximum values
            if (r + 1) >= k:
                # The maximum value for the current window is at the front of the deque (nums[q[0]])
                ans.append(nums[q[0]])
                # Slide the window to the right by incrementing l
                l += 1

            # Move to the next element in nums
            r += 1

        return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # This method is the entry point to find the maximum sliding window using the optimal approach
        return self.__optimal(nums=nums, k=k)


# Test the solution
if __name__ == "__main__":
    # Example usage of the maxSlidingWindow method
    nums = [1, 3, 1, 2, 0, 5]
    k = 3
    solution = Solution()
    result = solution.maxSlidingWindow(nums=nums, k=k)
    print(result)
