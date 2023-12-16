"""Delete Middle Node in singly linked list."""


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


def delete_middle_node(head: Node) -> Node:
    if head is None:
        return None
    slow: Node = head
    fast: Node = head
    prev: Node = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next
    return head


def delete_middle_node2(head: Node) -> Node:
    if head is None:
        return None
    slow: Node = head
    fast: Node = head
    fast = fast.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    slow.next = slow.next.next

    return head


if __name__ == "__main__":
    llist: SingleLinkedList = SingleLinkedList()
    print(llist.head)
    nodes: list[int] = [1, 2, 3, 4, 5]
    for node in nodes:
        llist.add_data(node)
    llist.print_list()
    delete_middle_node2(head=llist.head)
    llist.print_list()
