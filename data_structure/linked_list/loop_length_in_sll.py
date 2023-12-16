"""Find Loop length in singly linked list."""
from collections import defaultdict


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


def loop_length(head: Node) -> int:
    # Brute force solution
    if head is None:
        return 0
    temp: Node = head
    hsh = defaultdict(int)
    t: int = 1
    while temp:
        if hsh[temp]:
            lenght: int = t - hsh[temp]
            return lenght
        hsh[temp] = t
        t += 1
        temp = temp.next

    return 0


def find_length(slow: Node, fast: Node) -> int:
    cnt: int = 1
    fast = fast.next
    while slow != fast:
        cnt += 1
        fast = fast.next

    return cnt


def loop_length_optimal(head: Node) -> Node:
    slow: Node = head
    fast: Node = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return find_length(slow=slow, fast=fast)

    return 0


if __name__ == "__main__":
    llist: SingleLinkedList = SingleLinkedList()
    print(llist.head)
    node1: Node = Node(1)
    node2: Node = Node(2)
    node3: Node = Node(3)
    node4: Node = Node(4)
    node5: Node = Node(5)
    node6: Node = Node(6)
    node7: Node = Node(7)
    node8: Node = Node(8)
    node9: Node = Node(9)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    llist.head = node1
    node9.next = node3
    # llist.print_list()
    print(loop_length(head=llist.head))
    print(loop_length_optimal(head=llist.head))
