"""Group Odd even index nodes."""


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node = None


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

    def odd_even_group(self) -> None:
        numbers: list[int] = []
        tmp: Node = self.head
        while tmp:
            numbers.append(tmp.data)
            if tmp.next:
                tmp = tmp.next.next
            else:
                tmp = tmp.next

        tmp = self.head.next
        while tmp:
            numbers.append(tmp.data)
            if tmp.next:
                tmp = tmp.next.next
            else:
                tmp = tmp.next
        cur: Node = self.head
        for data in numbers:
            cur.data = data
            cur = cur.next

    def odd_even_group_optimal(self) -> None:
        if self.head is None or self.head.next is None:
            return

        odd: Node = self.head
        even: Node = self.head.next
        even_head: Node = self.head.next

        while even != None and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = even_head

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
    llist.add_data(6)
    llist.print_list()
    # llist.odd_even_group()
    llist.odd_even_group_optimal()
    llist.print_list()
