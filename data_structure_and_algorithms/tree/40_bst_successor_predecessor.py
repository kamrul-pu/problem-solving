"""Successors predecessor of Binary Search Tree"""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


def insert_node(root: Node, data: int) -> Node:
    """Iterative approach."""
    if root is None:
        return Node(data)

    cur: Node = root
    while True:
        if cur.data <= data:
            # insert in the right
            if cur.right:
                cur = cur.right
            else:
                cur.right = Node(data)
                break
        else:
            # insert in the left subtree
            if cur.left:
                cur = cur.left
            else:
                cur.left = Node(data)
                break

    return root


def in_order(root: Node) -> None:
    if root is None:
        return
    in_order(root.left)
    print(root.data, end="->")
    in_order(root.right)


def build_tree(elements: list[int]) -> Node:
    root = Node(elements[0])
    for i in range(1, len(elements)):
        insert_node(root=root, data=elements[i])

    return root


def find_successor(root: Node, data: int) -> int:
    if root is None:
        return None
    successor: int = None
    curr: Node = root
    while curr:
        if curr.data > data:
            # successors may be in the left portion
            successor = curr.data
            curr = curr.left
        else:
            # successors may be in the right subtree
            curr = curr.right

    return successor


def find_predicessor(root: Node, data: int) -> int:
    if root is None:
        return None
    predecessor: int = None
    curr: Node = root
    while curr:
        if curr.data < data:
            # successors may be in the right portion
            predecessor = curr.data
            curr = curr.right
        else:
            # successors may be in the left subtree
            curr = curr.left

    return predecessor


if __name__ == "__main__":
    elements: list[int] = [8, 5, 1, 7, 10, 12]
    root: Node = build_tree(elements=elements)
    in_order(root)
    print("None")
    print(find_successor(root=root, data=10))
    print(find_predicessor(root=root, data=10))
