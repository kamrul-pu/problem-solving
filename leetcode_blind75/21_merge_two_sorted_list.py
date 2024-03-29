from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}"


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1

        if not list1 or not list2:
            return list1 if not list2 else list2

        seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = seek

        while seek and target:
            while seek.next and seek.next.val < target.val:
                seek = seek.next
            seek.next, target = target, seek.next
            seek = seek.next

        return head


list1: ListNode = ListNode(1)
l1 = list1.next = ListNode(2)
l2 = l1.next = ListNode(4)

list2: ListNode = ListNode(1)
l21 = list2.next = ListNode(3)
l22 = l21.next = ListNode(4)

solution: Solution = Solution()
l3 = solution.mergeTwoLists(list1=list1, list2=list2)

temp = l3

while temp:
    print(temp.val, end="->")
    temp = temp.next
print("NULL")
