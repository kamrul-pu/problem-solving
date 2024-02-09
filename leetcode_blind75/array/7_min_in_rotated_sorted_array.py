"""FInd minimum in rotated sorted array."""

from typing import List


class Solution:
    # Brute-force approach to find minimum element in array
    def __find_min(self, nums: List[int], n: int) -> int:
        result: int = nums[0]
        # Iterate through the array to find the minimum element
        for i in range(n):
            result = min(result, nums[i])

        return result

    # Better approach to find minimum element in array
    def __find_min_better(self, nums: List[int], n: int) -> int:
        l: int = 0
        r: int = n - 1
        mn: int = nums[0]
        # Use two pointers to scan the array from both ends towards the middle
        while l <= r:
            mn = min(mn, nums[l], nums[r])
            l += 1
            r -= 1

        return mn

    # Optimal approach to find minimum element in rotated sorted array
    def __find_min_optimal(self, nums: List[int], n: int) -> int:
        result: int = nums[0]
        l: int = 0
        r: int = n - 1
        # Use binary search to find the minimum element
        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            mid: int = (l + r) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return result

    # Main function to find minimum element in rotated sorted array
    def findMin(self, nums: list[int]) -> int:
        n: int = len(nums)
        # Uncomment the appropriate function call based on the approach to use
        # return self.__find_min(nums=nums, n=n)  # Brute-force approach
        # return self.__find_min_better(nums=nums, n=n)  # Better approach
        return self.__find_min_optimal(nums=nums, n=n)  # Optimal approach


# Main function to test the findMin function
if __name__ == "__main__":
    # Test input array
    nums: List[int] = [3, 4, 5, 1, 2]
    # nums: List[int] = [4, 5, 0, 1, 2]
    solution: Solution = Solution()
    print(solution.findMin(nums=nums))
