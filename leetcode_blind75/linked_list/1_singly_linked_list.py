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


def find(head: Node, data: int) -> Node:
    """
    Search for a node with the given data value in the linked list.

    Parameters:
        head (Node): The head node of the linked list.
        data (int): The data value to search for.

    Returns:
        Node: The node with the given data value if found, else None.
    """
    if head is None:
        return None

    # Start from the head node and iterate through the list
    node: Node = head
    while node:
        # Check if the current node's data matches the search data
        if node.data == data:
            return node
        # Move to the next node
        node = node.next

    # Data not found in the list
    return None


def insert_sorted(nums: List[int]) -> Node:
    """
    Insert elements from a list into a sorted singly linked list.

    Parameters:
        nums (List[int]): The list of integers to insert.

    Returns:
        Node: The head node of the sorted linked list.
    """
    n: int = len(nums)
    if n == 0:
        return None

    # Initialize the head node with the first element
    head: Node = Node(data=nums[0])
    curr: Node = head

    # Iterate through the list to insert elements into the sorted list
    for i in range(1, n):
        curr = head
        temp: Node = Node(nums[i])

        # If the current node's data is greater than the new element, insert it at the beginning
        if head.data > nums[i]:
            temp.next = head
            head = temp
        else:
            # Find the correct position to insert the new element
            while curr.next and curr.next.data < nums[i]:
                curr = curr.next

            # Insert the new element into the sorted list
            temp.next = curr.next
            curr.next = temp

    return head


def insert_position(head: Node, data: int, position: int) -> Node:
    """
    Insert a node with the given data at a specified position in the linked list.

    Parameters:
        head (Node): The head node of the linked list.
        data (int): The data value of the node to be inserted.
        position (int): The position where the node should be inserted (0-based index).

    Returns:
        Node: The head node of the modified linked list after insertion.
    """
    # Check if the list is empty
    if head is None:
        return head

    # Create a new node with the given data
    temp: Node = Node(data=data)

    # Insert the node at the beginning if the position is 0
    if position == 0:
        temp.next = head
        head = temp
        return head

    # Move to the node just before the specified position
    position -= 1
    curr: Node = head
    while curr.next and position:
        curr = curr.next
        position -= 1

    # Insert the new node at the specified position
    temp.next = curr.next
    curr.next = temp

    # Return the head node of the modified linked list
    return head


def delete_node(head: Node, data) -> None:
    """
    Delete a node with the given data value from the linked list.

    Parameters:
        head (Node): The head node of the linked list.
        data (int): The data value of the node to delete.

    Returns:
        None
    """
    if head is None:
        return None

    # Check if the head node itself contains the data to be deleted
    if head.data == data:
        head = head.next
        return head

    # Initialize pointers for traversal
    curr: Node = head
    prev: Node = head

    # Iterate through the list to find the node with the given data value
    while curr.next and curr.data != data:
        prev = curr
        curr = curr.next

    # If the node with the given data value is found, delete it by adjusting pointers
    if curr.data == data:
        prev.next = curr.next

    # Return the updated head node
    return head


def mid_element(head: Node) -> Node:
    """
    Find the middle element of a singly linked list.

    Parameters:
        head (Node): The head node of the linked list.

    Returns:
        Node: The middle node of the linked list.
    """
    # Check if the list is empty
    if head is None:
        return None

    # Initialize slow and fast pointers
    slow: Node = head
    fast: Node = head.next

    # Move slow pointer one step and fast pointer two steps at a time until fast reaches the end
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Return the middle node (or the first middle node in case of even number of nodes)
    return slow


if __name__ == "__main__":
    nums: List[int] = [10, 3, 5, 92, 5, 7, 8]
    head: Node = build_list(nums=nums)
    print_list(head=head)  # Print the original list
    print(find(head=head, data=7))  # Find a node with data value 7
    head1: Node = insert_sorted(nums=nums)
    print_list(head=head1)  # Print the sorted list
    head1 = delete_node(head=head1, data=99)  # Delete a node with data value 99
    print_list(head=head1)  # Print the list after deletion
    print(mid_element(head=head1).data)
    head1 = insert_position(head=head1, data=9, position=5)
    print_list(head=head1)
