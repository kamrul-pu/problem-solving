"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        # Initialize variable to store the count of palindromic substrings
        palindrom: int = 0

        # Get the length of the input string
        n: int = len(s)

        # Iterate through each character in the string
        for i in range(n):
            # Odd length palindrome: Expand around the current character
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                # Increment the count for each palindromic substring found
                palindrom += 1
                # Expand the palindrome window
                l -= 1
                r += 1

            # Even length palindrome: Expand around current and next characters
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                # Increment the count for each palindromic substring found
                palindrom += 1
                # Expand the palindrome window
                l -= 1
                r += 1

        return palindrom


if __name__ == "__main__":
    # Test the solution
    s: str = "abc"
    solution: Solution = Solution()
    print(solution.countSubstrings(s=s))
