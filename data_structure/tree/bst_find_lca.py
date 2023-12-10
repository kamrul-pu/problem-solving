"""Find LCA in Binary Search Tree."""


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


def lowest_common_anchestor(root: Node, p: int, q: int) -> Node:
    if root is None:
        return None
    curr: int = root.data
    if curr < p and curr < q:
        return lowest_common_anchestor(root.right, p, q)
    if curr > p and curr > q:
        return lowest_common_anchestor(root.left, p, q)
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


if __name__ == "__main__":
    elements: list[int] = [5, 7, 8, 1, 2, 4, 3, 6]
    root: Node = build_tree(elements=elements)
    in_order(root)
    print("None")
    lca: Node = lowest_common_anchestor(root=root, p=4, q=6)
    print(lca.data)
