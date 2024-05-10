"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
"""

from typing import List


class Solution:
    def __is_palindrome(self, s: str, i: int, j: int) -> bool:
        # Helper function to check if substring s[i:j+1] is a palindrome
        while i < j:
            if s[i] != s[j]:  # Characters mismatch indicates not a palindrome
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        n: int = len(s)
        result: List[List[str]] = []  # List to store all valid partitions
        part: List[str] = []  # List to store the current partition being formed

        def dfs(i):
            # Base case: When we've processed the entire string
            if i >= n:
                result.append(
                    part[:]
                )  # Append a copy of the current partition to result

            # Explore all possible partitions starting from index i
            for j in range(i, n):
                if self.__is_palindrome(s, i, j):
                    # If s[i:j+1] is a palindrome, add it to the current partition
                    part.append(s[i : j + 1])
                    # Recursively explore further partitions starting from j+1
                    dfs(j + 1)
                    # Backtrack: Remove the last added substring to explore other partitions
                    part.pop()

        # Start DFS from index 0 to generate all valid partitions
        dfs(0)

        return result


if __name__ == "__main__":
    s: str = "aab"
    solution: Solution = Solution()
    result: List[List[str]] = solution.partition(s=s)
    print(result)
