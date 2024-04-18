"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""

from collections import defaultdict
from typing import DefaultDict, List, Tuple


class Solution:
    def __f(self, s1: str, s2: str) -> bool:
        n: int = len(s2)
        l: int = 0
        r: int = l + len(s1)
        hsh: DefaultDict[Tuple[int]] = defaultdict(int)

        # Sliding window approach to iterate through substrings of s2 of length equal to s1
        while r < n + 1:
            key: List[int] = [0] * 26

            # Count frequency of characters in the current substring of s2
            for i in range(l, r):
                key[ord(s2[i]) - ord("a")] += 1

            # Store the frequency count (key) in a defaultdict to track occurrences
            hsh[tuple(key)] += 1
            l += 1
            r += 1

        # Calculate the frequency count of characters in s1
        key_1: List[int] = [0] * 26
        for ch in s1:
            key_1[ord(ch) - ord("a")] += 1

        # Check if the frequency count of s1 exists in the defaultdict (hsh)
        return tuple(key_1) in hsh

    def __optimal(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Initialize frequency counts for characters in s1 and the first window of s2
        s1_count: List[int] = [0] * 26
        s2_count: List[int] = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches: int = 0

        # Check initial window of length s1 in s2
        for i in range(26):
            matches += 1 if s1_count[i] == s2_count[i] else 0

        l = 0
        # Slide the window over s2 and update frequency counts
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Add the new character at the right end of the window
            index: int = ord(s2[r]) - ord("a")
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            # Remove the character at the left end of the window
            index: int = ord(s2[l]) - ord("a")
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1

            l += 1

        return matches == 26

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # return self.__f(s1=s1, s2=s2)
        return self.__optimal(s1=s1, s2=s2)


if __name__ == "__main__":
    s1: str = "ab"
    # s1 = "adc"
    s2: str = "eidbaooo"
    # s2 = "eidboaoo"
    # s2 = "dcda"
    solution: Solution = Solution()
    print(solution.checkInclusion(s1=s1, s2=s2))
