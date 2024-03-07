"""Check if a Binary Search Tree is Valid or not."""


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


def is_valid_bst(root: Node, mn: int, mx: int) -> bool:
    if root is None:
        return True
    if root.data >= mx or root.data <= mn:
        return False
    return is_valid_bst(root.left, mn, root.data) and is_valid_bst(
        root.right, root.data, mx
    )


def is_valid_bst_util(root: Node) -> bool:
    INT_MIN = -99999
    INT_MAX = 99999
    return is_valid_bst(root=root, mn=INT_MIN, mx=INT_MAX)


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


if __name__ == "__main__":
    elements: list[int] = [5, 7, 8, 1, 2, 4, 3, 6]
    root: Node = build_tree(elements=elements)
    in_order(root)
    print("None")
    print(is_valid_bst_util(root=root))
