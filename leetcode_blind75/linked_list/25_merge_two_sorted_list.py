"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __merge_optimal(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted linked list using an optimal approach.

        Args:
            list1 (Optional[ListNode]): The head of the first sorted linked list.
            list2 (Optional[ListNode]): The head of the second sorted linked list.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.
        """
        if list1 is None and list2 is None:
            return list1
        if list1 is None or list2 is None:
            return list1 if list1 else list2

        # Determine which list has the smaller value at the head
        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)

        head = seek
        # Traverse both lists and merge them
        while seek and target:
            # Advance through list1 until reaching a node whose value is greater than the current node in list2
            while seek.next and seek.next.val < target.val:
                seek = seek.next

            # Insert the current node from list2 into list1 after the current node in list1
            seek.next, target = target, seek.next
            # Move to the next node in list1
            seek = seek.next

        return head

    def __merge(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted linked list.

        Args:
            list1 (Optional[ListNode]): The head of the first sorted linked list.
            list2 (Optional[ListNode]): The head of the second sorted linked list.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.
        """
        if list1 is None and list2 is None:
            return list1
        if list1 is None or list2 is None:
            return list1 if list1 else list2

        # Create a dummy node to handle the merged list
        dummy: ListNode = ListNode(float("inf"))
        temp: ListNode = dummy
        temp1: ListNode = list1
        temp2: ListNode = list2

        # Traverse both lists and merge them
        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next

            temp = temp.next

        # Attach remaining nodes from either list1 or list2
        temp.next = list1 if list1 else list2

        return dummy.next

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted linked list.

        Args:
            list1 (Optional[ListNode]): The head of the first sorted linked list.
            list2 (Optional[ListNode]): The head of the second sorted linked list.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.
        """
        # return self.__merge(list1=list1, list2=list2)
        return self.__merge_optimal(list1, list2)


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
    # Test the mergeTwoLists method
    head1: ListNode = ListNode(1, ListNode(2, ListNode(4)))
    head2: ListNode = ListNode(1, ListNode(3, ListNode(4)))
    print_list(head=head1)
    print_list(head=head2)
    solution: Solution = Solution()
    head: ListNode = solution.mergeTwoLists(list1=head1, list2=head2)
    print_list(head=head)
