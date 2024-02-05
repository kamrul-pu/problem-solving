"""Longest string chain dp problem."""

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        res = 1
        words.sort(key=lambda x: len(x))
        dp = {word: 1 for word in words}

        for i in range(1, len(words)):
            w = words[i]
            for j in range(len(w)):
                if w[:j] + w[j + 1 :] in dp:
                    dp[w] = max(dp[w], 1 + dp[w[:j] + w[j + 1 :]])
            res = max(res, dp[w])

        return res


if __name__ == "__main__":
    words: List[str] = ["a", "b", "ba", "bca", "bda", "bdca"]
    solution: Solution = Solution()
    print(solution.longestStrChain(words=words))
