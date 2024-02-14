"""Merge two sorted list."""

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __merge_optimal(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return list1
        if list1 is None or list2 is None:
            return list1 if list2 is None else list2

        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)

        head = seek
        while seek and target:
            while seek.next and seek.next.val < target.val:
                seek = seek.next

            seek.next, target = target, seek.next
            seek = seek.next

        return head

    def __merge(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return list1
        if list1 is None or list2 is None:
            return list1 if list2 is None else list2

        temp1: ListNode = list1
        temp2: ListNode = list2
        if temp1.val < temp2.val:
            new_list: ListNode = temp1
            temp1 = temp1.next
        else:
            new_list = temp2
            temp2 = temp2.next
        head: ListNode = new_list
        cur: ListNode = new_list
        while temp1 and temp2:
            if temp1.val < temp2.val:
                cur.next = temp1
                temp1 = temp1.next
                cur = cur.next
            else:
                cur.next = temp2
                temp2 = temp2.next
                cur = cur.next

        while temp1:
            cur.next = temp1
            temp1 = temp1.next
            cur = cur.next

        while temp2:
            cur.next = temp2
            temp2 = temp2.next
            cur = cur.next

        return head

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return self.__merge_optimal(list1, list2)
        # return self.__merge(list1=list1, list2=list2)

    def print_list(self, head: Optional[ListNode]) -> None:
        cur: ListNode = head
        while cur:
            print(cur.val, end="->")
            cur = cur.next

        print("NUll")


if __name__ == "__main__":
    list1: ListNode = ListNode(val=1)
    node2: ListNode = ListNode(val=2)
    node3: ListNode = ListNode(val=4)
    list1.next = node2
    node2.next = node3

    list2: ListNode = ListNode(val=1)
    list2.next = ListNode(val=3)
    list2.next.next = ListNode(val=4)

    solution: Solution = Solution()
    solution.print_list(head=list1)
    solution.print_list(head=list2)
    n_head = solution.mergeTwoLists(list1=list1, list2=list2)
    solution.print_list(head=n_head)
