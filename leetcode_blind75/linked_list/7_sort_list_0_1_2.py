"""
Sort linked list 0 1 2
"""

from typing import List, Optional


# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __sort(self, head: Optional[Node]) -> Optional[Node]:
        """
        Sort the linked list containing 0s, 1s, and 2s using counting sort.

        Parameters:
            head (Optional[Node]): The head node of the linked list.

        Returns:
            Optional[Node]: The head node of the sorted linked list.
        """

        # Count occurrences of 0s, 1s, and 2s
        count: List[int] = [0, 0, 0]
        cur: Node = head
        while cur:
            count[cur.val] += 1
            cur = cur.next

        # Update node values according to count array
        cur = head
        for i in range(3):
            while count[i]:
                cur.val = i
                count[i] -= 1
                cur = cur.next

        return head

    def __sort_optimal(self, head: Optional[Node]) -> Optional[Node]:
        """
        Sort the linked list containing 0s, 1s, and 2s using three separate pointers.

        Parameters:
            head (Optional[Node]): The head node of the linked list.

        Returns:
            Optional[Node]: The head node of the sorted linked list.
        """

        # Initialize pointers for nodes with values 0, 1, and 2
        zero_head = zero = Node(-1)
        one_head = one = Node(-1)
        two_head = two = Node(-1)
        temp: Node = head

        # Traverse the linked list and append nodes to respective pointers
        while temp:
            if temp.val == 0:
                zero.next = temp
                zero = zero.next
            elif temp.val == 1:
                one.next = temp
                one = one.next
            else:
                two.next = temp
                two = two.next

            temp = temp.next

        # Connect the three lists and return the head of the sorted list
        zero.next = one_head.next if one_head.next else two_head.next
        one.next = two_head.next
        two.next = None

        return zero_head.next

    def sort_0_1_2(self, head: Optional[Node]) -> Optional[Node]:
        """
        Sort the linked list containing 0s, 1s, and 2s.

        Parameters:
            head (Optional[Node]): The head node of the linked list.

        Returns:
            Optional[Node]: The head node of the sorted linked list.
        """
        if head is None or head.next is None:
            return head

        # Call the optimal sorting method for sorting
        return self.__sort_optimal(head=head)


def print_list(head: Node) -> None:
    """
    Print the linked list starting from the given head node.

    Parameters:
        head (Node): The head node of the linked list.
    """
    node: Node = head
    while node:
        print(node.val, end="->")
        node = node.next
    print("Null")


def build_list() -> Node:
    head: Node = Node(
        val=1,
        next=Node(
            val=0,
            next=Node(
                val=2,
                next=Node(
                    val=1,
                    next=Node(
                        val=0,
                        next=Node(val=1, next=Node(val=2)),
                    ),
                ),
            ),
        ),
    )
    return head


if __name__ == "__main__":
    head = build_list()
    print_list(head=head)
    solution: Solution = Solution()
    head = solution.sort_0_1_2(head=head)
    print_list(head=head)
