"""Single Linked List Using Python."""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list: list):
        self.head = None
        for data in data_list:
            self.insert_at_begining(data)

    def remove_at(self, index: int) -> bool:
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_at(self, index: int, data: int):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after: int, data_to_insert: int):
        if self.head is None:
            print("list is empty")
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return True
            itr = itr.next
        print(f"{data_after} is not in the list")

    def remove_by_value(self, data):
        if self.head is None:
            print("list is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        prev = None
        while itr:
            if itr.data == data:
                prev.next = itr.next
                return
            prev = itr
            itr = itr.next
        print(f"{data} is not in the list")

    def get_length(self) -> int:
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        while itr:
            print(itr.data, end="->")
            itr = itr.next
        print()


ll = LinkedList()
ll.insert_at_begining(10)
ll.insert_at_begining(20)
ll.insert_at_begining(30)
ll.insert_at_end(34)
ll.insert_at_end(100)
dl = [1, 2, 3, 4, 5]
ll.insert_values(dl)
ll.print()
print("length of the linked list: ", ll.get_length())
ll.remove_at(1)
ll.insert_at(2, 36)
ll.print()
ll.insert_after_value(36, 38)
ll.print()
ll.insert_after_value(39, 40)
ll.remove_by_value(38)
print(ll.print())
ll.remove_by_value(5)
ll.print()
ll.remove_by_value(1)
ll.print()
