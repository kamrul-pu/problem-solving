"""House robber 2."""

from typing import List


class Solution:
    def __house_rob(self, nums: List[int], n: int) -> int:
        """
        Helper function to find the maximum amount of money that can be robbed from non-circular houses.

        Args:
            nums (List[int]): The list representing the amount of money in each house.
            n (int): The number of houses.

        Returns:
            int: The maximum amount of money that can be robbed.
        """
        # Initialize variables to keep track of the previous and previous to previous amounts
        prev: int = nums[0]
        prev2: int = 0

        # Iterate through the houses from the second house to the second-to-last house
        for i in range(1, n - 1):
            # Calculate the maximum amount of money that can be robbed at each house
            pick: int = nums[i] + prev2
            not_pick: int = 0 + prev
            cur: int = max(pick, not_pick)
            # Update the variables for the next iteration
            prev2 = prev
            prev = cur
        # Store the maximum amount of money robbed from non-circular houses in ans1
        ans1: int = prev

        # Reset variables for the second pass through the houses (skipping the first house)
        prev: int = nums[1]
        prev2: int = 0

        # Iterate through the houses from the third house to the last house
        for i in range(2, n):
            # Calculate the maximum amount of money that can be robbed at each house
            pick: int = nums[i] + prev2
            not_pick: int = 0 + prev
            cur: int = max(pick, not_pick)
            # Update the variables for the next iteration
            prev2 = prev
            prev = cur

        # Store the maximum amount of money robbed from non-circular houses in ans2
        ans2: int = prev

        # Return the maximum of ans1 and ans2, representing the maximum amount robbed from non-circular houses
        return max(ans1, ans2)

    def rob(self, nums: List[int]) -> int:
        """
        Function to find the maximum amount of money that can be robbed from circular houses.

        Args:
            nums (List[int]): The list representing the amount of money in each house.

        Returns:
            int: The maximum amount of money that can be robbed.
        """
        n: int = len(nums)
        # Call the helper function to find the maximum amount robbed from non-circular houses
        return self.__house_rob(nums=nums, n=n)


if __name__ == "__main__":
    nums: List[int] = [2, 3, 2]
    # nums = [1, 2, 3, 1]
    solution: Solution = Solution()
    print(solution.rob(nums=nums))
