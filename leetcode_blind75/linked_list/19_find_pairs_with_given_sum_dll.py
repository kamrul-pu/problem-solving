from typing import Optional, List


# Definition for singly Linked List Node
class Node:
    def __init__(self, x: int, next=None, prev=None):
        self.data: int = x
        self.next: Optional[Node] = next
        self.prev: Optional[Node] = prev


class Solution:
    def __f(self, target: int, head: Optional[Node]) -> List[List[int]]:
        """

        Args:
            target (int): The target sum.
            head (Optional[Node]): The head of the linked list.

        Returns:
            List[List[int]]: A list of pairs of nodes whose values sum up to the target.
        """
        ans: List[List[int]] = []
        if head is None or head.next is None:
            return ans

        # Loop through each node in the list
        temp1: Optional[Node] = head
        while temp1:
            # Start from the next node of temp1
            temp2: Optional[Node] = temp1.next
            while temp2:
                # Calculate the sum of nodes
                result: int = temp1.data + temp2.data
                if result == target:
                    ans.append([temp1.data, temp2.data])
                # If the sum is greater than the target, break out of the loop
                if result > target:
                    break
                temp2 = temp2.next

            temp1 = temp1.next

        return ans

    def __find(self, target: int, head: Optional[Node]) -> List[List[int]]:
        """

        Args:
            target (int): The target sum.
            head (Optional[Node]): The head of the linked list.

        Returns:
            List[List[int]]: A list of pairs of nodes whose values sum up to the target.
        """
        ans: List[List[int]] = []
        if head is None or head.next is None:
            return ans

        # Initialize two pointers: left and right
        tail: Optional[Node] = head
        while tail and tail.next:
            tail = tail.next

        left: Optional[Node] = head
        right: Optional[Node] = tail
        # Iterate until left pointer is less than right pointer
        while left and right and left.data < right.data:
            # Calculate the sum of nodes
            result: int = left.data + right.data
            if result > target:
                right = right.prev
            elif result < target:
                left = left.next
            else:
                ans.append([left.data, right.data])
                left = left.next
                right = right.prev

        return ans

    def findPairsWithGivenSum(
        self, target: int, head: Optional[Node]
    ) -> List[List[int]]:
        """
        Find pairs of nodes in the linked list that sum up to the given target value.

        Args:
            target (int): The target sum.
            head (Optional[Node]): The head of the linked list.

        Returns:
            List[List[int]]: A list of pairs of nodes whose values sum up to the target.
        """
        return self.__find(target=target, head=head)


def create_doubly_linked_list(values: List[int]) -> Optional[Node]:
    """
    Create a doubly linked list from a list of values.

    Args:
        values (List[int]): The list of values to create the linked list from.

    Returns:
        Optional[Node]: The head of the created linked list.
    """
    if not values:
        return None

    head: Node = Node(values[0])
    prev_node: Optional[Node] = head
    for val in values[1:]:
        new_node: Node = Node(val, prev=prev_node)
        prev_node.next = new_node
        prev_node = new_node

    return head


def print_list(head: Optional[Node]) -> None:
    """
    Print the linked list starting from the given head node.

    Args:
        head (Optional[Node]): The head node of the linked list.
    """
    current: Optional[Node] = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    values: List[int] = [1, 2, 4, 5, 6, 8, 9]
    head: Optional[Node] = create_doubly_linked_list(values)
    print_list(head)
    target: int = 7
    solution: Solution = Solution()
    print(solution.findPairsWithGivenSum(target=target, head=head))
