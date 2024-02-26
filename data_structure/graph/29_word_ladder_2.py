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
from typing import Deque, List, Set


def word_ladder_sequence(
    start_word: str, target_word: str, word_list: List[str]
) -> List[List[str]]:
    q: Deque = deque()
    q.append([start_word])
    st: Set = set()
    for item in word_list:
        st.add(item)
    # if start_word in st:
    #     st.remove(start_word)
    used_on_level: List[str] = [start_word]
    level: int = 0
    ans: List[List[str]] = []
    while q:
        front: List[str] = q.popleft()
        if len(front) > level:
            level += 1
            for it in used_on_level:
                if it in st:
                    st.remove(it)
        word: str = front[-1]
        if word == target_word:
            if len(ans) == 0:
                ans.append(front)
            elif len(ans[0]) == len(front):
                ans.append(front)

        for i in range(len(word)):
            for ch in range(ord("a"), ord("z") + 1):
                new_word: str = word[:i] + chr(ch) + word[i + 1 :]
                if new_word in st:
                    front.append(new_word)
                    q.append(front.copy())
                    front.pop()

    return ans


if __name__ == "__main__":
    word_list: List[str] = ["put", "bot", "pot", "poz", "coz"]
    start_word: str = "bat"
    end_word: str = "coz"
    ladder_sequence: List[List[str]] = word_ladder_sequence(
        start_word=start_word, target_word=end_word, word_list=word_list
    )
    print(ladder_sequence)
