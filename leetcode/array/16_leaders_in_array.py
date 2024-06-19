from typing import List

class Solution:
    def allLeaders(self, nums: List[int]) -> List[int]:
        """
        Return a list of all leaders in nums.
        A leader is an element which is greater than all the elements to its right in the array.
        """
        n = len(nums)
        leaders: List[int] = []  # Initialize an empty list to store leaders
        maxi: int = float("-inf")  # Initialize maxi to negative infinity to track maximum encountered so far

        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            if nums[i] > maxi:
                leaders.append(nums[i])  # If nums[i] is greater than maxi, it's a leader, so add it to leaders
                maxi = nums[i]  # Update maxi to nums[i] to track the maximum element encountered so far

        return leaders[::-1]  # Return leaders list reversed to match the original order of leaders from left to right


# Example usage:
arr: List[int] = [10, 22, 12, 3, 0, 6]
solution: Solution = Solution()
print(solution.allLeaders(arr))  # Output: [22, 12, 6]
