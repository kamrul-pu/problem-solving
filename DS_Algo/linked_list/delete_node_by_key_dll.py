"""Delete all nodes by key in Doubly Linked List."""


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node = None
        self.prev: Node = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def print_list(self, reverse: bool = False) -> None:
        if reverse:
            node = self.tail
        else:
            node: Node = self.head
        while node:
            print(node.data, end="->")
            if reverse:
                node = node.prev
            else:
                node = node.next
        print("Null")


def delete_all_occurance(head: Node, tail: Node, key: int) -> Node:
    if head is None:
        return head
    prev_node: Node = None
    temp: Node = head
    next_node: Node = None
    while temp:
        if temp.data == key:
            # delete the node
            if temp == head:
                head = head.next
                head.prev = None
            if temp == tail:
                tail = temp.prev
            prev_node = temp.prev
            next_node = temp.next
            if prev_node:
                prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node
            temp = next_node
        else:
            # move temp to the next node
            temp = temp.next

    return head, tail


if __name__ == "__main__":
    dll: DoublyLinkedList = DoublyLinkedList()
    dll.print_list()
    # add data manually to the doubly linked list
    node1: Node = Node(10)
    node2: Node = Node(4)
    node3: Node = Node(10)
    node4: Node = Node(10)
    node5: Node = Node(6)
    node6: Node = Node(10)
    dll.head = node1
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3
    node4.next = node5
    node5.prev = node4
    node5.next = node6
    node6.prev = node5
    dll.tail = node6
    dll.print_list()
    dll.print_list(reverse=True)
    dll.head, dll.tail = delete_all_occurance(head=dll.head, tail=dll.tail, key=10)
    dll.print_list()
    dll.print_list(reverse=True)
