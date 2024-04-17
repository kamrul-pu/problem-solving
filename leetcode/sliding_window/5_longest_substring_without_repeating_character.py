"""
Given a string s, find the length of the longest substring without repeating characters.
"""

from typing import Dict, Set


class Solution:
    def __f(self, s: str) -> int:
        # Initialize an empty set to keep track of characters in the current window
        char_set: Set[str] = set()
        # Initialize variables to keep track of the left pointer (`l`), maximum length (`mx_len`), and current length (`l`)
        l: int = 0
        mx_len: int = 0
        # Iterate through each character in the string `s` using a sliding window approach
        for r in range(len(s)):
            # If the current character `s[r]` is already in the set (indicating a repeating character)
            while s[r] in char_set:
                # Remove characters from the left side of the window until the repeating character is removed
                char_set.remove(s[l])
                l += 1
            # Add the current character `s[r] to the characters set
            char_set.add(s[r])
            # Update the max length if bigger length string found
            mx_len = max(mx_len, r - l + 1)

        return mx_len

    def __brute(self, s: str) -> int:
        """
        Brute force approach to find the length of the longest substring without repeating characters.
        This method iterates over all possible substrings and keeps track of characters using a hash table.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        """
        n: int = len(s)
        mx: int = 0  # Initialize the maximum length
        for i in range(n):  # Iterate over all possible starting indices of substrings
            hsh: Dict = dict()  # Hash table to store characters and their indices
            for j in range(i, n):  # Iterate over characters starting from i
                if (
                    s[j] in hsh
                ):  # If the character is already in the hash table, break the loop
                    break
                ln: int = j - i + 1  # Length of the current substring
                mx = max(mx, ln)  # Update the maximum length if needed
                hsh[s[j]] = 1  # Add the character to the hash table
        return mx

    def __optimal(self, s: str) -> int:
        """
        Optimal approach to find the length of the longest substring without repeating characters.
        This method uses a sliding window approach with a hash table to efficiently find the solution.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        """
        n: int = len(s)
        mx: int = 0  # Initialize the maximum length
        hsh: Dict = dict()  # Hash table to store characters and their indices
        l: int = 0  # Left pointer of the sliding window
        r: int = 0  # Right pointer of the sliding window
        while r < n:  # Iterate over the characters of the string
            if (
                s[r] in hsh and hsh[s[r]] >= l
            ):  # If the character is already seen in the current window
                l = (
                    hsh[s[r]] + 1
                )  # Move the left pointer to the next position after the last occurrence
            else:
                ln: int = (
                    r - l + 1
                )  # Length of the current substring without repeating characters
                mx = max(mx, ln)  # Update the maximum length if needed
            hsh[s[r]] = r  # Update the index of the current character in the hash table
            r += 1  # Move the right pointer to the next position
        return mx

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.
        This method allows you to choose between the brute force and optimal solutions.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        """
        # return self.__brute(s=s)  # Uncomment to use the brute force approach
        return self.__optimal(
            s=s
        )  # Uncomment to use the optimal sliding window approach


if __name__ == "__main__":
    s: str = "abcabcbb"  # Example input string
    solution: Solution = Solution()
    # Output the length of the longest substring without repeating characters
    print(solution.lengthOfLongestSubstring(s=s))
