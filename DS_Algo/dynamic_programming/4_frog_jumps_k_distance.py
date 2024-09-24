from typing import List


class Solution:
    def __f(self, n: int, stones: List[int], dp: List[List[int]], k: int) -> int:
        # Base case: if there are no stones to consider, the energy cost is 0
        if n == 0:
            return 0

        # If we've already computed the minimum energy for this stone, return it
        if dp[n] != -1:
            return dp[n]

        # Initialize minimum energy to a very high value
        mn: int = float("inf")

        # Try jumping from the last stone to the previous k stones
        for i in range(1, k + 1):
            if n - i >= 0:  # Ensure we don't go out of bounds
                # Calculate energy cost of jumping to stone n from n-i
                jump_energy = self.__f(n - i, stones, dp, k) + abs(
                    stones[n] - stones[n - i]
                )
                # Update minimum energy if this jump is better
                mn = min(mn, jump_energy)

        # Store the computed minimum energy for this stone in dp
        dp[n] = mn
        return dp[n]

    def __tabulation(self, stones: List[int], n: int, k: int) -> int:
        # Create a dp array to store minimum energy for each stone
        dp: List[int] = [0] * n

        # Fill the dp array iteratively from the second stone to the last
        for i in range(1, n):
            # Initialize minimum energy for this stone to a very high value
            mn: int = float("inf")

            # Try jumping from the previous k stones
            for j in range(1, k + 1):
                if i - j >= 0:  # Ensure we don't go out of bounds
                    # Calculate energy cost of jumping to stone i from i-j
                    jump_energy = dp[i - j] + abs(stones[i] - stones[i - j])
                    # Update minimum energy if this jump is better
                    mn = min(mn, jump_energy)

            # Store the computed minimum energy for this stone in dp
            dp[i] = mn

        # The answer for the last stone is the minimum energy computed
        return dp[n - 1]

    def min_energy(self, stones: List[int], k: int) -> int:
        n: int = len(stones)  # Get the number of stones
        dp: List[int] = [-1] * n  # Initialize the dp array with -1 for memoization

        # Use the tabulation method to find the minimum energy
        return self.__tabulation(stones, n, k)


# Main execution
if __name__ == "__main__":
    stones: List[int] = [10, 20, 30, 40, 10]  # Example stones' heights
    k: int = 3  # Maximum jump length
    solution: Solution = Solution()  # Create an instance of Solution
    print(
        solution.min_energy(stones, k)
    )  # Calculate and print the minimum energy required
