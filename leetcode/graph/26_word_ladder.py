"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words
in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
"""

from collections import deque
from typing import Deque, List, Set, Tuple


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Initialize a queue for BFS traversal
        q: Deque = deque()

        # Append the starting word and its step count (1) to the queue
        q.append((beginWord, 1))

        # Initialize a set to store words from the wordList
        st: Set = set()

        # Add all words from wordList to the set
        for word in wordList:
            st.add(word)

        # Remove the starting word from the set if it exists
        if beginWord in st:
            st.remove(beginWord)

        # Perform BFS traversal
        while q:
            # Dequeue a word and its step count from the queue
            front: Tuple = q.popleft()
            word: str = front[0]
            steps: int = front[1]

            # If the dequeued word matches the target word, return the step count
            if word == endWord:
                return steps

            # Generate all possible one-letter mutations of the dequeued word
            for i in range(len(word)):
                for ch in range(ord("a"), ord("z") + 1):
                    new_word: str = word[:i] + chr(ch) + word[i + 1 :]

                    # If the mutated word is in the set, remove it and enqueue it with the updated step count
                    if new_word in st:
                        st.remove(new_word)
                        q.append((new_word, steps + 1))

        # If no transformation sequence exists, return 0
        return 0


if __name__ == "__main__":
    word_list: List[str] = ["hot", "dot", "dog", "lot", "log", "cog"]
    begin_word: str = "hit"
    end_word: str = "cog"
    solution: Solution = Solution()

    # Print the length of the shortest transformation sequence from beginWord to endWord
    print(
        solution.ladderLength(
            beginWord=begin_word, endWord=end_word, wordList=word_list
        )
    )
