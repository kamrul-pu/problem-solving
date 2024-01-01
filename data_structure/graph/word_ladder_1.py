"""Word ladder 1 using bfs."""
from collections import deque


def word_ladder_length(start_word: str, target_word: str, word_list: list[str]) -> int:
    q: deque = deque()
    q.append((start_word, 1))
    st: set = set()
    for item in word_list:
        st.add(item)
    if start_word in st:
        st.remove(start_word)
    while q:
        front: tuple = q.popleft()
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
    word_list: list[str] = ["hot", "dot", "dog", "lot", "log", "cog"]
    start_word: str = "hit"
    end_word: str = "cog"
    print(
        word_ladder_length(
            start_word=start_word, target_word=end_word, word_list=word_list
        )
    )
