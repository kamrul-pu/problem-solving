"""Reverse linked List."""

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __reverse_data(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st: List[int] = []
        cur: ListNode = head
        # traverse the whole list and insert in stack
        while cur:
            st.append(cur.val)
            cur = cur.next

        # pop each element in the list and put it in reverse manager
        cur: ListNode = head
        while st:
            top: int = st.pop()
            cur.val = top
            cur = cur.next
        return head

    def __reverse_optimal(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev: ListNode = None
        cur: ListNode = head

        while cur:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next

        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.__reverse_data(head=head)
        return self.__reverse_optimal(head=head)

    def print_list(self, head: Optional[ListNode]) -> None:
        cur: ListNode = head
        while cur:
            print(cur.val, end="->")
            cur = cur.next

        print("NUll")


if __name__ == "__main__":
    head: ListNode = ListNode(val=1)
    node2: ListNode = ListNode(val=2)
    node3: ListNode = ListNode(val=3)
    node4: ListNode = ListNode(val=4)
    node5: ListNode = ListNode(val=5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution: Solution = Solution()
    solution.print_list(head=head)
    n_head = solution.reverseList(head=head)
    solution.print_list(head=n_head)
