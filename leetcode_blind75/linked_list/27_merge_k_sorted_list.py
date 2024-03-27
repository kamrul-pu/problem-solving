"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def __merge(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merges two sorted linked lists in an optimal way.

        Args:
            list1 (Optional[ListNode]): Head of the first sorted linked list.
            list2 (Optional[ListNode]): Head of the second sorted linked list.

        Returns:
            Optional[ListNode]: Head of the merged sorted linked list.
        """
        # If both lists are empty, return any of them (None in this case)
        if list1 is None and list2 is None:
            return list1
        # If one list is empty, return the other list
        if list1 is None or list2 is None:
            return list1 if list1 else list2

        # Determine the head of the merged list by selecting the smaller value
        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = seek

        # Merge the lists by iterating through the nodes
        while seek and target:
            # Move the seeker pointer until it's less than or equal to the target value
            while seek.next and seek.next.val < target.val:
                seek = seek.next

            # Swap pointers between seeker and target nodes
            seek.next, target = target, seek.next
            seek = seek.next

        return head

    def __merge_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Get the number of lists
        n: int = len(lists)

        # If there are no lists or the input list is None, return None
        if n == 0 or lists is None:
            return None

        # Initialize the head of the merged list with the first list
        head: ListNode = lists[0]

        # Merge each list with the merged list
        for i in range(1, n):
            head = self.__merge(list1=head, list2=lists[i])

        # Return the head of the merged list
        return head

    def __merge_using_pq(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge K sorted linked lists into one sorted linked list using a priority queue.

        Args:
            lists (List[Optional[ListNode]]): A list of K sorted linked lists.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.
        """
        # Initialize a priority queue
        pq = []

        # Insert the heads of non-empty lists into the priority queue
        for lst in lists:
            heapq.heappush(pq, (lst.val, ListNodeWrapper(lst)))

        # Initialize a dummy node to construct the merged linked list
        dummy: ListNode = ListNode(val=-1)
        temp: ListNode = dummy

        # Merge the lists using the priority queue
        while pq:
            # Pop the top element from the priority queue
            top = heapq.heappop(pq)
            # Append the node to the merged linked list
            temp.next = top[1].node
            # Move to the next node in the merged linked list
            temp = temp.next
            # If the current node has a next node, push it to the priority queue
            if top[1].node.next:
                heapq.heappush(
                    pq, (top[1].node.next.val, ListNodeWrapper(top[1].node.next))
                )

        # Return the head of the merged linked list
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # return self.__merge_lists(lists=lists)
        return self.__merge_using_pq(lists=lists)


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
    head1: ListNode = ListNode(1, ListNode(4, ListNode(5)))
    head2: ListNode = ListNode(1, ListNode(3, ListNode(4)))
    head3: ListNode = ListNode(2, ListNode(6))
    lists: List[ListNode] = [head1, head2, head3]
    solution: Solution = Solution()
    head: ListNode = solution.mergeKLists(lists=lists)
    print_list(head=head)
