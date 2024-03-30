"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.
"""

from typing import List


class Solution:
    def __brute(self, s: str) -> int:
        n: int = len(s)
        max_len: int = 0
        for i in range(n):
            hsh: List[int] = [0] * 3
            for j in range(i, n):
                # Initialize an array to track whether each character has occurred
                hsh[ord(s[j]) - ord("a")] = 1
                # Check if all characters 'a', 'b', and 'c' have occurred at least once
                if hsh[0] + hsh[1] + hsh[2] == 3:
                    max_len += 1

        return max_len

    def __better(self, s: str) -> int:
        n: int = len(s)
        max_len: int = 0
        for i in range(n):
            hsh: List[int] = [0] * 3
            for j in range(i, n):
                hsh[ord(s[j]) - ord("a")] = 1
                # If all characters have occurred at least once, count substrings
                if hsh[0] + hsh[1] + hsh[2] == 3:
                    max_len += n - j
                    break

        return max_len

    def __optimal(self, s: str) -> int:
        n: int = len(s)
        cnt: int = 0
        last_seen: List[int] = [
            -1
        ] * 3  # Initialize a list to track the last occurrence index of each character
        for i in range(n):
            last_seen[ord(s[i]) - ord("a")] = (
                i  # Update the last occurrence index of the current character
            )
            # Check if all characters 'a', 'b', and 'c' have occurred at least once
            if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
                # Increment count by the minimum of last_seen indices + 1
                cnt += 1 + min(last_seen)

        return cnt

    def numberOfSubstrings(self, s: str) -> int:
        # return self.__brute(s=s)  # Uncomment to use the brute force approach
        # return self.__better(s=s)  # Uncomment to use the optimized brute force approach
        return self.__optimal(s=s)  # Use the optimal approach


if __name__ == "__main__":
    s: str = "abcabc"
    solution: Solution = Solution()
    print(solution.numberOfSubstrings(s=s))
