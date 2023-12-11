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

    def find_data(self, data: int) -> bool:
        if self.head is None:
            return False
        if self.head.data == data:
            return True
        elif self.tail.data == data:
            return True
        else:
            cur: Node = self.head
            while cur:
                if cur.data == data:
                    return True
                cur = cur.next

        return False

    def delete_node(self, data: int) -> None:
        if self.head is None:
            return "No Item in the list."
        if self.head.data == data:
            # need to delete the head element
            self.head.prev = None
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return "Delete successfully!"
        elif self.tail.data == data:
            # delete the tail data
            self.tail = self.tail.prev
            self.tail.next = None
            return "Delete Successfully!"
        else:
            # find and delete the node.
            cur: Node = self.head
            while cur.next and cur.next.data != data:
                cur = cur.next

            if cur.next is None:
                return "Item is not in the list"
            else:
                cur.next = cur.next.next
                if cur.next.prev:
                    cur.next.prev = cur
                return "Deleted Successfully!"

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
    dll: DoublyLinkedList = DoublyLinkedList()
    dll.print_list()
    # add data manually to the doubly linked list
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
    elements: list[int] = [30, 10, 5, 2, 3, 10, 15, 20, 1]
    dll1: DoublyLinkedList = DoublyLinkedList()
    for element in elements:
        dll1.insert_node(element)

    dll1.print_list()
    dll1.print_list(reverse=True)

    print(dll1.find_data(2))
    print(dll1.find_data(3))
    print(dll1.find_data(27))
    print(dll1.find_data(32))
    print(dll1.delete_node(1))
    print(dll1.delete_node(30))
    dll1.print_list()
    dll1.print_list(reverse=True)
    print(dll1.delete_node(22))
    print(dll1.delete_node(5))
    print(dll1.delete_node(10))
    print(dll1.delete_node(10))
    print(dll1.delete_node(15))
    print(dll1.delete_node(3))
    print(dll1.delete_node(2))
    print(dll1.delete_node(21))
    print(dll1.delete_node(20))
    dll1.print_list()
    dll1.print_list(reverse=True)
