"""Singly linked Add two lists numbers."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def print_list(self) -> None:
        cur: Node = self.head
        while cur:
            print(cur.data, end="->")
            cur = cur.next
        print("Null")


def add_two_list(l1: SingleLinkedList, l2: SingleLinkedList) -> SingleLinkedList:
    carry: int = 0
    dummy_node: Node = Node(-1)
    cur: Node = dummy_node
    t1 = l1.head
    t2 = l2.head

    while t1 is not None or t2 is not None:
        total: int = carry
        if t1:
            total += t1.data
            t1 = t1.next
        if t2:
            total += t2.data
            t2 = t2.next
        data: int = total % 10
        carry = total // 10
        cur.next = Node(data)
        cur = cur.next
    if carry:
        cur.next = Node(carry)
    new_list: SingleLinkedList = SingleLinkedList()
    new_list.head = dummy_node.next
    return new_list


if __name__ == "__main__":
    l1: SingleLinkedList = SingleLinkedList()
    l1.head = Node(3)
    l1.head.next = Node(5)
    l2: SingleLinkedList = SingleLinkedList()
    l2.head = Node(4)
    l2.head.next = Node(5)
    l2.head.next.next = Node(9)
    l2.head.next.next.next = Node(9)
    l1.print_list()
    l2.print_list()
    l3: SingleLinkedList = add_two_list(l1, l2)
    l3.print_list()
