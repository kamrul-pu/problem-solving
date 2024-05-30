"""
There is a foreign language language which uses the latin alphabet,
but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary,
where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid,
return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
There is no index i such that a[i] != b[i] and a.length < b.length.
"""

from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Create an adjacency dictionary to store character relationships
        adjacency = {char: set() for word in words for char in word}

        # Build the adjacency dictionary by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))

            # If a shorter word is a prefix of a longer word, return empty string
            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return ""

            # Compare characters in corresponding positions of adjacent words
            for j in range(min_length):
                if word1[j] != word2[j]:
                    adjacency[word1[j]].add(word2[j])
                    break

        # Dictionary to keep track of visited characters during DFS
        visited = {}  # False = visited, True = in current path
        result = []

        # Depth-first search to determine the order of characters
        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = True
            for neighbor in adjacency[char]:
                if dfs(neighbor):
                    return True
            visited[char] = False
            result.append(char)

        # Perform DFS for each character in the adjacency dictionary
        for char in adjacency:
            if dfs(char):
                return ""  # If there's a cycle, return empty string

        # Reverse the result and concatenate characters to form the final order
        result.reverse()
        return "".join(result)


if __name__ == "__main__":
    words: List[str] = ["hrn", "hrf", "er", "enn", "rfnn"]
    solution: Solution = Solution()
    result: str = solution.foreignDictionary(words=words)
    print(result)
