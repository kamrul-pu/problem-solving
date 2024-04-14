"""Word break problem."""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Function to determine if a string can be segmented into space-separated words,
        where each word is in the dictionary.

        Args:
            s (str): The string to be segmented.
            wordDict (List[str]): List of words in the dictionary.

        Returns:
            bool: True if the string can be segmented, False otherwise.
        """
        n: int = len(s)
        # Convert wordDict to a set for O(1) lookup time.
        word_set = set(wordDict)
        # Initialize dynamic programming array with True for the empty string.
        dp: List[bool] = [True] + [False] * n
        for i in range(n):
            for j in range(i, n):
                # If substring s[i:j+1] is in the word dictionary, mark dp[j+1] as True.
                if s[i : j + 1] in word_set:
                    dp[j + 1] = dp[i] or dp[j + 1]
        return dp[-1]


if __name__ == "__main__":
    s: str = "leetcode"
    wordDict: List[str] = ["leet", "code"]
    solution: Solution = Solution()
    print(solution.wordBreak(s=s, wordDict=wordDict))
