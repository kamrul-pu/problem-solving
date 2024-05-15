"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
"""

from typing import Dict, List


class Node:
    def __init__(self) -> None:
        # Initialize a Node with a dictionary to store its children nodes
        self.children: Dict = dict()
        # 'eof' indicates whether the current node marks the end of a word
        self.eof: bool = False

    def add_word(self, word):
        # Method to add a word to the Trie
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = (
                    Node()
                )  # Create a new node if the character is not in the children
            cur = cur.children[c]
        cur.eof = True  # Mark the end of the word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Initialize the Trie with an empty root node
        root: Node = Node()

        # Add all words from the input list to the Trie
        for word in words:
            root.add_word(word=word)

        # Get the dimensions of the board
        rows, cols = len(board), len(board[0])
        # Initialize a set to store the found words
        res, visit = set(), set()

        def dfs(r, c, node: Node, word) -> None:
            # Depth-first search function to explore the board and find words
            if (
                r < 0
                or c < 0
                or r == rows
                or c == cols
                or (r, c) in visit
                or board[r][c] not in node.children
            ):
                # Base cases for terminating the search:
                # - Out of bounds
                # - Already visited
                # - Character not in the Trie
                return

            visit.add((r, c))  # Mark the current cell as visited
            node = node.children[
                board[r][c]
            ]  # Move to the corresponding node in the Trie
            word += board[r][c]  # Add the character to the current word
            if node.eof:
                res.add(
                    word
                )  # If the current node marks the end of a word, add it to the result set

            # Explore neighboring cells recursively
            dfs(r - 1, c, node, word)  # Up
            dfs(r + 1, c, node, word)  # Down
            dfs(r, c - 1, node, word)  # Left
            dfs(r, c + 1, node, word)  # Right

            visit.remove((r, c))  # Backtrack: mark the current cell as unvisited

        # Iterate through each cell in the board and start DFS from there
        for r in range(rows):
            for c in range(cols):
                dfs(
                    r, c, root, ""
                )  # Start DFS from the current cell with an empty word

        # Convert the result set to a list and return it
        return list(res)


# Test the solution
if __name__ == "__main__":
    board: List[List[str]] = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]

    words: List[str] = ["oath", "pea", "eat", "rain"]
    solution: Solution = Solution()
    result: List[str] = solution.findWords(board=board, words=words)
    print(result)
