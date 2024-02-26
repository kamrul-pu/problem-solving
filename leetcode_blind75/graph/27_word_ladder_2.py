"""
A transformation sequence from word beginWord to word endWord using a dictionary
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest
transformation sequences from beginWord to endWord,
or an empty list if no such sequence exists. Each sequence should be returned as a list of the words
[beginWord, s1, s2, ..., sk].
"""

from collections import defaultdict, deque
from typing import List, DefaultDict, Deque, Set


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        # Create a set for quick word lookup
        wordSet = set(wordList)

        # If endWord is not in the wordList, return an empty list
        if endWord not in wordSet:
            return []

        # Create a defaultdict to store word connections based on wildcard patterns
        graph: DefaultDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                graph[pattern].append(word)

        # Initialize a queue for BFS traversal
        q: Deque = deque()
        # Enqueue the starting word as the initial path
        q.append([beginWord])
        # Initialize a set to keep track of visited words
        visited: Set = set()
        # Mark the starting word as visited
        visited.add(beginWord)
        # Initialize a list to store the result paths
        result = []
        # Flag to indicate if endWord is found
        found = False

        # Perform BFS traversal
        while q and not found:
            # Get the number of paths at the current level
            level = len(q)
            # Set to keep track of visited words at the current level
            levelVisited: Set = set()
            # Process each path at the current level
            for _ in range(level):
                # Dequeue a path
                path = q.popleft()
                # Get the last word in the path
                word = path[-1]
                # Generate wildcard patterns for all possible transformations of the word
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1 :]
                    # Explore all words connected to the current word based on the wildcard pattern
                    for nextWord in graph[pattern]:
                        # If the nextWord is the endWord, add the path to the result
                        if nextWord == endWord:
                            found = True
                            result.append(path + [endWord])
                        # If the nextWord has not been visited, add it to the queue with the current path
                        elif nextWord not in visited:
                            levelVisited.add(nextWord)
                            q.append(path + [nextWord])
            # Mark all words visited at the current level
            visited |= levelVisited

        # Return the list of shortest transformation sequences from beginWord to endWord
        return result


if __name__ == "__main__":
    word_list: List[str] = ["hot", "dot", "dog", "lot", "log", "cog"]
    begin_word: str = "hit"
    end_word: str = "cog"
    solution: Solution = Solution()

    # Print the shortest transformation sequences from beginWord to endWord
    print(
        solution.findLadders(beginWord=begin_word, endWord=end_word, wordList=word_list)
    )
