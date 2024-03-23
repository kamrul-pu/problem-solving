"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:
"""

from typing import Dict, Optional


from typing import Dict, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        """
        Initialize a ListNode with a value and an optional next pointer.

        Parameters:
            x: The value stored in the node.
            next: Reference to the next ListNode, default is None.
        """
        self.val = x
        self.next = next


class Solution:
    def __f(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Find the intersection point of two linked lists using a dictionary.

        Parameters:
            headA: The head of the first linked list.
            headB: The head of the second linked list.

        Returns:
            ListNode: The intersection node if exists, otherwise None.
        """
        if headA is None or headB is None:
            return None

        temp1: ListNode = headA
        first_list: Dict[bool] = dict()

        # Store all nodes of the first list in a dictionary
        while temp1:
            first_list[temp1] = True
            temp1 = temp1.next

        # Traverse the second list, return the intersection node if found
        temp2: ListNode = headB
        while temp2:
            if temp2 in first_list:
                return temp2
            temp2 = temp2.next

        return None

    def __collision_point(self, temp1: ListNode, temp2: ListNode, d: int) -> ListNode:
        """
        Find the collision point of two linked lists.

        Parameters:
            temp1: A pointer to the head of the first linked list.
            temp2: A pointer to the head of the second linked list.
            d: The difference in length between the two lists.

        Returns:
            ListNode: The node at which the two lists intersect.
        """
        # Move the pointer of the longer list d steps forward
        while d:
            d -= 1
            temp2 = temp2.next

        # Move both pointers until they meet at the intersection node
        while temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next

        return temp1

    def __helper(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Helper function to find the intersection point of two linked lists.

        Parameters:
            headA: The head of the first linked list.
            headB: The head of the second linked list.

        Returns:
            ListNode: The intersection node if exists, otherwise None.
        """
        # Calculate the lengths of both lists
        n1: int = 0
        n2: int = 0
        temp1: ListNode = headA
        temp2: ListNode = headB

        while temp1:
            n1 += 1
            temp1 = temp1.next
        while temp2:
            n2 += 1
            temp2 = temp2.next

        # Adjust the pointers to have the same number of nodes remaining
        if n1 < n2:
            return self.__collision_point(headA, headB, n2 - n1)
        return self.__collision_point(headB, headA, n1 - n2)

    def __collision_point_optimal(self, head_1: ListNode, head_2: ListNode) -> ListNode:
        """
        Find the intersection point of two linked lists using optimal pointer manipulation.

        Parameters:
            head_1: The head of the first linked list.
            head_2: The head of the second linked list.

        Returns:
            ListNode: The intersection node if exists, otherwise None.
        """
        t1: ListNode = head_1
        t2: ListNode = head_2

        while t1 != t2:
            t1 = t1.next
            t2 = t2.next

            # If the end of one list is reached, start from the head of the other list
            if t1 is None and t2:
                t1 = head_2
            if t2 is None and t1:
                t2 = head_1

        return t1

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        """
        Find the intersection node of two linked lists.

        Parameters:
            headA: The head of the first linked list.
            headB: The head of the second linked list.

        Returns:
            ListNode: The intersection node if exists, otherwise None.
        """
        if headA is None or headB is None:
            return None
        return self.__collision_point_optimal(head_1=headA, head_2=headB)


def print_list(head: ListNode) -> None:
    node: ListNode = head
    while node:
        print(node.val, end="->")
        node = node.next
    print("Null")


if __name__ == "__main__":
    common: ListNode = ListNode(4, ListNode(6, ListNode(2)))
    head_1: ListNode = ListNode(3, ListNode(1, common))
    head_2: ListNode = ListNode(1, ListNode(2, ListNode(4, ListNode(5, common))))

    print_list(head=common)
    print_list(head=head_1)
    print_list(head=head_2)
    solution: Solution = Solution()
    collision_node: ListNode = solution.getIntersectionNode(head_1, head_2)
    print(collision_node.val if collision_node else "Null")
