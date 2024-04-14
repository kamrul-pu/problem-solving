"""
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
"""

from collections import defaultdict
from typing import DefaultDict


class Solution:
    def __brute(self, s: str, k: int) -> int:
        # Initialize variables
        n: int = len(s)
        max_len = 0
        mp: DefaultDict = defaultdict(int)
        # Iterate over each character in the string as a potential starting point
        for i in range(n):
            # Clear the frequency map for each iteration
            mp.clear()
            # Iterate over characters starting from the current position
            for j in range(i, n):
                # Update the frequency of the current character
                mp[s[j]] += 1
                # If the number of distinct characters is less than or equal to k, update the maximum length
                if len(mp) <= k:
                    max_len = max(max_len, j - i + 1)
        return max_len

    def __better(self, s: str, k: int) -> int:
        # Initialize variables
        n: int = len(s)
        max_len = l = r = 0
        mp: DefaultDict = defaultdict(int)
        # Iterate over the characters in the string
        while r < n:
            # Add the current character to the frequency map
            mp[s[r]] += 1
            # If the number of distinct characters exceeds k
            while len(mp) > k:
                # Decrease the frequency of the character at the left pointer
                mp[s[l]] -= 1
                # If the frequency becomes 0, remove the character from the map
                if mp[s[l]] == 0:
                    mp.pop(s[l])
                # Move the left pointer to the right
                l += 1
            # Update the maximum length
            if len(mp) <= k:
                max_len = max(max_len, r - l + 1)
            # Move the right pointer to the right
            r += 1
        return max_len

    def __optimal(self, s: str, k: int) -> int:
        # Initialize variables
        n: int = len(s)
        max_len = l = r = 0
        mp: DefaultDict = defaultdict(int)
        # Iterate over the characters in the string
        while r < n:
            # Add the current character to the frequency map
            mp[s[r]] += 1
            # If the number of distinct characters exceeds k
            if len(mp) > k:
                # Decrease the frequency of the character at the left pointer
                mp[s[l]] -= 1
                # If the frequency becomes 0, remove the character from the map
                if mp[s[l]] == 0:
                    mp.pop(s[l])
                # Move the left pointer to the right
                l += 1
            # Update the maximum length
            if len(mp) <= k:
                max_len = max(max_len, r - l + 1)
            # Move the right pointer to the right
            r += 1
        return max_len

    def lengthOfLongestSubstringTwoDistinct(self, s: str, k: int) -> int:
        # Choose the optimal solution
        return self.__optimal(s=s, k=k)


if __name__ == "__main__":
    # Example usage
    s: str = "aaabbccd"
    k: int = 2
    solution: Solution = Solution()
    print(solution.lengthOfLongestSubstringTwoDistinct(s=s, k=k))
