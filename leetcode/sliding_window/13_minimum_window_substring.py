"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
"""

from collections import defaultdict
from typing import DefaultDict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize variables
        n = len(s)  # Length of string s
        m = len(t)  # Length of string t
        hsh: DefaultDict = defaultdict(
            int
        )  # Dictionary to store character counts of string t

        # Count the frequency of characters in string t
        for char in t:
            hsh[char] += 1

        # Initialize pointers and variables for window calculation
        l = r = cnt = (
            0  # Pointers for left and right ends of the window, and count of characters found
        )
        min_len = float("inf")  # Initialize minimum window length to infinity
        s_index = -1  # Initialize starting index of the minimum window substring

        # Move the right pointer to expand the window
        while r < n:
            # If the current character is in string t, increment the count
            if hsh[s[r]] > 0:
                cnt += 1
            # Decrease the count of the character in the hash map
            hsh[s[r]] -= 1
            # Move the right pointer to the next character
            r += 1

            # Shrink the window by moving the left pointer
            while cnt == m:  # If all characters in t are found in the window
                # Update the minimum window length and starting index if necessary
                if (r - l) < min_len:
                    min_len = r - l
                    s_index = l
                # Increase the count of the character at the left end of the window
                hsh[s[l]] += 1
                # If the character count becomes positive, decrement the total character count
                if hsh[s[l]] > 0:
                    cnt -= 1
                # Move the left pointer to shrink the window
                l += 1

        # Return the minimum window substring or an empty string if no such substring exists
        return "" if s_index == -1 else s[s_index : s_index + min_len]


if __name__ == "__main__":
    s: str = "ADOBECODEBANC"
    t: str = "ABC"
    solution: Solution = Solution()
    print(solution.minWindow(s=s, t=t))
