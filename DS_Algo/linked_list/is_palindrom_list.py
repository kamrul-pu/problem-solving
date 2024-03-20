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

    def check_palindrome(self) -> bool:
        if self.head is None:
            return True

        lst: list[int] = []
        temp: Node = self.head
        while temp:
            lst.append(temp.data)
            temp = temp.next

        left: int = 0
        right: int = len(lst) - 1
        while left < right:
            if lst[left] != lst[right]:
                return False
            left += 1
            right -= 1

        return True

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


def is_palindrome(head: Node) -> bool:
    if head is None or head.next is None:
        return True
    slow: Node = head
    fast: Node = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    new_head: Node = reverse_list(slow.next)
    first: Node = head
    second: Node = new_head
    while second:
        if first.data != second.data:
            reverse_list(new_head)
            return False
        first = first.next
        second = second.next

    reverse_list(new_head)
    return True


if __name__ == "__main__":
    llist: SingleLinkedList = SingleLinkedList()
    print(llist.head)
    llist.add_data(1)
    llist.add_data(2)
    llist.add_data(3)
    # llist.add_data(5)
    llist.add_data(2)
    llist.add_data(1)
    llist.print_list()
    print(llist.check_palindrome())
    print(is_palindrome(llist.head))
    llist.print_list()
