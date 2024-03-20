"""Check if a linked list is palindrome or not."""


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
    # prev is the current head so return it
    return prev


def add_one(head: Node) -> Node:
    if head is None:
        return head
    head = reverse_list(head=head)
    carry: int = 1
    temp: Node = head
    while temp:
        temp.data = temp.data + carry
        if temp.data < 10:
            carry = 0
            break
        else:
            temp.data = 0
            carry = 1
        temp = temp.next

    head = reverse_list(head)
    if carry:
        node = Node(carry)
        node.next = head
        head = node
    return head


def helper(node: Node) -> int:
    if node is None:
        return 1
    carry: int = helper(node=node.next)
    node.data = node.data + carry
    if node.data < 0:
        return 0
    node.data = 0
    return 1


def add_one_optimal(head: Node) -> Node:
    if head is None:
        return head
    carry: int = helper(head)
    if carry == 1:
        node = Node(carry)
        node.next = head
        head = node
    return head


if __name__ == "__main__":
    llist: SingleLinkedList = SingleLinkedList()
    print(llist.head)
    llist.add_data(9)
    llist.add_data(9)
    llist.add_data(9)
    llist.add_data(9)
    llist.print_list()
    # llist.head = add_one(head=llist.head)
    # llist.print_list()
    llist.head = add_one_optimal(head=llist.head)
    llist.print_list()
