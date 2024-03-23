"""
A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.
"""


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def __reverse(self, head: Node) -> Node:
        """
        Reverse the given linked list.

        Parameters:
            head (Node): The head of the linked list.

        Returns:
            Node: The head of the reversed linked list.
        """
        if head is None or head.next is None:
            return head
        cur: Node = head
        prev: Node = None
        while cur:
            front: Node = cur.next
            cur.next = prev
            prev = cur
            cur = front

        return prev

    def __f(self, head: Node) -> Node:
        """
        Perform addition operation on the reversed linked list.

        Parameters:
            head (Node): The head of the linked list representing the number.

        Returns:
            Node: The head of the updated linked list representing the incremented number.
        """
        new_head = self.__reverse(head=head)
        carry: int = 1
        temp = new_head
        while temp:
            temp.data = temp.data + carry
            if temp.data < 10:
                carry = 0
                break
            else:
                carry = 1
                temp.data = 0
            temp = temp.next

        head: Node = self.__reverse(head=new_head)
        if carry:
            node = Node(carry)
            node.next = head
            head = node
        return head

    def addOne(self, head: Node) -> Node:
        """
        Add 1 to the number represented by the linked list.

        Parameters:
            head (Node): The head of the linked list representing the number.

        Returns:
            Node: The head of the linked list representing the incremented number.
        """
        return self.__f(head=head)


def print_list(head: Node) -> None:
    node: Node = head
    while node:
        print(node.data, end="->")
        node = node.next
    print("Null")


if __name__ == "__main__":
    head: Node = Node(4)
    head.next = Node(5)
    head.next.next = Node(6)
    print_list(head=head)  # Output: 4->5->6->Null

    solution: Solution = Solution()
    head = solution.addOne(head=head)
    print_list(head=head)  # Output: 4->5->7->Null
