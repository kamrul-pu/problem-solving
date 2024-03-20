"""416. Partition Equal Subset Sum."""

from typing import List


class Solution:
    def __subset_sum(self, nums: List[int], n: int, k: int) -> bool:
        """
        Check if there exists a subset of nums that adds up to the target sum k.

        Args:
            nums (List[int]): List of integers.
            n (int): Number of elements in the nums list.
            k (int): Target sum.

        Returns:
            bool: True if there exists a subset that adds up to k, False otherwise.
        """
        # Initialize two lists to keep track of subset sums
        prev: List[bool] = [False] * (k + 1)
        cur: List[bool] = [False] * (k + 1)

        prev[0] = True  # Base case: subset sum of 0 is always possible
        if nums[0] <= k:
            prev[nums[0]] = (
                True  # Initialize the first element of nums in prev list if it's smaller than or equal to k
            )

        # Dynamic programming loop to fill in the cur list based on prev list
        for i in range(1, n):
            cur[0] = True  # Base case: subset sum of 0 is always possible
            for target in range(1, k + 1):
                not_take: bool = prev[target]  # If not taking the current element
                take: bool = False
                if nums[i] <= target:
                    take = prev[target - nums[i]]  # If taking the current element
                cur[target] = (
                    take or not_take
                )  # Update the cur list based on whether we take or not take the current element

            prev = cur  # Update prev list for the next iteration

        return prev[k]  # Return whether it's possible to achieve the target sum k

    def canPartition(self, nums: List[int]) -> bool:
        """
        Determine whether the given list can be partitioned into two subsets with equal sum.

        Args:
            nums (List[int]): List of integers.

        Returns:
            bool: True if the list can be partitioned into two equal sum subsets, False otherwise.
        """
        n: int = len(nums)  # Get the number of elements in the nums list
        s: int = sum(nums)  # Calculate the total sum of elements in the nums list
        if (
            s % 2 == 1
        ):  # If the total sum is odd, it's not possible to partition into two equal sum subsets
            return False

        s //= 2  # Calculate the target sum for each subset
        return self.__subset_sum(
            nums=nums, n=n, k=s
        )  # Check if there exists a subset that adds up to half of the total sum


if __name__ == "__main__":
    nums: List[int] = [1, 5, 11, 5]  # Example input list
    solution: Solution = Solution()  # Create an instance of the Solution class
    print(
        solution.canPartition(nums=nums)
    )  # Print whether it's possible to partition the list into two equal sum subsets
