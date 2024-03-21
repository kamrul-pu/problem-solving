"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of the
node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

from typing import Optional

from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        """
        Constructor for the ListNode class.

        Args:
            x: The value of the node.
        """
        self.val = x
        self.next = None


class Solution:
    def __detect_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Detects if there is a cycle in a linked list using a dictionary to track visited nodes.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            bool: True if there is a cycle, False otherwise.
        """
        if head is None or head.next is None:
            return False
        nodes: defaultdict = defaultdict(bool)
        temp: ListNode = head

        while temp:
            if nodes[temp]:
                return True
            nodes[temp] = True
            temp = temp.next

        return False

    def __detect_cycle_optimal(self, head: Optional[ListNode]) -> bool:
        """
        Detects if there is a cycle in a linked list using the slow and fast pointer technique.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            bool: True if there is a cycle, False otherwise.
        """
        if head is None or head.next is None:
            return False
        slow: ListNode = head
        fast: ListNode = head.next
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next

        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines if there is a cycle in the linked list.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            bool: True if there is a cycle, False otherwise.
        """
        # return self.__detect_cycle(head=head)
        return self.__detect_cycle_optimal(head=head)

    def print_list(self, head: Optional[ListNode]) -> None:
        """
        Prints the values of the linked list.

        Args:
            head (Optional[ListNode]): The head of the linked list.
        """
        cur: ListNode = head
        while cur:
            print(cur.val, end="->")
            cur = cur.next

        print("NUll")


if __name__ == "__main__":
    head: ListNode = ListNode(1)
    node2: ListNode = ListNode(2)
    node3: ListNode = ListNode(3)
    node4: ListNode = ListNode(4)
    node5: ListNode = ListNode(5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3

    solution: Solution = Solution()
    # solution.print_list(head=head)
    print(solution.hasCycle(head=head))
