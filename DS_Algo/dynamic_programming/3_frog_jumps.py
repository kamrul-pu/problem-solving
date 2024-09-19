from typing import List

# Define a constant for a large integer value.
INT_MAX: int = 999999


class Solution:
    # Recursive function with memoization to find the minimum energy
    def __f(self, n: int, arr: List[int], dp: List[int]) -> int:
        # Base case: if we are at the first step, no energy is needed
        if n == 0:
            return 0
        # Return already computed value from dp if it exists
        if dp[n] != -1:
            return dp[n]

        # Calculate energy cost to jump from (n-1) to n
        left: int = self.__f(n - 1, arr, dp) + abs(arr[n] - arr[n - 1])
        right: int = INT_MAX  # Initialize right jump cost to a large value

        # If we can jump from (n-2) to n, calculate that cost as well
        if n > 1:
            right = self.__f(n - 2, arr, dp) + abs(arr[n] - arr[n - 2])

        # Store the minimum energy required in dp
        dp[n] = min(left, right)
        return dp[n]

    # Tabulation method to iteratively find minimum energy
    def __tabulation(self, n: int, arr: List[int]) -> int:
        dp: List[int] = [0] * n  # DP array initialized to zero
        for i in range(1, n):
            # Calculate energy cost if jumping from (i-1) to i
            left = dp[i - 1] + abs(arr[i] - arr[i - 1])
            right = INT_MAX  # Initialize right jump cost to a large value

            # Calculate energy cost if jumping from (i-2) to i if possible
            if i > 1:
                right = dp[i - 2] + abs(arr[i] - arr[i - 2])

            # Store the minimum energy required to reach step i
            dp[i] = min(left, right)
        return dp[
            n - 1
        ]  # The last element gives the minimum energy to reach the last step

    # Optimized version using constant space
    def __optimized(self, n: int, arr: List[int]) -> int:
        prev2 = INT_MAX  # Energy cost for two steps back
        prev = 0  # Energy cost for the last step
        for i in range(1, n):
            # Calculate energy cost if jumping from (i-1) to i
            left = prev + abs(arr[i] - arr[i - 1])
            right = prev2  # Energy cost for jumping from (i-2) to i

            # If possible, calculate cost from (i-2) to i
            if i > 1:
                right = prev2 + abs(arr[i] - arr[i - 2])

            # Current minimum energy to reach step i
            cur = min(left, right)
            # Update previous energies for the next iteration
            prev2 = prev
            prev = cur

        return prev  # Return the minimum energy to reach the last step

    # Main function to determine minimum energy required
    def min_energy(self, n: int, arr: List[int]) -> int:
        dp: List[int] = [-1] * n  # DP array initialized to -1
        # Uncomment to use different approaches
        # return self.__f(n - 1, arr, dp)  # Recursive with memoization
        # return self.__tabulation(n, arr)  # Tabulation method
        return self.__optimized(n, arr)  # Optimized space approach


# Example usage
if __name__ == "__main__":
    n: int = 4  # Number of steps
    arr: List[int] = [10, 20, 30, 10]  # Energy levels at each step

    # Create an instance of the Solution class
    solution: Solution = Solution()

    # Calculate and print the minimum energy required for the entire jump sequence
    min_cost: int = solution.min_energy(n, arr)
    print("Minimum energy required:", min_cost)
