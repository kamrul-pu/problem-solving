"""Binary Tree Level Order Traversal."""

from collections import deque
from typing import List, Deque


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def level_order_trversal(root):
    ans: List[List[int]] = []

    # Return null if the tree is empty
    if root is None:
        return ans
    # Initialize queue
    queue: Deque = deque()
    queue.append(root)

    # iterate the queue until it's empty
    while queue:
        # check the length of queue
        curr_size = len(queue)
        curr_list: List[int] = []

        while curr_size > 0:
            curr_node = queue.popleft()
            curr_list.append(curr_node.data)
            curr_size -= 1

            # check for the left child
            if curr_node.left is not None:
                queue.append(curr_node.left)
            # check for the right child
            if curr_node.right is not None:
                queue.append(curr_node.right)

        # append the curr_list to answer after each iteration
        ans.append(curr_list)

    # return the answer
    return ans


def level_wise_traversal(root: TreeNode) -> List[List[int]]:
    ans: List[List[int]] = []
    if root is None:
        return ans

    q = deque()
    q.append(root)

    while q:
        size: int = len(q)
        curr_list: List[int] = []
        for i in range(0, size):
            curr_node = q.popleft()
            curr_list.append(curr_node.data)

            if curr_node.left is not None:
                q.append(curr_node.left)
            if curr_node.right is not None:
                q.append(curr_node.right)

        ans.append(curr_list)

    return ans


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(level_order_trversal(root))
    print(level_wise_traversal(root))
