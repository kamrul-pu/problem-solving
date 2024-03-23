"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

from collections import defaultdict
from typing import Optional, DefaultDict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __detect_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Detects if a linked list has a cycle using a hash map.

        Parameters:
            head (ListNode): The head of the linked list.

        Returns:
            bool: True if the linked list has a cycle, False otherwise.
        """
        if head is None or head.next is None:
            return False

        # Use a hash map to track visited nodes
        nodes: DefaultDict[bool] = defaultdict(bool)
        node: ListNode = head
        while node:
            if nodes[node]:
                return True
            nodes[node] = True
            node = node.next

        return False

    def __detect_cycle_optimal(self, head: Optional[ListNode]) -> bool:
        """
        Detects if a linked list has a cycle using the slow and fast pointer approach.

        Parameters:
            head (ListNode): The head of the linked list.

        Returns:
            bool: True if the linked list has a cycle, False otherwise.
        """
        if head is None or head.next is None:
            return False

        # Initialize slow and fast pointers
        slow: ListNode = head
        fast: ListNode = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a linked list has a cycle.

        Parameters:
            head (ListNode): The head of the linked list.

        Returns:
            bool: True if the linked list has a cycle, False otherwise.
        """
        # Use the optimal method to detect a cycle
        return self.__detect_cycle_optimal(head=head)


if __name__ == "__main__":
    two: ListNode = ListNode(3)
    head: ListNode = ListNode(3)
    head.next = two
    two.next = ListNode(0)
    two.next.next = ListNode(-4)
    two.next.next.next = two

    solution: Solution = Solution()
    print(solution.hasCycle(head=head))
