"""Jump game."""

from typing import List


class Solution:
    def __f(self, i: int, n: int, nums: List[int], dp: List[int]) -> bool:
        """
        Recursive function to check if it's possible to reach the last index starting from index i.

        Args:
            i (int): Current index.
            n (int): Length of the array.
            nums (List[int]): Integer array representing maximum jump length at each position.
            dp (List[int]): Dynamic programming array to store intermediate results.

        Returns:
            bool: True if it's possible to reach the last index from index i, False otherwise.
        """
        if i == n - 1:
            return True
        if nums[i] == 0:
            return False
        if dp[i] != -1:
            return dp[i]
        for j in range(1, nums[i] + 1):
            if self.__f(i + j, n, nums, dp):
                dp[i] = True
                return dp[i]

        dp[i] = False
        return dp[i]

    def __can_jump(self, nums: List[int], n: int) -> bool:
        """
        Function to check if it's possible to reach the last index using a greedy approach.

        Args:
            nums (List[int]): Integer array representing maximum jump length at each position.
            n (int): Length of the array.

        Returns:
            bool: True if it's possible to reach the last index, False otherwise.
        """
        reachable: int = 0
        for i in range(n):
            if reachable < i:
                return False
            reachable = max(reachable, i + nums[i])

        return True

    def canJump(self, nums: List[int]) -> bool:
        """
        Main function to determine if it's possible to reach the last index.

        Args:
            nums (List[int]): Integer array representing maximum jump length at each position.

        Returns:
            bool: True if it's possible to reach the last index, False otherwise.
        """
        n: int = len(nums)
        # dp: List[int] = [-1] * n
        # return self.__f(0, n, nums, dp)
        return self.__can_jump(nums=nums, n=n)


if __name__ == "__main__":
    nums: List[int] = [2, 3, 1, 1, 4]
    nums = [2, 0, 0]
    solution: Solution = Solution()
    print(solution.canJump(nums=nums))
