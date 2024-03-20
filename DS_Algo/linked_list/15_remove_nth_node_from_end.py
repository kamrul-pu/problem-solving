"""Singly linked list Remove nth node from the end."""


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


def delete_nth_back_node(head: Node, n: int) -> Node:
    if head is None:
        return head
    cnt: int = 0
    temp: Node = head
    while temp:
        cnt += 1
        temp = temp.next
    if cnt == n:
        head = head.next
        return head
    if n > 5:
        print("Invalid index")
        return head
    target: int = cnt - n - 1
    temp: Node = head

    while target:
        temp = temp.next
        target -= 1
    temp.next = temp.next.next
    return head


def del_node_from_back(head: Node, n: int) -> Node:
    if head is None:
        return None
    first: Node = head
    slow: Node = head
    for i in range(n):
        if first.next:
            first = first.next
        else:
            print("Invalid index")
            return head

    while first.next:
        first = first.next
        slow = slow.next
    # print("F", first.data)
    print("S", slow.data)
    if slow == head:
        head = head.next
        return head
    slow.next = slow.next.next
    return head


if __name__ == "__main__":
    llist: SingleLinkedList = SingleLinkedList()
    print(llist.head)
    llist.add_data(1)
    llist.add_data(2)
    llist.add_data(3)
    llist.add_data(4)
    llist.add_data(5)
    # llist.add_data(6)
    # llist.add_data(7)
    llist.print_list()
    # llist.head = delete_nth_back_node(llist.head, 2)
    llist.head = del_node_from_back(head=llist.head, n=1)
    llist.print_list()
