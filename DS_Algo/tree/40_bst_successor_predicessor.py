from typing import Optional


class Node:
    def __init__(self, val) -> None:
        """
        Initializes a node of the binary tree.

        Parameters:
            val (int): The value of the node.
        """
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def get_successor(self, root: Optional[Node], key: int) -> Node:
        """
        Finds the successor node of a given key in the binary tree.

        Parameters:
            root (Optional[Node]): The root node of the binary tree.
            key (int): The value whose successor is to be found.

        Returns:
            Optional[Node]: The successor node of the given key.
        """
        if root is None:
            return None
        successor: Node = None
        curr: Node = root
        while curr:
            if curr.val > key:
                # If current node's value is greater than the key, move left
                successor = curr
                curr = curr.left
            else:
                # If current node's value is less than or equal to the key, move right
                curr = curr.right
        return successor

    def get_predicessor(self, root: Optional[Node], key: int) -> Node:
        """
        Finds the predecessor node of a given key in the binary tree.

        Parameters:
            root (Optional[Node]): The root node of the binary tree.
            key (int): The value whose predecessor is to be found.

        Returns:
            Optional[Node]: The predecessor node of the given key.
        """
        if root is None:
            return None
        predicessor: Node = None
        curr: Node = root
        while curr:
            if curr.val < key:
                # If current node's value is less than the key, move right
                predicessor = curr
                curr = curr.right
            else:
                # If current node's value is greater than or equal to the key, move left
                curr = curr.left
        return predicessor


def build_tree() -> Node:
    """
    Helper method to build a sample binary tree for testing.

    Returns:
        Node: The root node of the constructed binary tree.
    """
    root: Node = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.right = Node(7)
    return root


if __name__ == "__main__":
    # Build the binary search tree
    root: Node = build_tree()

    # Create an instance of Solution class
    solution: Solution = Solution()

    # Find the successor and predecessor nodes for the key value
    successor: Node = solution.get_successor(root=root, key=60)
    predicessor: Node = solution.get_predicessor(root=root, key=60)

    # Print the values of the successor and predecessor nodes
    print(successor.val if successor else "Null")
    print(predicessor.val if predicessor else "Null")
