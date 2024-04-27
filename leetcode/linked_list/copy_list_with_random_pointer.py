"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
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
    def __f(self, head: "Optional[Node]") -> "Optional[Node]":
        # Approach using a dictionary to track original nodes and their copies
        mp: DefaultDict[Node, Node] = defaultdict(None)

        temp: Node = head

        # First pass: Create copies of each node without setting next and random pointers
        while temp:
            copy_node: Node = Node(temp.val)
            mp[temp] = copy_node
            temp = temp.next

        temp = head

        # Second pass: Set next and random pointers for the copied nodes
        while temp:
            copy_node: Node = mp[temp]
            copy_node.next = mp[temp.next] if temp.next else None
            copy_node.random = mp[temp.random] if temp.random else None
            temp = temp.next

        return mp[head]

    def __copy(self, head: "Optional[Node]") -> "Optional[Node]":
        # Optimized approach using constant space without using extra dictionary
        temp: Node = head

        # First pass: Insert copied nodes into the original list
        while temp:
            copy_node: Node = Node(temp.val)
            copy_node.next = temp.next
            temp.next = copy_node
            temp = temp.next.next

        temp = head

        # Second pass: Set random pointers for the copied nodes
        while temp:
            temp.next.random = temp.random.next if temp.random else None
            temp = temp.next.next

        dummy: Node = Node(-1)
        res: Node = dummy
        temp = head

        # Third pass: Separate original and copied lists
        while temp:
            res.next = temp.next
            res = res.next
            temp.next = temp.next.next
            temp = temp.next

        return dummy.next

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return head

        # Use either __f or __copy method to create a deep copy of the linked list
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
        # Print node value and arrow "->" to the next node
        print(node.val, end="->")
        node = node.next
    # Print "Null" to indicate end of the list
    print("Null")


if __name__ == "__main__":
    # Example usage
    one: Node = Node(7)
    two: Node = Node(13)
    three: Node = Node(11)
    four: Node = Node(10)
    five: Node = Node(1)
    # Construct the original linked list with random pointers
    one.next = two
    two.next = three
    two.random = one
    three.next = four
    three.random = five
    four.next = five
    four.random = three
    five.random = one
    # Display the original linked list
    print("Original Linked List:")
    print_list(head=one)
    solution: Solution = Solution()
    # Create a deep copy of the linked list and display it
    head = solution.copyRandomList(head=one)
    print("\nDeep Copy of the Linked List:")
    print_list(head=head)
