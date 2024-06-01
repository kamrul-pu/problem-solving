"""
Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize variables to store the result
        res: str = ""
        res_len: int = 0

        # Get the length of the input string
        n: int = len(s)

        # Iterate through each character in the string
        for i in range(n):
            # Odd length palindrome: Expand around the current character
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                # Update result if the current palindrome is longer than the previous one
                if (r - l + 1) > res_len:
                    res = s[l : r + 1]
                    res_len = r - l + 1  # Update the length of the longest palindrome
                # Expand the palindrome window
                l -= 1
                r += 1

            # Even length palindrome: Expand around current and next characters
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l : r + 1]
                    res_len = r - l + 1  # Update the length of the longest palindrome
                # Expand the palindrome window
                l -= 1
                r += 1

        return res


if __name__ == "__main__":
    # Test the solution
    s: str = "babad"
    solution: Solution = Solution()
    print(solution.longestPalindrome(s=s))
