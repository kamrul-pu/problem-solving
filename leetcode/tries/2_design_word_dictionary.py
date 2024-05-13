"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.
"""

from typing import Dict, Optional


class Node:
    def __init__(self) -> None:
        # Each node represents a character in the word
        # 'children' is a dictionary mapping characters to their corresponding child nodes
        self.children: Dict[str, Optional[Node]] = dict()
        # 'eof' (end of word) is a flag indicating whether the current node represents the end of a word
        self.eof: bool = False


class WordDictionary:
    def __init__(self):
        # Initialize the root node of the trie
        self.root: Node = Node()

    def addWord(self, word: str) -> None:
        cur: Node = self.root

        # Traverse through each character in the word
        for c in word:
            # If the character is not already present in the trie, add a new node for it
            if c not in cur.children:
                cur.children[c] = Node()
            # Move to the next node
            cur = cur.children[c]

        # Mark the end of the word
        cur.eof = True

    def search(self, word: str) -> bool:

        # Define a helper function for depth-first search
        def dfs(j: int, root: Node):
            cur: Node = root
            # Traverse through the characters in the word starting from index j
            for i in range(j, len(word)):
                c = word[i]
                # If the character is a '.', explore all possible children
                if c == ".":
                    for child in cur.children.values():
                        # Recursively search for the remaining characters in the word
                        if dfs(i + 1, child):
                            return True
                    # If no match is found, return False
                    return False
                else:
                    # If the character is not a '.', check if it exists in the children of the current node
                    if c not in cur.children:
                        return False
                    # Move to the next node
                    cur = cur.children[c]

            # Return True if the current node marks the end of a word, otherwise False
            return cur.eof

        # Start the depth-first search from the root node
        return dfs(0, self.root)


if __name__ == "__main__":
    # Create an instance of the WordDictionary class
    word_dictionary: WordDictionary = WordDictionary()
    # Add words to the dictionary
    print(word_dictionary.addWord("bad"))
    print(word_dictionary.addWord("mad"))
    print(word_dictionary.addWord("dad"))
    # Search for words in the dictionary
    print(word_dictionary.search("pad"))
    print(word_dictionary.search("bad"))
    print(word_dictionary.search(".ad"))
    print(word_dictionary.search("b.."))
