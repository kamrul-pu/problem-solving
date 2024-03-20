"""Singly linked list Reverse."""


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

    def print_list(self) -> None:
        cur: Node = self.head
        while cur:
            print(cur.data, end="->")
            cur = cur.next
        print("Null")


def reverse_list(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    temp: Node = head
    prev: Node = None
    while temp:
        front: Node = temp.next
        temp.next = prev
        prev = temp
        temp = front

    return prev


def reverse_list_recursive(head: Node) -> None:
    if head is None or head.next is None:
        # for 0 or 1 node
        return head
    new_head: Node = reverse_list_recursive(head.next)
    front: Node = head.next
    front.next = head
    head.next = None

    return new_head


if __name__ == "__main__":
    llist: SingleLinkedList = SingleLinkedList()
    print(llist.head)
    llist.add_data(1)
    llist.add_data(2)
    llist.add_data(3)
    llist.add_data(4)
    llist.add_data(5)
    llist.print_list()
    llist.head = reverse_list(head=llist.head)
    llist.print_list()
    llist.head = reverse_list_recursive(llist.head)
    llist.print_list()
