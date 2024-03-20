"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

"""Singly Linked List in Python."""

from typing import List, Optional


class Node:
    def __init__(self, data: int) -> None:
        """
        Initialize a node with data and a reference to the next node.

        Parameters:
            data (int): The data value of the node.
        """
        self.data = data
        self.next: Optional[Node] = None


class Solution:
    def __reverse_data(self, head: Optional[Node]) -> Optional[Node]:
        """
        Reverse the linked list using an auxiliary list to store node data.

        Parameters:
            head (Optional[Node]): The head node of the linked list.

        Returns:
            Optional[Node]: The head node of the reversed linked list.
        """
        if head is None or head.next is None:
            return head

        # Store node data in a stack
        st: List[int] = []
        curr: Node = head
        while curr:
            st.append(curr.data)
            curr = curr.next

        # Update node data in reverse order
        curr: Node = head
        while curr:
            top: int = st.pop()
            curr.data = top
            curr = curr.next

    def __reverse_optimal(self, head: Optional[Node]) -> Optional[Node]:
        """
        Reverse the linked list using an optimal approach.

        Parameters:
            head (Optional[Node]): The head node of the linked list.

        Returns:
            Optional[Node]: The head node of the reversed linked list.
        """
        # Check if the list is empty or has only one node
        if head is None or head.next is None:
            return head

        # Initialize pointers
        # Pointer to the previous node, initially None as there's no node before the head
        prev: Node = None
        # Pointer to the current node, initially set to the head of the list
        curr: Node = head

        # Reverse the pointers
        while curr:
            curr_next = curr.next  # Store the next node before modifying the pointer
            curr.next = prev  # Reverse the pointer, making the current node point to the previous node
            prev = curr  # Move the previous pointer one step forward
            curr = curr_next  # Move the current pointer one step forward to proceed to the next node

        # After the loop, prev will point to the last node, which becomes the new head of the reversed list
        return prev

    def reverseList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Wrapper function to choose between reverse methods.

        Parameters:
            head (Optional[Node]): The head node of the linked list.

        Returns:
            Optional[Node]: The head node of the reversed linked list.
        """
        # Choose the optimal reverse method
        # return self.__reverse_data(head=head)
        return self.__reverse_optimal(head=head)


def print_list(head: Node) -> None:
    """
    Print the linked list starting from the given head node.

    Parameters:
        head (Node): The head node of the linked list.
    """
    node: Node = head
    while node:
        print(node.data, end="->")
        node = node.next
    print("Null")


def build_list(nums: List[int]) -> Node:
    """
    Build a singly linked list from a list of integers.

    Parameters:
        nums (List[int]): The list of integers to build the linked list from.

    Returns:
        Node: The head node of the linked list.
    """
    n: int = len(nums)
    if n == 0:
        return None

    # Initialize the head node
    head: Node = Node(nums[0])
    node: Node = head

    # Iterate through the list to create nodes and link them
    for i in range(1, n):
        node.next = Node(nums[i])
        node = node.next

    return head


if __name__ == "__main__":
    nums: List[int] = [10, 3, 5, 92, 5, 7, 8]
    head: Node = build_list(nums=nums)
    print_list(head=head)  # Print the original list
    solution: Solution = Solution()
    head = solution.reverseList(head=head)
    print_list(head=head)
