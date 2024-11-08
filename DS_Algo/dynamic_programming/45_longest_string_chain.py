"""Longest string chain dp problem."""

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Initialize the result to keep track of the longest chain length found.
        res = 1

        # Sort words by length. This ensures that shorter words are processed first,
        # allowing us to build chains by adding one character at a time.
        words.sort(key=lambda x: len(x))

        # Initialize a dictionary `dp` where each word is mapped to the length of
        # the longest chain ending with that word. Initially, each word has a chain length of 1.
        dp = {word: 1 for word in words}

        # Iterate over each word in the sorted list.
        for i in range(1, len(words)):
            w = words[i]  # Current word being considered for chain extension.

            # Try removing each character from the current word to find predecessors.
            for j in range(len(w)):
                # Form a predecessor by removing the character at position `j`.
                predecessor = w[:j] + w[j + 1 :]

                # If the predecessor exists in `dp`, it means we can extend a chain to the current word.
                if predecessor in dp:
                    # Update the chain length for the current word `w` in `dp`.
                    # This is done by taking the maximum between the existing length of `dp[w]`
                    # and the length of the chain ending at `predecessor` + 1 (adding `w` to the chain).
                    dp[w] = max(dp[w], 1 + dp[predecessor])

            # Update the result with the maximum chain length found so far.
            res = max(res, dp[w])

        # Return the longest chain length found.
        return res


# Example usage
if __name__ == "__main__":
    words: List[str] = ["a", "b", "ba", "bca", "bda", "bdca"]
    solution: Solution = Solution()
    print(solution.longestStrChain(words=words))
