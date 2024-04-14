"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

from typing import List


class Solution:
    def __brute(self, s: str, k: int) -> int:
        n: int = len(s)
        max_len: int = 0
        for i in range(n):
            hsh: List[int] = [0] * 26
            max_f: int = 0
            for j in range(i, n):
                # Update the frequency of the current character
                hsh[ord(s[j]) - ord("A")] += 1
                # Update the maximum frequency of characters seen so far
                max_f = max(max_f, hsh[ord(s[j]) - ord("A")])
                # Calculate the number of character changes needed to make all characters in the substring same
                char_change: int = (j - i + 1) - max_f
                # Check if the number of character changes is within the allowed limit k
                if char_change <= k:
                    max_len = max(max_len, j - i + 1)
                else:
                    break
        return max_len

    def __better(self, s: str, k: int) -> int:
        n: int = len(s)
        l = r = mx_len = max_f = 0
        hsh: List[int] = [0] * 26
        while r < n:
            # Update the frequency of the current character
            hsh[ord(s[r]) - ord("A")] += 1
            # Update the maximum frequency of characters seen so far
            max_f = max(max_f, hsh[ord(s[r]) - ord("A")])
            # If the number of character changes exceeds k, adjust the window
            while (r - l + 1) - max_f > k:
                hsh[ord(s[l]) - ord("A")] -= 1
                # Recalculate the maximum frequency within the window
                max_f = max(hsh)
                l += 1
            # Update the maximum length of the substring
            mx_len = max(mx_len, r - l + 1)
            r += 1
        return mx_len

    def __optimal(self, s: str, k: int) -> int:
        n: int = len(s)
        l = r = mx_len = max_f = 0
        hsh: List[int] = [0] * 26
        while r < n:
            # Update the frequency of the current character
            hsh[ord(s[r]) - ord("A")] += 1
            # Update the maximum frequency of characters seen so far
            max_f = max(max_f, hsh[ord(s[r]) - ord("A")])
            # If the number of character changes exceeds k, adjust the window
            if (r - l + 1) - max_f > k:
                hsh[ord(s[l]) - ord("A")] -= 1
                l += 1
            # Update the maximum length of the substring
            mx_len = max(mx_len, r - l + 1)
            r += 1
        return mx_len

    def characterReplacement(self, s: str, k: int) -> int:
        # Uncomment one of the following methods to use the desired approach
        # return self.__brute(s=s, k=k)  # Brute force approach
        # return self.__better(s=s, k=k)  # Optimized approach
        return self.__optimal(s=s, k=k)  # Optimal approach


if __name__ == "__main__":
    s: str = "AABABBA"
    k: int = 2
    solution: Solution = Solution()
    print(solution.characterReplacement(s=s, k=k))
