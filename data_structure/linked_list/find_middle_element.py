"""Find the middle Element in the singly linked list."""


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


def find_middle(head: Node) -> Node:
    if head is None:
        return None
    nodes: list[Node] = []
    temp: Node = head
    cnt: int = 0
    while temp:
        nodes.append(temp)
        temp = temp.next
        cnt += 1

    return nodes[cnt // 2]


def find_middle1(head: Node) -> None:
    if head is None:
        return None

    cnt: int = 0
    temp: Node = head
    while temp:
        cnt += 1
        temp = temp.next

    mid: int = cnt // 2
    temp: Node = head
    while mid:
        temp = temp.next
        mid -= 1

    return temp


def find_middle_optimal(head: Node) -> Node:
    if head is None:
        return None
    fast: Node = head
    slow: Node = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


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
    middle: Node = find_middle(head=llist.head)
    print(middle)
    print(middle.data)
    print(find_middle1(head=llist.head))
    print(find_middle_optimal(head=llist.head))
