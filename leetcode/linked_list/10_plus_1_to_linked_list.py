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
        # Reverse the linked list to simplify addition
        new_head = self.__reverse(head=head)

        # Initialize carry for addition
        carry: int = 1
        temp = new_head
        while temp:
            # Add carry to the current node's data
            temp.data = temp.data + carry

            # Check if the result is less than 10
            if temp.data < 10:
                carry = 0  # Update carry to 0
                break
            else:
                carry = 1  # Update carry to 1 for next iteration
                temp.data = 0  # Update current node's data to 0 for single-digit result

            # Move to the next node
            temp = temp.next

        # Reverse the linked list back to its original order
        head: Node = self.__reverse(head=new_head)

        # If carry is still 1, create a new node with value 1 and append it to the head
        if carry:
            node = Node(carry)
            node.next = head
            head = node

        return head

    def __helper(self, node: Node) -> int:
        """
        Recursively add 1 to the number represented by the linked list.

        Parameters:
            node (Node): The current node in the linked list.

        Returns:
            int: The carry value (0 or 1) after adding 1 to the number.
        """
        # Base case: if node is None, return 1 indicating carry
        if node is None:
            return 1

        # Recursively process the next node and get the carry value
        carry = self.__helper(node.next)

        # Add the carry to the current node's data
        node.data = node.data + carry

        # If the result is less than 10, return 0 indicating no carry
        if node.data < 10:
            return 0

        # If the result is 10 or greater, set the node's data to 0 and return 1 indicating carry
        node.data = 0
        return 1

    def addOne(self, head: Node) -> Node:
        """
        Add 1 to the number represented by the linked list.

        Parameters:
            head (Node): The head of the linked list representing the number.

        Returns:
            Node: The head of the linked list representing the incremented number.
        """
        # Call the recursive helper function to add 1 to the linked list
        carry: int = self.__helper(head)

        # If there's a carry after adding 1 to the linked list, create a new node with value 1 and append it to the head
        if carry == 1:
            node = Node(1)
            node.next = head
            head = node

        return head


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
