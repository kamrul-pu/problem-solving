"""Singly linked list Reverse in k group."""


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


def get_kth_node(temp: Node, k: int) -> Node | None:
    k -= 1
    while temp and k > 0:
        k -= 1
        temp = temp.next
    return temp


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


def k_reverse(head: Node, k: int) -> Node:
    temp: Node = head
    prev_last: Node = None
    while temp:
        kth_node = get_kth_node(temp=temp, k=k)
        if kth_node is None:
            if prev_last:
                prev_last.next = temp
            break
        next_node: Node = kth_node.next
        kth_node.next = None
        reverse_list(temp)
        if temp == head:
            head = kth_node
        else:
            prev_last.next = kth_node

        prev_last = temp
        temp = next_node

    return head


if __name__ == "__main__":
    llist: SingleLinkedList = SingleLinkedList()
    print(llist.head)
    for i in range(1, 11):
        llist.add_data(i)
    llist.print_list()
    llist.head = k_reverse(head=llist.head, k=3)
    llist.print_list()
