"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise,
add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""

from typing import Dict, Optional


class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key: int = key
        self.val: int = val
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: Dict[int, Node] = {}  # Dictionary to store key-node mappings
        self.left: Optional[Node] = Node(
            0, 0
        )  # Dummy head node for the least recently used (LRU) end
        self.right: Optional[Node] = Node(
            0, 0
        )  # Dummy tail node for the most recently used (MRU) end
        self.left.next = self.right  # Connect left to right
        self.right.prev = self.left  # Connect right to left

    def remove(self, node: Optional[Node]) -> None:
        # Remove a node from the linked list
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node: Optional[Node]) -> None:
        # Insert a node at the end of the linked list (most recently used position)
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Key exists in the cache, update its position to most recently used
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Key already exists, update its value and move to most recently used position
            self.remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            # Cache is full, evict the least recently used item (from the front of the linked list)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        # Insert the new node with the updated value at the end of the linked list (most recently used position)
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)


if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    capacity: int = 2
    obj = LRUCache(capacity)
    print(obj.put(1, 1))
    print(obj.put(2, 2))
    param_1 = obj.get(1)
    print(param_1)
    print(obj.put(3, 3))
    param_1 = obj.get(2)
    print(param_1)
    print(obj.put(4, 4))
    param_1 = obj.get(1)
    print(param_1)
    param_1 = obj.get(3)
    print(param_1)
    param_1 = obj.get(4)
    print(param_1)
