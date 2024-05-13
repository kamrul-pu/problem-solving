"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in
a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix,
and false otherwise.
"""

from typing import Dict


class Node:
    def __init__(self) -> None:
        # Initialize a Node with a dictionary to store its children nodes
        self.children: Dict = dict()
        # 'end_of_word' indicates whether the current node marks the end of a word
        self.end_of_word: bool = False


class Trie:

    def __init__(self):
        # Initialize the Trie with a root node
        self.root: Node = Node()

    def insert(self, word: str) -> None:
        cur: Node = self.root  # Start from the root

        # Traverse through each character in the word
        for c in word:
            # If the character is not in the current node's children, add it
            if c not in cur.children:
                cur.children[c] = Node()
            # Move to the child node corresponding to the current character
            cur = cur.children[c]

        # Mark the end of the word by setting 'end_of_word' to True
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur: Node = self.root  # Start from the root

        # Traverse through each character in the word
        for c in word:
            # If the character is not in the current node's children, the word is not in the trie
            if c not in cur.children:
                return False
            # Move to the child node corresponding to the current character
            cur = cur.children[c]

        # Check if the end of the word is marked in the trie
        return cur.end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur: Node = self.root  # Start from the root

        # Traverse through each character in the prefix
        for c in prefix:
            # If the character is not in the current node's children, the prefix is not in the trie
            if c not in cur.children:
                return False
            # Move to the child node corresponding to the current character
            cur = cur.children[c]

        # If all characters in the prefix are found in the trie, return True
        return True


if __name__ == "__main__":
    trie: Trie = Trie()
    print(trie.insert("apple"))  # Insert "apple" into the trie
    print(trie.search("apple"))  # Check if "apple" is in the trie (should return True)
    print(trie.search("app"))  # Check if "app" is in the trie (should return False)
    print(
        trie.startsWith("app")
    )  # Check if there is a word in the trie starting with "app" (should return True)
    print(trie.insert("app"))  # Insert "app" into the trie
    print(trie.search("app"))  # Check if "app" is in the trie (should return True)
