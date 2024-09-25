"""House robber 2 first and last element is also adjacent"""

from typing import List


class Solution:
    # This method calculates the maximum amount of money that can be robbed from a list of houses,
    # considering that the first and last houses cannot both be robbed.
    def __house_rob_optimal(self, nums: List[int]) -> int:
        n: int = len(nums)

        # Variables to store the maximum money that can be robbed from the last two houses.
        prev: int = nums[0]  # Maximum money if we rob the first house.
        prev2: int = 0  # Maximum money if we skip the first house.

        # Iterate through the houses starting from the second one.
        for i in range(1, n):
            # Option 1: Rob the current house and add to the maximum from two houses back.
            pick: int = nums[i] + prev2
            # Option 2: Don't rob the current house; take the maximum from the previous house.
            not_pick: int = prev
            # Current maximum is the better of the two options.
            cur: int = max(pick, not_pick)
            # Update prev2 to the last maximum before the current house.
            prev2 = prev
            # Update prev to the current maximum.
            prev = cur

        # After processing all houses, prev holds the answer for the current sub-array.
        return prev

    # Main method that determines the maximum money that can be robbed from the houses.
    def rob(self, nums: List[int]) -> int:
        # Calculate the maximum amount robbed by excluding the last house.
        ans1 = self.__house_rob_optimal(nums[:-1])
        # Calculate the maximum amount robbed by excluding the first house.
        ans2 = self.__house_rob_optimal(nums[1:])
        # Return the maximum of the two scenarios, which ensures we don't rob both the first and last houses.
        return max(ans1, ans2)


# Entry point for testing the solution.
if __name__ == "__main__":
    arr: list[int] = [1, 2, 3]
    n: int = len(arr)
    solution: Solution = Solution()
    print(
        solution.rob(arr)
    )  # This will print the maximum amount of money that can be robbed.
