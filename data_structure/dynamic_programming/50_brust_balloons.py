from typing import List


class Solution:
    def __f(self, i: int, j: int, nums: List[int], dp: List[List[int]]) -> int:
        # Recursive function to calculate maximum coins from bursting balloons between indices i and j
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        maxi: int = -1e9  # Initialize maximum value to negative infinity
        for k in range(i, j + 1):
            # Calculate the cost of bursting balloon k last between i and j
            cost: int = (
                nums[i - 1] * nums[k] * nums[j + 1]  # Bursting balloon k
                + self.__f(i, k - 1, nums, dp)  # Coins gained from left subarray
                + self.__f(k + 1, j, nums, dp)  # Coins gained from right subarray
            )
            maxi = max(maxi, cost)  # Update maximum coins gained
        dp[i][j] = maxi  # Store the result in the dp table
        return maxi

    def maxCoins(self, nums: List[int]) -> int:
        n: int = len(nums)
        nums.insert(0, 1)  # Insert 1 at the beginning
        nums.append(1)  # Insert 1 at the end
        # dp: List[List[int]] = [[-1] * (n + 2) for _ in range(n + 2)]  # Memoization table
        # return self.__f(1, n, nums, dp)  # Call the recursive function
        return self.__max_coins_tabulation(
            nums=nums, n=n
        )  # Call the tabulation function

    def __max_coins_tabulation(self, nums: List[int], n: int) -> int:
        # Tabulation function to calculate maximum coins
        dp: List[List[int]] = [
            [0] * (n + 2) for _ in range(n + 2)
        ]  # Initialize dp table
        for i in range(n, 0, -1):
            for j in range(1, n + 1):
                if i > j:
                    continue
                maxi: int = -1e9  # Initialize maximum value to negative infinity
                for k in range(i, j + 1):
                    # Calculate the cost of bursting balloon k last between i and j
                    cost: int = (
                        nums[i - 1] * nums[k] * nums[j + 1]  # Bursting balloon k
                        + dp[i][k - 1]  # Coins gained from left subarray
                        + dp[k + 1][j]  # Coins gained from right subarray
                    )
                    maxi = max(maxi, cost)  # Update maximum coins gained
                dp[i][j] = maxi  # Store the result in the dp table
        return dp[1][n]  # Return the maximum coins gained


if __name__ == "__main__":
    nums: List[int] = [3, 1, 5, 8]  # Balloon values
    solution: Solution = Solution()  # Create Solution object
    print(solution.maxCoins(nums))  # Print the maximum coins gained
