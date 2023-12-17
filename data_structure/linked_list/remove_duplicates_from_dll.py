"""Removes duplicates from  doubly linked list."""


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


def remove_duplicates(head: Node, tail: Node) -> (Node, Node):
    temp: Node = head
    while temp and temp.next:
        next_node: Node = temp.next
        # traverse while they are same
        while next_node and next_node.data == temp.data:
            next_node = next_node.next

        temp.next = next_node
        if next_node:
            next_node.prev = temp
        # Update the tail pointer if it is last node
        if temp.next is None:
            tail = temp
        temp = temp.next

    return head, tail


if __name__ == "__main__":
    dll: DoublyLinkedList = DoublyLinkedList()
    elements: list[int] = [3, 1, 2, 1, 3, 4, 1, 4]
    for element in elements:
        dll.insert_node(element)

    dll.print_list()
    dll.print_list(reverse=True)

    dll.head, dll.tail = remove_duplicates(head=dll.head, tail=dll.tail)
    dll.print_list()
    dll.print_list(reverse=True)
