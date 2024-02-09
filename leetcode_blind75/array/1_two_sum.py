"""Two sum leetcode solution."""

from typing import List


class Solution:
    # Brute-force approach to find two indices that sum up to the target
    def __f(self, nums: List[int], target: int, n: int) -> List[int]:
        # Iterate through all possible pairs of indices
        for i in range(n - 1):
            for j in range(i + 1, n):
                # If the sum of the elements at these indices equals the target, return the indices
                if nums[i] + nums[j] == target:
                    return [i, j]
        # If no such pair is found, return an empty list
        return []

    # Optimal approach using a dictionary to find two indices that sum up to the target
    def __two_sum_optimal(self, nums: List[int], target: int, n: int) -> List[int]:
        # Create a dictionary to store the indices of elements encountered
        index_dict: dict = dict()

        # Iterate through the array
        for i in range(n):
            # Calculate the remaining value needed to reach the target
            remaining: int = target - nums[i]
            # If the remaining value is found in the dictionary, return the indices
            if remaining in index_dict:
                return [index_dict[remaining], i]
            # Otherwise, store the current element's index in the dictionary
            index_dict[nums[i]] = i

        # If no such pair is found, return an empty list
        return []

    # Main function to find two indices that sum up to the target
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n: int = len(nums)
        # Call the optimal approach function to find the indices
        return self.__two_sum_optimal(nums=nums, target=target, n=n)


# Test the twoSum function
if __name__ == "__main__":
    nums: List[int] = [2, 7, 11, 15]
    target: int = 9
    solution: Solution = Solution()
    print(solution.twoSum(nums=nums, target=target))
