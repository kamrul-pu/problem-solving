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

    def print_list(self) -> None:
        cur: Node = self.head
        while cur:
            print(cur.data, end="->")
            cur = cur.next
        print("Null")


def sort_0_1_2(root: Node) -> Node:
    # Brute force solution using data replacement
    if root is None:
        return root
    cnt_0: int = 0
    cnt_1: int = 0
    cnt_2: int = 0
    temp: Node = root
    while temp:
        if temp.data == 0:
            cnt_0 += 1
        elif temp.data == 1:
            cnt_1 += 1
        else:
            cnt_2 += 1
        temp = temp.next

    temp: Node = root
    while cnt_0:
        temp.data = 0
        temp = temp.next
        cnt_0 -= 1
    while cnt_1:
        temp.data = 1
        temp = temp.next
        cnt_1 -= 1
    while cnt_2:
        temp.data = 2
        temp = temp.next
        cnt_2 -= 1

    return root


def sort_0_1_2_optimal(root: Node) -> Node:
    # list is empty or their is only a single element in the list
    if root is None or root.next is None:
        return root
    zero_head = zero = Node(-1)
    one_head = one = Node(-1)
    two_head = two = Node(-1)
    temp: Node = root
    while temp:
        if temp.data == 0:
            zero.next = temp
            zero = temp
        elif temp.data == 1:
            one.next = temp
            one = temp
        else:
            two.next = temp
            two = temp
        temp = temp.next

    if one_head.next:
        zero.next = one_head.next
    else:
        zero.next = two_head.next
    one.next = two_head.next
    two.next = None
    new_head = zero_head.next
    return new_head


if __name__ == "__main__":
    llist: SingleLinkedList = SingleLinkedList()
    print(llist.head)
    llist.add_data(1)
    llist.add_data(0)
    llist.add_data(1)
    llist.add_data(2)
    llist.add_data(0)
    llist.add_data(2)
    llist.add_data(1)
    llist.print_list()
    # llist.head = sort_0_1_2(root=llist.head)
    # llist.print_list()
    llist.head = sort_0_1_2_optimal(root=llist.head)
    llist.print_list()
