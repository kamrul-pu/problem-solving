"""Find the pairs for given sum in doubly linked list."""


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node = None
        self.prev: Node = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def insert_node(self, data: int) -> None:
        node: Node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        if self.head.data >= data:
            # insert at the begining
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif self.tail.data <= data:
            # insert at last
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            # insert in middle area by sorting them
            cur: Node = self.head
            while cur.next and cur.next.data < data:
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node

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


def find_pairs(head: Node, tail: Node, sum: int) -> list[list[int]]:
    answer: list[list[int]] = []
    temp1: Node = head
    while temp1:
        temp2: Node = temp1.next
        while temp2:
            if temp1.data + temp2.data == sum:
                answer.append([temp1.data, temp2.data])
            temp2 = temp2.next

        temp1 = temp1.next

    return answer


def find_pairs_optimal(head: Node, tail: Node, sum: int) -> list[list[int]]:
    left: Node = head
    right: Node = tail
    answer: list[list[int]] = []
    while left.data < right.data:
        cur_sum = left.data + right.data
        if cur_sum == sum:
            answer.append([left.data, right.data])
        if cur_sum > sum:
            right = right.prev
        else:
            left = left.next

    return answer


if __name__ == "__main__":
    dll: DoublyLinkedList = DoublyLinkedList()
    elements: list[int] = [9, 2, 3, 4, 1]
    for element in elements:
        dll.insert_node(element)

    dll.print_list()
    dll.print_list(reverse=True)
    sum: int = 5
    answer: list[list[int]] = find_pairs(head=dll.head, tail=dll.tail, sum=sum)
    print(answer)
    answer: list[list[int]] = find_pairs_optimal(head=dll.head, tail=dll.tail, sum=sum)
    print(answer)
