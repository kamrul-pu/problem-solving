"""Doubly Linked List in Python."""

from typing import List


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node = None
        self.prev: Node = None


class DoublyLinkedList:
    def __init__(self) -> None:
        """Initialize an empty Doubly Linked List."""
        self.head: Node = None
        self.tail: Node = None

    def insert_node(self, data: int) -> None:
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

    def find_data(self, data: int) -> bool:
        """
        Search for a node with the given data value in the Doubly Linked List.

        Parameters:
            data (int): The data value to search for.

        Returns:
            bool: True if the data is found, False otherwise.
        """
        if self.head is None:
            return False
        if self.head.data == data or self.tail.data == data:
            return True
        cur: Node = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def delete_node(self, data: int) -> str:
        """
        Delete a node with the given data value from the Doubly Linked List.

        Parameters:
            data (int): The data value of the node to be deleted.

        Returns:
            str: A message indicating the status of the deletion.
        """
        if self.head is None:
            return "No item in the list."
        if self.head.data == data:
            # Delete the head node
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return "Deleted successfully!"
        elif self.tail.data == data:
            # Delete the tail node
            tail: Node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            tail.prev = None
            return "Deleted successfully!"
        else:
            # Find and delete the node
            cur: Node = self.head
            while cur.next and cur.next.data != data:
                cur = cur.next
            if cur.next is None:
                return "Item is not in the list."
            else:
                temp: Node = cur.next
                cur.next = cur.next.next
                temp.next = None
                temp.prev = None
                if cur.next:
                    cur.next.prev = cur
                return "Deleted successfully!"

    def print_list(self, reverse: bool = False) -> None:
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
    dll.print_list()

    # Manually adding nodes to the Doubly Linked List
    node1: Node = Node(1)
    node2: Node = Node(2)
    node3: Node = Node(3)
    dll.head = node1
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    dll.tail = node3
    dll.print_list()
    dll.print_list(reverse=True)

    # Inserting elements into the Doubly Linked List
    elements: List[int] = [30, 10, 5, 2, 3, 10, 15, 20, 1]
    dll1: DoublyLinkedList = DoublyLinkedList()
    for element in elements:
        dll1.insert_node(element)

    dll1.print_list()
    dll1.print_list(reverse=True)

    # Searching for elements in the Doubly Linked List
    print(dll1.find_data(2))
    print(dll1.find_data(3))
    print(dll1.find_data(27))
    print(dll1.find_data(32))

    # Deleting elements from the Doubly Linked List
    print(dll1.delete_node(1))
    print(dll1.delete_node(30))
    dll1.print_list()
    dll1.print_list(reverse=True)
