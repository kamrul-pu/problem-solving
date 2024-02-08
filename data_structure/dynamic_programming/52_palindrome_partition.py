"""Palindrome partition - ii. Using front partition."""

from typing import List


class Solution:
    def __is_palindrome(self, i: int, j: int, s: str) -> bool:
        # Helper function to check if a substring from index i to j is a palindrome
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def __f(self, i: int, s: str, n: int, dp: List[int]) -> int:
        # Recursive function to find the minimum cuts needed to partition the string
        if i == n:
            return 0
        if dp[i] != -1:
            return dp[i]
        mn_cost: int = 1e9  # Initialize minimum cost to a very large value
        for j in range(i, n):
            # Check all possible substrings starting from index i
            if self.__is_palindrome(i, j, s):
                # If the substring from i to j is a palindrome
                cost: int = 1 + self.__f(
                    j + 1, s, n, dp
                )  # Calculate cost for remaining string
                mn_cost = min(mn_cost, cost)  # Update minimum cost

        dp[i] = mn_cost  # Memoize the result
        return mn_cost

    def __min_partition_tabulation(self, s: str, n: int) -> int:
        # Tabulation function to find the minimum cuts needed to partition the string
        dp: List[int] = [0 for _ in range(n + 1)]  # Initialize DP array

        for i in range(n - 1, -1, -1):
            mn_cost: int = 1e9  # Initialize minimum cost to a very large value
            for j in range(i, n):
                # Check all possible substrings starting from index i
                if self.__is_palindrome(i, j, s):
                    # If the substring from i to j is a palindrome
                    cost: int = 1 + dp[j + 1]  # Calculate cost for remaining string
                    mn_cost = min(mn_cost, cost)  # Update minimum cost

            dp[i] = mn_cost  # Store the minimum cost for current index i

        return dp[0] - 1  # Return the minimum cuts needed

    def minCut(self, s: str) -> int:
        n: int = len(s)
        # dp: List[int] = [-1 for _ in range(n)]  # Memoization table
        # return self.__f(0, s, n, dp) - 1  # Call the recursive function
        return self.__min_partition_tabulation(s, n)  # Call the tabulation function


if __name__ == "__main__":
    s: str = "bababcbadcede"  # Example string
    solution: Solution = Solution()
    print(solution.minCut(s=s))  # Print the minimum cuts needed to partition the string
