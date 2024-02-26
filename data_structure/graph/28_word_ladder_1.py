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


def word_ladder_length(start_word: str, target_word: str, word_list: List[str]) -> int:
    q: Deque = deque()
    q.append((start_word, 1))
    st: Set = set()
    for item in word_list:
        st.add(item)
    if start_word in st:
        st.remove(start_word)
    while q:
        front: Tuple = q.popleft()
        word: str = front[0]
        steps: int = front[1]
        if word == target_word:
            return steps
        for i in range(len(word)):
            for ch in range(ord("a"), ord("z") + 1):
                new_word = word[:i] + chr(ch) + word[i + 1 :]
                if new_word in st:
                    st.remove(new_word)
                    q.append((new_word, steps + 1))
    return 0


if __name__ == "__main__":
    word_list: List[str] = ["hot", "dot", "dog", "lot", "log", "cog"]
    start_word: str = "hit"
    end_word: str = "cog"
    ladder_cnt: int = word_ladder_length(
        start_word=start_word, target_word=end_word, word_list=word_list
    )
    print(ladder_cnt)
