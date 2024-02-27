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

from collections import deque
from typing import List, Deque, Set


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        # Create a set for quick word lookup
        word_set: Set = set(wordList)

        # Initialize a queue for BFS
        q: Deque = deque()

        # Start the queue with the initial word
        q.append([beginWord])

        # Keep track of words used on each level to avoid repeating them
        used_on_level: List[str] = []
        used_on_level.append(beginWord)

        # Initialize the current level
        level: int = 0

        # Initialize the list to store the resulting sequences
        ans: List[List[str]] = []

        while q:
            # Pop the first sequence from the queue
            front: List[str] = q.popleft()

            # Check if we are moving to the next level
            if len(front) > level:
                level += 1

                # Remove words used in the previous level from the word set
                for word in used_on_level:
                    if word in word_set:
                        word_set.remove(word)

            # Get the last word in the sequence
            word: str = front[-1]

            # Check if we have reached the endWord
            if word == endWord:
                # Check if this is the first sequence found or if it's as short as the ones found before
                if len(ans) == 0:
                    ans.append(front)
                elif len(ans[0]) == len(front):
                    ans.append(front)

            # Generate new words by changing one letter at a time
            for i in range(len(word)):
                for ch in range(ord("a"), ord("z") + 1):
                    new_word: str = word[:i] + chr(ch) + word[i + 1 :]
                    if new_word in word_set:
                        # Add the new word to the sequence and append it to the queue
                        front.append(new_word)
                        q.append(front.copy())
                        used_on_level.append(new_word)
                        front.pop()

        return ans


if __name__ == "__main__":
    word_list: List[str] = ["hot", "dot", "dog", "lot", "log", "cog"]
    begin_word: str = "hit"
    end_word: str = "cog"
    solution: Solution = Solution()

    # Print the shortest transformation sequences from beginWord to endWord
    print(
        solution.findLadders(beginWord=begin_word, endWord=end_word, wordList=word_list)
    )
