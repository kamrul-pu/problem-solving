"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

from typing import Optional, Deque
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __reorder(self, head: Optional[ListNode]) -> None:
        """
        Helper method to reorder the linked list using deque.

        Args:
            head (Optional[ListNode]): Head of the linked list.
        """
        if head is None or head.next is None:
            return

        # Using deque to store values of the second half of the linked list
        q: Deque = deque()
        temp: ListNode = head.next
        while temp:
            q.append(temp.val)
            temp = temp.next

        # Traverse the linked list and update node values from the deque
        temp: ListNode = head.next
        flag: bool = True
        while temp:
            if flag:
                top: int = q.pop()
                flag = False
            else:
                top: int = q.popleft()
                flag = True

            temp.val = top
            temp = temp.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders the linked list to the specified form in-place.

        Args:
            head (Optional[ListNode]): Head of the linked list.
        """
        # If the list is empty or has only one node, no reordering is needed
        if head is None or head.next is None:
            return

        # Finding the middle of the linked list
        slow: ListNode = head
        fast: ListNode = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge the two halves of the linked list
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

    def print_list(self, head: Optional[ListNode]) -> None:
        """
        Prints the linked list.

        Args:
            head (Optional[ListNode]): Head of the linked list.
        """
        cur: ListNode = head
        while cur:
            print(cur.val, end="->")
            cur = cur.next

        print("NULL")


if __name__ == "__main__":
    # Creating the linked list
    head: ListNode = ListNode(val=1)
    node2: ListNode = ListNode(val=2)
    node3: ListNode = ListNode(val=3)
    node4: ListNode = ListNode(val=4)
    node5: ListNode = ListNode(val=5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # Instantiating the Solution class
    solution: Solution = Solution()

    # Printing the original linked list
    solution.print_list(head=head)

    # Reordering the linked list
    solution.reorderList(head=head)

    # Printing the reordered linked list
    solution.print_list(head=head)
