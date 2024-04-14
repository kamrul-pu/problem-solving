"""
Given the head of a linked list, rotate the list to the right by k places.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __get_kth_node(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k -= 1
        temp: ListNode = head
        while temp and k > 0:
            k -= 1
            temp = temp.next
        return temp

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotate the linked list to the right by k places.

        Args:
            head (Optional[ListNode]): The head of the linked list.
            k (int): The number of places to rotate the list.

        Returns:
            Optional[ListNode]: The head of the rotated linked list.
        """
        if head is None or head.next is None:
            return head

        # Find the length of the linked list
        tail: ListNode = head
        length: int = 1
        while tail.next:
            length += 1
            tail = tail.next

        # Calculate the effective rotation value considering the length of the list
        k %= length
        if k == 0:
            return head

        # Find the node at (length - k) position from the beginning
        kth_node: ListNode = self.__get_kth_node(head, k=length - k)

        # Rotate the list
        tail.next = head
        head = kth_node.next
        kth_node.next = None

        return head


def print_list(head: ListNode) -> None:
    """
    Print the linked list starting from the given head node.

    Args:
        head (ListNode): The head node of the linked list.
    """
    node: ListNode = head
    while node:
        print(node.val, end="->")
        node = node.next
    print("Null")


if __name__ == "__main__":
    # Test the reverseKGroup method
    head: ListNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print_list(head=head)
    solution: Solution = Solution()
    k: int = 2
    head = solution.rotateRight(head=head, k=k)
    print_list(head=head)
