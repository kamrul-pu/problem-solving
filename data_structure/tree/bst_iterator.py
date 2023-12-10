"""Successors predecessor of Binary Search Tree"""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root: Node) -> None:
        self.stack: list[Node] = []
        self.push_all(root)

    def push_all(self, node: Node) -> None:
        while node is not None:
            self.stack.append(node)
            node = node.left

    def has_next(self):
        return len(self.stack) != 0

    def next(self) -> int:
        if self.has_next():
            node: Node = self.stack.pop()
            self.push_all(node.right)
            return node.data
        return None


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


def in_order(root: Node, in_order_list: list[int]) -> None:
    if root is None:
        return
    in_order(root.left, in_order_list)
    in_order_list.append(root.data)
    print(root.data, end="->")
    in_order(root.right, in_order_list)


def build_tree(elements: list[int]) -> Node:
    root = Node(elements[0])
    for i in range(1, len(elements)):
        insert_node(root=root, data=elements[i])

    return root


if __name__ == "__main__":
    elements: list[int] = [8, 5, 1, 7, 10, 12]
    root: Node = build_tree(elements=elements)
    in_order_list: list[int] = []
    in_order(root, in_order_list)
    print("None")
    iterator = BSTIterator(root=root)
    print(iterator.next())
    print(iterator.next())
    print(iterator.has_next())
    print(iterator.next())
    print(iterator.has_next())
    print(iterator.next())
    print(iterator.has_next())
    print(iterator.next())
    print(iterator.has_next())
    print(iterator.next())
    print(iterator.has_next())
    print(iterator.next())
