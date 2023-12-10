"""Create Binary Search Tree from pre order traversal."""


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


def build(elements: list[int], i: list[int], bound: int) -> Node:
    if i[0] == len(elements) or (elements[i[0]] > bound):
        return None
    root: Node = Node(elements[i[0]])
    i[0] += 1
    root.left: Node = build(elements=elements, i=i, bound=root.data)
    root.right: Node = build(elements=elements, i=i, bound=bound)
    return root


def build_bst_from_preorder(elements: list[int]) -> Node:
    i: list[int] = [0]
    return build(elements=elements, i=i, bound=float("inf"))


if __name__ == "__main__":
    elements: list[int] = [8, 5, 1, 7, 10, 12]
    root: Node = build_tree(elements=elements)
    in_order(root)
    print("None")
    print(root.right.right.data)
    root1: Node = build_bst_from_preorder(elements=elements)
    in_order(root=root1)
    print("None")
