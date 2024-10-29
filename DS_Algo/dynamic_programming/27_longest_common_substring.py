"""Longest common substring problem using dynamic programming."""

from typing import List


class Solution:
    def __f(self, s1: str, s2: str) -> int:
        n: int = len(s1)  # Length of the first string
        m: int = len(s2)  # Length of the second string

        # Create a 2D list (dp) to store lengths of longest common suffixes
        dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]

        ans: int = 0  # Variable to keep track of the maximum length found

        # Fill the dp array
        for i in range(1, n + 1):  # Iterate over the first string
            for j in range(1, m + 1):  # Iterate over the second string
                if s1[i - 1] == s2[j - 1]:  # If characters match
                    dp[i][j] = (
                        1 + dp[i - 1][j - 1]
                    )  # Increment the count from previous match
                    ans = max(ans, dp[i][j])  # Update the maximum length found

        return ans  # Return the length of the longest common substring

    def __optimized(self, s1: str, s2: str) -> int:
        n: int = len(s1)  # Length of the first string
        m: int = len(s2)  # Length of the second string

        # Use two lists to save space (only keep current and previous row)
        prev: List[int] = [0] * (m + 1)
        curr: List[int] = [0] * (m + 1)

        ans: int = 0  # Variable to keep track of the maximum length found

        # Fill the dp array using optimized space
        for i in range(1, n + 1):  # Iterate over the first string
            for j in range(1, m + 1):  # Iterate over the second string
                if s1[i - 1] == s2[j - 1]:  # If characters match
                    curr[j] = 1 + prev[j - 1]  # Increment the count from previous match
                    ans = max(ans, curr[j])  # Update the maximum length found
            prev = curr  # Move current row to previous row for next iteration

        return ans  # Return the length of the longest common substring

    def lcs(self, s1: str, s2: str) -> int:
        # Choose either the full implementation or the optimized one
        # return self.__f(s1, s2)  # Uncomment to use the full dp implementation
        return self.__optimized(
            s1, s2
        )  # Using the optimized version for better space efficiency


if __name__ == "__main__":
    s1: str = "abcd"  # First string
    s2: str = "abzd"  # Second string
    solution: Solution = Solution()  # Create an instance of Solution
    print(solution.lcs(s1, s2))  # Output the length of the longest common substring
