"""Remove nth node from the end of the linked list."""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        cnt: int = 0
        cur: ListNode = head
        while cur:
            cnt += 1
            cur = cur.next
        if cnt == n:
            head = head.next
            return head
        if n > cnt:
            return head
        target: int = cnt - n - 1
        cur: ListNode = head
        while target:
            target -= 1
            cur = cur.next
        cur.next = cur.next.next
        return head

    def print_list(self, head: Optional[ListNode]) -> None:
        cur: ListNode = head
        while cur:
            print(cur.val, end="->")
            cur = cur.next

        print("NUll")


if __name__ == "__main__":
    head: ListNode = ListNode(val=1)
    head.next = ListNode(val=2)
    head.next.next = ListNode(val=3)
    head.next.next.next = ListNode(val=4)
    head.next.next.next.next = ListNode(val=5)
    solution: Solution = Solution()
    solution.print_list(head=head)
    print(solution.removeNthFromEnd(head=head, n=2))
    solution.print_list(head=head)
