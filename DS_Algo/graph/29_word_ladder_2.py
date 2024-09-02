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
from typing import Deque, List, Set, Dict


class Solution:
    def __dfs(
        self,
        word: str,
        sequence: List[str],
        beginWord: str,
        ans: List[List[str]],
        mpp: Dict[str, int],
    ) -> None:
        """
        Depth-First Search (DFS) to find all possible paths from endWord to beginWord.

        Args:
        word: The current word in the transformation sequence.
        sequence: The current sequence of words.
        beginWord: The start word of the transformation.
        ans: List to store all valid sequences.
        mpp: Dictionary mapping words to their level/steps in the transformation.

        This function builds the path from the endWord back to the beginWord using DFS.
        """
        # Base case: if the current word is the beginning word, reverse the sequence and add it to the answer.
        if word == beginWord:
            ans.append(list(reversed(sequence)))
            return

        # Get the number of steps required to reach the current word.
        steps: int = mpp[word]

        # Try all possible one-letter transformations of the current word.
        for i in range(len(word)):
            for ch in range(ord("a"), ord("z") + 1):
                new_word: str = word[:i] + chr(ch) + word[i + 1 :]

                # If the transformed word is in the map and is one step before the current word, proceed.
                if new_word in mpp and mpp[new_word] + 1 == steps:
                    sequence.append(new_word)
                    self.__dfs(new_word, sequence, beginWord, ans, mpp)
                    sequence.pop()

    def __find_ladders_optimal(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        """
        Find the shortest transformation sequences from beginWord to endWord.

        Args:
        beginWord: The start word of the transformation.
        endWord: The target word of the transformation.
        wordList: List of words to use for transformations.

        Returns:
        A list of lists, where each list is a valid transformation sequence.
        """
        # Initialize a dictionary to store the level of each word in the BFS.
        mpp: Dict[str, int] = dict()
        # Create a set for fast lookup of words.
        word_set: Set[str] = set(wordList)
        q: Deque[str] = deque()
        q.append(beginWord)
        mpp[beginWord] = 1
        n: int = len(beginWord)

        # Remove the beginWord from the word set if it's present.
        if beginWord in word_set:
            word_set.remove(beginWord)

        # Perform BFS to determine the shortest path lengths to each word.
        while q:
            word: str = q.popleft()
            steps: int = mpp[word]

            # If we reached the endWord, stop the BFS.
            if word == endWord:
                break

            # Try all possible one-letter transformations of the current word.
            for i in range(n):
                for ch in range(ord("a"), ord("z") + 1):
                    new_word: str = word[:i] + chr(ch) + word[i + 1 :]

                    # If the transformed word is in the word set, update its level and enqueue it.
                    if new_word in word_set:
                        q.append(new_word)
                        word_set.remove(new_word)
                        mpp[new_word] = steps + 1

        ans: List[List[str]] = []

        # If the endWord is reachable, use DFS to find all possible transformation sequences.
        if endWord in mpp:
            sequence: List[str] = []
            sequence.append(endWord)
            self.__dfs(
                word=endWord, sequence=sequence, beginWord=beginWord, ans=ans, mpp=mpp
            )

        return ans

    def __find_ladders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        """
        Find the shortest transformation sequences from beginWord to endWord using BFS.

        Args:
        beginWord: The start word of the transformation.
        endWord: The target word of the transformation.
        wordList: List of words to use for transformations.

        Returns:
        A list of lists, where each list is a valid transformation sequence.
        """
        # Initialize a set of words for quick lookup.
        words: Set[str] = set(wordList)
        q: Deque[List[str]] = deque()
        q.append([beginWord])
        level: int = 0
        used: Set[str] = set()
        used.add(beginWord)
        ans: List[List[str]] = []

        # Perform BFS to explore all possible sequences.
        while q:
            front: List[str] = q.popleft()

            # When the length of the sequence increases, update the level and clear used set.
            if len(front) > level:
                level += 1
                for it in used:
                    if it in words:
                        words.remove(it)
                used.clear()

            # Get the last word in the current sequence.
            word: str = front[-1]

            # If we reached the endWord, add the sequence to the result list.
            if word == endWord:
                if len(ans) == 0:
                    ans.append(front)
                elif len(ans[0]) == len(front):
                    ans.append(front)

            # Try all possible one-letter transformations of the current word.
            for i in range(len(word)):
                for ch in range(ord("a"), ord("z") + 1):
                    new_word: str = word[:i] + chr(ch) + word[i + 1 :]

                    # If the transformed word is in the set, add it to the sequence and enqueue it.
                    if new_word in words:
                        used.add(new_word)
                        q.append(front + [new_word])

        return ans

    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        """
        Public method to find the shortest transformation sequences from beginWord to endWord.

        Args:
        beginWord: The start word of the transformation.
        endWord: The target word of the transformation.
        wordList: List of words to use for transformations.

        Returns:
        A list of lists, where each list is a valid transformation sequence.
        """
        return self.__find_ladders(
            beginWord=beginWord, endWord=endWord, wordList=wordList
        )
        # Alternatively, use the optimal solution:
        # return self.__find_ladders_optimal(
        #     beginWord=beginWord, endWord=endWord, wordList=wordList
        # )


if __name__ == "__main__":
    word_list: List[str] = ["pat", "bot", "pot", "poz", "coz"]
    start_word: str = "bat"
    end_word: str = "coz"
    solution: Solution = Solution()
    ladder_sequence: List[List[str]] = solution.findLadders(
        start_word, end_word, word_list
    )
    print(ladder_sequence)
