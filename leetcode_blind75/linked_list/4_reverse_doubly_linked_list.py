"""Revers doubly Linked list."""

"""Doubly Linked List in Python."""

from typing import List


class Node:
    def __init__(self, data: int, next=None, prev=None) -> None:
        self.data: int = data
        self.next: Node = next
        self.prev: Node = prev


class DoublyLinkedList:
    def __init__(self) -> None:
        """Initialize an empty Doubly Linked List."""
        self.head: Node = None
        self.tail: Node = None

    def insertNode(self, data: int) -> None:
        """
        Insert a node with the given data value into the Doubly Linked List.

        Parameters:
            data (int): The data value of the node to be inserted.
        """
        node: Node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        if self.head.data >= data:
            # insert at the beginning
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif self.tail.data <= data:
            # insert at the end
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            # insert in the middle by sorting
            cur: Node = self.head
            while cur.next and cur.next.data < data:
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node

    def reverseList(self) -> None:
        if self.head is None:
            return
        # Initialize pointers
        cur: Node = self.head  # Pointer to the current node (starts from head)
        last: Node = None  # Pointer to the previous node (initially None)
        while cur:
            # Update 'last' to point to the previous node of 'cur'
            last = cur.prev
            # Reverse the 'prev' and 'next' pointers of 'cur'
            cur.prev = cur.next
            cur.next = last
            # Move 'cur' to the next node
            cur = cur.prev
        # Update head and tail pointers
        self.tail = self.head
        self.head = last.prev

    def printList(self, reverse: bool = False) -> None:
        """
        Print the Doubly Linked List.

        Parameters:
            reverse (bool): Flag indicating whether to print the list in reverse order.
        """
        node: Node = self.tail if reverse else self.head
        while node:
            print(node.data, end="->")
            node = node.prev if reverse else node.next
        print("Null")


if __name__ == "__main__":
    # Test cases
    dll: DoublyLinkedList = DoublyLinkedList()
    # Inserting elements into the Doubly Linked List
    elements: List[int] = [30, 10, 5, 2, 3, 10, 15, 20, 1]
    dll1: DoublyLinkedList = DoublyLinkedList()
    for element in elements:
        dll.insertNode(element)
    dll.printList()
    dll.printList(reverse=True)
    dll.reverseList()
    dll.printList()
    dll.printList(reverse=True)
