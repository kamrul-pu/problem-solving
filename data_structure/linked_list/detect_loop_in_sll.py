"""Detect Loop in singly linked list."""
from collections import defaultdict
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " miliseconds")
        return result

    return wrapper


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


@time_it
def detect_cycle(head: Node) -> bool:
    # Brute force solution
    if head is None:
        return False
    temp: Node = head
    hsh = defaultdict(bool)
    while temp:
        if hsh[temp]:
            return True
        hsh[temp] = True
        temp = temp.next

    return False


@time_it
def detect_cycle_optimal(head: Node) -> bool:
    if head is None:
        return False
    fast: Node = head
    slow: Node = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


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
    print(detect_cycle(head=llist.head))
    print(detect_cycle(head=llist.head))
