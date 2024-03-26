"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes
is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a linked list.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            Optional[ListNode]: The head of the reversed linked list.
        """
        if head is None or head.next is None:
            return head

        prev: ListNode = None
        node = head
        while node:
            front: ListNode = node.next
            node.next = prev
            prev = node
            node = front
        return prev

    def __get_kth_node(self, temp: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Get the kth node from the current node.

        Args:
            temp (Optional[ListNode]): The current node.
            k (int): The number of nodes to traverse.

        Returns:
            Optional[ListNode]: The kth node from the current node.
        """
        k -= 1
        while temp and k > 0:
            k -= 1
            temp = temp.next
        return temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse nodes of a linked list in groups of size k.

        Args:
            head (Optional[ListNode]): The head of the linked list.
            k (int): The size of each group.

        Returns:
            Optional[ListNode]: The head of the modified linked list.
        """
        temp: ListNode = head
        prev_last: ListNode = None
        while temp:
            # Get the kth node from the current position
            kth_node: ListNode = self.__get_kth_node(temp, k)
            if kth_node is None:
                # If kth_node is None, it means the remaining nodes are less than k
                if prev_last:
                    prev_last.next = temp
                break

            # Get the next node after kth node
            next_node: ListNode = kth_node.next
            kth_node.next = None

            # Reverse the current group
            self.__reverse(temp)

            # Update the head of the linked list if needed
            if temp == head:
                head = kth_node
            else:
                prev_last.next = kth_node

            # Update pointers for the next iteration
            prev_last = temp
            temp = next_node

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
    head = solution.reverseKGroup(head=head, k=k)
    print_list(head=head)
