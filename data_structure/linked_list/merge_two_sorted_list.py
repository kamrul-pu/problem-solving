"""Merged two sorted singly linked list."""

from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def add(self, data: int) -> None:
        node: Node = Node(data=data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def print_list(self) -> None:
        temp: Node = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")


def merge_two_sorted_list(
    head1: SinglyLinkedList, head2: SinglyLinkedList
) -> SinglyLinkedList:

    temp1: Node = head1.head
    temp2: Node = head2.head
    llist: SinglyLinkedList = SinglyLinkedList()

    while temp1 and temp2:
        if temp1.data < temp2.data:
            llist.add(data=temp1.data)
            temp1 = temp1.next
        else:
            llist.add(data=temp2.data)
            temp2 = temp2.next

    while temp2:
        llist.add(data=temp2.data)
        temp2 = temp2.next
    while temp1:
        llist.add(data=temp1.data)
        temp1 = temp1.next

    return llist


if __name__ == "__main__":
    llist1: SinglyLinkedList = SinglyLinkedList()
    llist2: SinglyLinkedList = SinglyLinkedList()
    llist1.add(data=1)
    llist1.add(data=2)
    llist1.add(data=4)
    llist2.add(data=1)
    llist2.add(data=3)
    llist2.add(data=4)

    llist1.print_list()
    llist2.print_list()

    llist: SinglyLinkedList = merge_two_sorted_list(head1=llist1, head2=llist2)
    llist.print_list()
