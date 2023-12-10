"""Singly linked list in python."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def add_data(self, data: int) -> None:
        node: Node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def add_data_sorted(self, data: int) -> None:
        node: Node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        if self.head.data >= data:
            # add as a first node and change the head reference
            node.next = self.head
            self.head = node
        elif self.tail.data <= data:
            # add the data at last position
            self.tail.next = node
            self.tail = node
        else:
            # need to store in the middle
            cur: Node = self.head
            while cur.next and cur.next.data < data:
                cur = cur.next

            node.next = cur.next
            cur.next = node

    def delete_node(self, data: int) -> None:
        if self.head is None:
            return "No element in the list"
        if self.head.data == data:
            self.head = self.head.next
            return "Node deleted"
        cur: Node = self.head
        prev: Node = self.head
        while cur and cur.data != data:
            prev = cur
            cur = cur.next

        if cur is None:
            return "Node is not in the list"
        if cur.data == self.tail.data:
            self.tail = prev
        prev.next = cur.next
        return "Node deleted!"

    def print_list(self) -> None:
        cur: Node = self.head
        while cur:
            print(cur.data, end="->")
            cur = cur.next
        print("Null")


if __name__ == "__main__":
    llist: SingleLinkedList = SingleLinkedList()
    print(llist.head)
    llist.add_data(10)
    llist.add_data(230)
    llist.add_data(20)
    llist.add_data(34)
    llist.add_data(5)
    llist.print_list()
    # add as a sorted list
    llist1: SingleLinkedList = SingleLinkedList()
    llist1.add_data_sorted(20)
    llist1.add_data_sorted(230)
    llist1.add_data_sorted(34)
    llist1.add_data_sorted(10)
    llist1.add_data_sorted(5)
    llist1.add_data_sorted(2)
    llist1.add_data_sorted(232)
    llist1.print_list()
    print(llist1.delete_node(2))
    llist1.print_list()
    print(llist1.delete_node(230))
    llist1.print_list()
    print(llist1.delete_node(232))
    llist1.print_list()
    print(llist1.delete_node(12))
    llist1.print_list()
