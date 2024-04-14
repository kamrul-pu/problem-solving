"""House robber."""

from typing import List


class Solution:
    def __f(self, i: int, nums: List[int], dp: List[int]) -> int:
        """
        Recursive function to find the maximum amount of money that can be robbed from the houses.

        Args:
            i (int): Index of the current house.
            nums (List[int]): The list representing the amount of money in each house.
            dp (List[int]): Memoization table to store the results of subproblems.

        Returns:
            int: The maximum amount of money that can be robbed.
        """
        if i == 0:
            return nums[i]
        if i < 0:
            return 0
        if dp[i] != -1:
            return dp[i]
        # Calculate the maximum amount of money that can be robbed either by picking or not picking the current house
        not_pick: int = 0 + self.__f(i - 1, nums, dp)
        pick: int = nums[i] + self.__f(i - 2, nums, dp)
        # Store the maximum amount of money for the current house in the memoization table
        dp[i] = max(not_pick, pick)
        return dp[i]

    def __house_rob_tabulation(self, nums: List[int], n: int) -> int:
        """
        Function to find the maximum amount of money that can be robbed using tabulation.

        Args:
            nums (List[int]): The list representing the amount of money in each house.
            n (int): The number of houses.

        Returns:
            int: The maximum amount of money that can be robbed.
        """
        # Initialize the table to store the maximum amount of money that can be robbed at each house
        dp: List[int] = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            # Calculate the maximum amount of money that can be robbed at each house
            not_pick: int = 0 + dp[i - 1]
            pick: int = nums[i] + (dp[i - 2] if i > 1 else 0)
            dp[i] = max(not_pick, pick)
        return dp[n - 1]

    def __house_rob_optimal(self, nums: List[int], n: int) -> int:
        """
        Function to find the maximum amount of money that can be robbed using an optimal approach.

        Args:
            nums (List[int]): The list representing the amount of money in each house.
            n (int): The number of houses.

        Returns:
            int: The maximum amount of money that can be robbed.
        """
        prev: int = nums[0]
        prev2: int = 0
        for i in range(1, n):
            # Calculate the maximum amount of money that can be robbed at each house using an optimal approach
            pick: int = nums[i] + prev2
            not_pick: int = 0 + prev
            cur: int = max(pick, not_pick)
            prev2 = prev
            prev = cur
        return prev

    def rob(self, nums: List[int]) -> int:
        """
        Function to find the maximum amount of money that can be robbed.

        Args:
            nums (List[int]): The list representing the amount of money in each house.

        Returns:
            int: The maximum amount of money that can be robbed.
        """
        n: int = len(nums)
        # Uncomment one of the following methods to use
        # dp: List[int] = [-1] * n
        # return self.__f(n - 1, nums, dp)  # Using recursion with memoization
        return self.__house_rob_tabulation(nums, n)  # Using tabulation
        # return self.__house_rob_optimal(nums, n)  # Using an optimal approach


if __name__ == "__main__":
    nums: List[int] = [1, 2, 3, 1]
    nums = [1, 2]
    solution: Solution = Solution()
    print(solution.rob(nums=nums))
