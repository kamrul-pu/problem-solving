"""Search in rotated sorted array."""

from typing import List


from typing import List


class Solution:
    # Binary search function to find the target element in the rotated sorted array
    def __f(self, nums: List[int], target: int, n: int) -> int:
        lo: int = 0
        hi: int = n - 1
        # Perform binary search until the search range is valid
        while lo <= hi:
            mid: int = (lo + hi) // 2
            # If the middle element is the target, return its index
            if nums[mid] == target:
                return mid

            # Check if the left portion is sorted
            if nums[lo] <= nums[mid]:
                # If the target is within the sorted left portion, update the search range accordingly
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            # If the right portion is sorted
            else:
                # If the target is within the sorted right portion, update the search range accordingly
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        # If the target element is not found, return -1
        return -1

    # Main function to search for the target element in the rotated sorted array
    def search(self, nums: List[int], target: int) -> int:
        n: int = len(nums)
        return self.__f(nums=nums, target=target, n=n)


# Main function to test the search function
if __name__ == "__main__":
    nums: List[int] = [4, 5, 6, 7, 0, 1, 2]
    target: int = 0
    solution: Solution = Solution()
    print(solution.search(nums=nums, target=target))
