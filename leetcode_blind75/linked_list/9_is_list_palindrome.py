"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initialize a ListNode with a given value and optional next node.

        Parameters:
            val (int): The value of the node.
            next (ListNode): Reference to the next node (default is None).
        """
        self.val = val
        self.next = next


class Solution:
    def __f(self, head: Optional[ListNode]) -> bool:
        """
        Helper function to determine if a linked list is a palindrome using list conversion.

        Parameters:
            head (Optional[ListNode]): The head node of the linked list.

        Returns:
            bool: True if the linked list is a palindrome, False otherwise.
        """
        if head.next is None:
            return True

        # Convert linked list to a list
        l_list: List[int] = []
        cur: ListNode = head
        while cur:
            l_list.append(cur.val)
            cur = cur.next

        # Check if the list is a palindrome
        low: int = 0
        high: int = len(l_list) - 1
        while low < high:
            if l_list[low] != l_list[high]:
                return False
            low += 1
            high -= 1
        return True

    def __reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Helper function to reverse a linked list.

        Parameters:
            head (Optional[ListNode]): The head node of the linked list.

        Returns:
            Optional[ListNode]: The head node of the reversed linked list.
        """
        if head is None or head.next is None:
            return head

        # Reverse the linked list
        temp: ListNode = head
        prev: ListNode = None
        while temp:
            front: ListNode = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def __palindrome_optimal(self, head: ListNode) -> bool:
        """
        Helper function to determine if a linked list is a palindrome using optimal approach.

        Parameters:
            head (ListNode): The head node of the linked list.

        Returns:
            bool: True if the linked list is a palindrome, False otherwise.
        """
        if head is None or head.next is None:
            return True

        # Find the middle of the linked list
        slow: ListNode = head
        fast: ListNode = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half of the linked list
        new_head: ListNode = self.__reverse(head=slow.next)

        # Compare the first and second halves of the linked list
        first: ListNode = head
        second: ListNode = new_head
        while second:
            if first.val != second.val:
                self.__reverse(head=new_head)
                return False
            first = first.next
            second = second.next
        self.__reverse(head=new_head)
        return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Determine if a linked list is a palindrome.

        Parameters:
            head (Optional[ListNode]): The head node of the linked list.

        Returns:
            bool: True if the linked list is a palindrome, False otherwise.
        """
        # Uncomment one of the following methods to use
        # return self.__f(head=head)
        # return self.__palindrome(node=head)
        return self.__palindrome_optimal(head=head)


if __name__ == "__main__":
    head: ListNode = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    solution: Solution = Solution()
    print(solution.isPalindrome(head=head))
