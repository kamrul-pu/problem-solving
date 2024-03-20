"""Doubly Linked List in python."""


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node = None
        self.prev: Node = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def insert_node(self, data: int) -> None:
        node: Node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        if self.head.data >= data:
            # insert at the begining
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif self.tail.data <= data:
            # insert at last
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            # insert in middle area by sorting them
            cur: Node = self.head
            while cur.next and cur.next.data < data:
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node

    def reverse_dl(self) -> None:
        # using stack swap by data
        stack: list[int] = []
        temp: Node = self.head
        while temp:
            stack.append(temp.data)
            temp = temp.next
        # insert the data back
        temp: Node = self.head
        while stack:
            temp.data = stack.pop()
            temp = temp.next

    def reverse_dlist(self) -> None:
        cur: Node = self.head
        while cur:
            tmp: Node = cur.next
            cur.next = cur.prev
            cur.prev = tmp
            cur = tmp
        # swap head and tail pointer
        self.head, self.tail = self.tail, self.head

    def print_list(self, reverse: bool = False) -> None:
        if reverse:
            node = self.tail
        else:
            node: Node = self.head
        while node:
            print(node.data, end="->")
            if reverse:
                node = node.prev
            else:
                node = node.next
        print("Null")


if __name__ == "__main__":
    elements: list[int] = [30, 10, 5, 2, 3, 10, 15, 20, 1]
    dll1: DoublyLinkedList = DoublyLinkedList()
    for element in elements:
        dll1.insert_node(element)

    dll1.print_list()
    # dll1.print_list(reverse=True)
    dll1.reverse_dlist()
    dll1.print_list()
    dll1.reverse_dlist()
    dll1.print_list()
