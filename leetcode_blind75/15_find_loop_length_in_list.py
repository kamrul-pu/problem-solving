"""
Detect loop length in the linked list.
"""

from collections import defaultdict
from typing import Optional, DefaultDict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __length(self, head: Optional[ListNode]) -> int:
        """
        Find the length of the loop in the linked list using a hash map.

        Parameters:
            head (ListNode): The head of the linked list.

        Returns:
            int: The length of the loop if a loop is detected, 0 otherwise.
        """
        if head is None or head.next is None:
            return 0

        # Use a hash map to track visited nodes
        nodes: DefaultDict[int] = defaultdict(int)
        node: ListNode = head
        i: int = 1
        while node:
            # If the node is already visited, it's the start of the loop
            if nodes[node] != 0:
                return i - nodes[node]
            nodes[node] = i
            i += 1
            node = node.next

        return 0

    def __find_length(self, slow: ListNode, fast: ListNode) -> int:
        """
        Helper function to find the length of the loop in the linked list.

        Parameters:
            slow (ListNode): The slow pointer in the linked list.
            fast (ListNode): The fast pointer in the linked list.

        Returns:
            int: The length of the loop.
        """
        cnt: int = 1
        fast = fast.next
        while fast and slow != fast:
            cnt += 1
            fast = fast.next

        return cnt

    def __length_optimal(self, head: Optional[ListNode]) -> int:
        """
        Find the length of the loop in the linked list using Floyd's Tortoise and Hare algorithm.

        Parameters:
            head (ListNode): The head of the linked list.

        Returns:
            int: The length of the loop if a loop is detected, 0 otherwise.
        """
        if head is None or head.next is None:
            return 0

        slow: ListNode = head
        fast: ListNode = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # If slow and fast pointers meet, there's a loop
            if slow == fast:
                return self.__find_length(slow=slow, fast=fast)

        return 0

    def loop_length(self, head: Optional[ListNode]) -> int:
        """
        Determine the length of the loop in the linked list.

        Parameters:
            head (ListNode): The head of the linked list.

        Returns:
            int: The length of the loop if a loop is detected, 0 otherwise.
        """
        # return self.__length(head=head)
        return self.__length_optimal(head=head)


if __name__ == "__main__":
    two: ListNode = ListNode(2)
    head: ListNode = ListNode(3)
    head.next = two
    two.next = ListNode(0)
    two.next.next = ListNode(-4)
    two.next.next.next = two

    solution: Solution = Solution()
    print(solution.loop_length(head=head))
