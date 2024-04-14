"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
"""

from collections import defaultdict
from typing import Optional, DefaultDict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __detect_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Detects the node where a cycle starts in a linked list using a hash map.

        This method uses a hash map to track visited nodes.
        If a node is encountered twice, it indicates the presence of a cycle.

        Parameters:
            head (ListNode): The head of the linked list.

        Returns:
            ListNode or None: The node where the cycle starts if found, otherwise None.
        """
        if head is None or head.next is None:
            return None

        # Use a hash map to track visited nodes
        nodes: DefaultDict[bool] = defaultdict(bool)
        node: ListNode = head
        while node:
            if nodes[node]:
                return node
            nodes[node] = True
            node = node.next

        return None

    def __find_node(self, slow: ListNode, fast: ListNode) -> Optional[ListNode]:
        """
        Finds the node where the cycle starts in the linked list.

        Parameters:
            slow (ListNode): The node where slow pointer meets fast pointer.
            fast (ListNode): The node where fast pointer meets slow pointer.

        Returns:
            ListNode or None: The node where the cycle starts if found, otherwise None.
        """
        # traverse while they are not equal
        while slow != fast:
            # move each pointer one step
            slow = slow.next
            fast = fast.next

        return slow

    def __detect_cycle_optimal(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Detects a cycle in the linked list using Floyd's Tortoise and Hare algorithm.

        Parameters:
            head (ListNode): The head of the linked list.

        Returns:
            ListNode or None: The node where the cycle starts if found, otherwise None.
        """
        # detect loop by initializing slow and fast pointer
        slow: ListNode = head
        fast: ListNode = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if there is a loop find the starting node
            if slow == fast:
                # start one of the pointer from head
                return self.__find_node(slow=head, fast=fast)

        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the node where a cycle starts in a linked list.

        This method delegates the task of cycle detection to the __detect_cycle method.

        Parameters:
            head (ListNode): The head of the linked list.

        Returns:
            ListNode or None: The node where the cycle starts if found, otherwise None.
        """
        return self.__detect_cycle_optimal(head=head)


if __name__ == "__main__":
    two: ListNode = ListNode(2)
    head: ListNode = ListNode(3)
    head.next = two
    two.next = ListNode(0)
    two.next.next = ListNode(-4)
    two.next.next.next = two

    solution: Solution = Solution()
    print(solution.detectCycle(head=head).val)
