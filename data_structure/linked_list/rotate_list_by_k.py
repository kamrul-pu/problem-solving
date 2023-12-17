"""Singly linked list Rotate by k."""


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


def find_nth_node(temp, k) -> Node:
    cnt: int = 1
    while temp:
        if cnt == k:
            return temp
        cnt += 1
        temp = temp.next
    return temp


def rotate_by_k(head: Node, k: int) -> Node:
    if head is None:
        return None
    cnt: int = 1
    tail: Node = head
    while tail.next:
        cnt += 1
        tail = tail.next
    if k % cnt == 0:
        return head, tail
    k = k % cnt
    tail.next = head
    new_last_node: Node = find_nth_node(temp=head, k=cnt - k)
    head = new_last_node.next
    tail = new_last_node
    new_last_node.next = None
    return head, tail


if __name__ == "__main__":
    llist: SingleLinkedList = SingleLinkedList()
    print(llist.head)
    llist.add_data(1)
    llist.add_data(2)
    llist.add_data(3)
    llist.add_data(4)
    llist.add_data(5)
    llist.print_list()

    llist.head, llist.tail = rotate_by_k(head=llist.head, k=6)
    llist.print_list()
