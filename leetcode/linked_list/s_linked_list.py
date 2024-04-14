from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head: Optional[ListNode]) -> None:
    cur: ListNode = head
    while cur:
        print(cur.val, end="->")
        cur = cur.next

    print("NUll")


def create_list(nums: List[int]) -> Optional[ListNode]:
    head: ListNode = ListNode(val=nums[0])
    tail: ListNode = head
    n: int = len(nums)
    for i in range(1, n):
        tail.next = ListNode(nums[i])
        tail = tail.next

    return head


if __name__ == "__main__":
    nums: List[int] = [1, 2, 3, 4, 5]
    head = create_list(nums=nums)
    print_list(head=head)
