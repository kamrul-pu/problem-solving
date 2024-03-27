"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value
of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the
pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the
original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the
copied list, x.random --> y. Return the head of the copied linked list.

"""

from collections import defaultdict
from typing import DefaultDict, Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __f(self, head: Optional[Node]) -> Node:
        """
        Create a deep copy of the given linked list using a dictionary to map original nodes to their copies.

        Args:
            head (Optional[Node]): The head of the original linked list.

        Returns:
            Node: The head of the copied linked list.
        """
        # Dictionary to map original nodes to their corresponding copies
        mp: DefaultDict = defaultdict(None)
        temp: Node = head

        # First pass: Create a shallow copy of the linked list without setting the random pointers
        while temp:
            node: Node = Node(temp.val)
            mp[temp] = node
            temp = temp.next

        temp = head
        # Second pass: Set the next and random pointers of the copied nodes based on the mapping
        while temp:
            copy_node: Node = mp[temp]
            copy_node.next = mp[temp.next] if temp.next else None
            copy_node.random = mp[temp.random] if temp.random else None
            temp = temp.next

        return mp[head]

    def __copy(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        Create a deep copy of the given linked list in place without using extra space.

        Args:
            head (Optional[Node]): The head of the original linked list.

        Returns:
            Optional[Node]: The head of the copied linked list.
        """
        temp = head
        # First pass: Create a shallow copy of each node and insert it between the original nodes
        while temp:
            copy_node: Node = Node(temp.val)
            copy_node.next = temp.next
            temp.next = copy_node
            temp = temp.next.next

        temp = head
        # Second pass: Set the random pointers of the copied nodes
        while temp:
            temp.next.random = temp.random.next if temp.random else None
            temp = temp.next.next

        dummy: Node = Node(-1)
        res: Node = dummy
        temp = head
        # Third pass: Extract the copied nodes from the modified original list
        while temp:
            res.next = temp.next
            res = res.next
            temp.next = temp.next.next
            temp = temp.next

        return dummy.next

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        Create a deep copy of the given linked list with random pointers.

        Args:
            head (Optional[Node]): The head of the original linked list.

        Returns:
            Optional[Node]: The head of the copied linked list.
        """
        if head is None:
            return head

        # Use either the dictionary-based approach or the in-place copying approach
        # return self.__f(head=head)
        return self.__copy(head=head)


def print_list(head: Node) -> None:
    """
    Print the linked list starting from the given head node.

    Args:
        head (ListNode): The head node of the linked list.
    """
    node: Node = head
    while node:
        print(node.val, end="->")
        node = node.next
    print("Null")


if __name__ == "__main__":
    # Example usage
    one: Node = Node(7)
    two: Node = Node(13)
    three: Node = Node(11)
    four: Node = Node(10)
    five: Node = Node(1)
    one.next = two
    two.next = three
    two.random = one
    three.next = four
    three.random = five
    four.next = five
    four.random = three
    five.random = one
    # Display the original linked list
    print_list(head=one)
    solution: Solution = Solution()
    # Create a deep copy of the linked list and display it
    head = solution.copyRandomList(head=one)
    print_list(head=head)
