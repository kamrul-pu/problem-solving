"""Word ladder 2 using bfs."""
from collections import deque


def word_ladder_sequence(
    start_word: str, target_word: str, word_list: list[str]
) -> list[list[str]]:
    q: deque = deque()
    q.append([start_word])
    st: set = set()
    for item in word_list:
        st.add(item)
    # if start_word in st:
    #     st.remove(start_word)
    used_on_level: list[str] = [start_word]
    level: int = 0
    ans: list[list[str]] = []
    while q:
        front: list[str] = q.popleft()
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
    word_list: list[str] = ["put", "bot", "pot", "poz", "coz"]
    start_word: str = "bat"
    end_word: str = "coz"
    ladder_sequence: list[list[str]] = word_ladder_sequence(
        start_word=start_word, target_word=end_word, word_list=word_list
    )
    print(ladder_sequence)
