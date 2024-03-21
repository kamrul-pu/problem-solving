"""
Given the head of a singly linked list, group all the nodes with odd indices together
followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # Initialize pointers for odd and even nodes
        odd: ListNode = head
        even_head: ListNode = head.next
        even: ListNode = head.next

        # Traverse the list and connect odd and even nodes separately
        while even and even.next:
            # Connect odd nodes
            odd.next = even.next
            # Move odd pointer to the next odd node
            odd = odd.next
            # Connect even nodes
            even.next = odd.next
            # Move even pointer to the next even node
            even = even.next

        # Connect the last odd node with the head of the even list
        odd.next = even_head

        return head


def print_list(head: ListNode) -> None:
    """
    Print the linked list starting from the given head node.

    Parameters:
        head (ListNode): The head node of the linked list.
    """
    node: ListNode = head
    while node:
        print(node.val, end="->")
        node = node.next
    print("Null")


if __name__ == "__main__":
    head: ListNode = ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5))),
        ),
    )
    print_list(head=head)
    solution: Solution = Solution()
    head = solution.oddEvenList(head=head)
    print_list(head=head)
