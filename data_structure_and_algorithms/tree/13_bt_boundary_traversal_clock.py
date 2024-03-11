"""Binary tree boundary traversal clockwise"""

from typing import List, Optional


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def __is_leaf(self, node: Optional[Node]) -> bool:
        # Helper function to check if a node is a leaf node (has no children).
        return node.left == None and node.right == None

    def __right_boundary_clock(self, root: Optional[Node], result: List[int]) -> None:
        # Helper function to traverse and collect the right boundary of the tree in a clockwise manner.
        # It starts from the root's right child and iteratively moves down to the rightmost non-leaf node.
        curr: Node = root.right
        while curr:
            if not self.__is_leaf(node=curr):
                result.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

    def __left_boundary_clock(self, root: Optional[Node], result: List[int]) -> None:
        # Helper function to traverse and collect the left boundary of the tree in a clockwise manner.
        # It starts from the root's left child and iteratively moves down to the leftmost non-leaf node.
        curr: Node = root.left
        tmp: List[int] = (
            []
        )  # Temporary storage for left boundary nodes (excluding leaves).
        while curr:
            if not self.__is_leaf(node=curr):
                tmp.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

        # Add the collected left boundary nodes (excluding leaves) to the result list.
        while tmp:
            result.append(tmp.pop())

    def __add_leaves(self, node: Optional[Node], result: List[int]) -> None:
        # Helper function to collect all the leaf nodes in the tree.
        if self.__is_leaf(node):
            result.append(node.data)
            return
        if node.left:
            self.__add_leaves(node.left, result)
        if node.right:
            self.__add_leaves(node.right, result)

    def boundary_clock(self, root: Optional[Node]) -> List[int]:
        # Main function to compute the boundary of the tree in a clockwise manner.
        result: List[int] = []
        if root is None:
            return result

        if not self.__is_leaf(root):
            result.append(root.data)

        leaves: List[int] = []  # Temporary storage for collecting leaf nodes.
        # Collect the right boundary, leaves, and left boundary in a clockwise manner.
        self.__right_boundary_clock(root=root, result=result)
        self.__add_leaves(node=root, result=leaves)
        # Reverse the order of collected leaves and add them to the result list.
        while leaves:
            result.append(leaves.pop())
        self.__left_boundary_clock(root=root, result=result)

        return result


def build_tree():
    # Build a sample binary tree for testing purposes.
    root = Node(-10)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    return root


if __name__ == "__main__":
    # Build a sample binary tree.
    root = build_tree()
    solution: Solution = Solution()
    print(solution.boundary_clock(root=root))
