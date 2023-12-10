"""Two Sum in Binary Search Tree."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root: Node, is_reversed: bool) -> None:
        self.stack: list[Node] = []
        self.reverse: bool = is_reversed
        self.push_all(root)

    def push_all(self, node: Node) -> None:
        while node is not None:
            self.stack.append(node)
            if self.reverse:
                node = node.right
            else:
                node = node.left

    def has_next(self):
        return len(self.stack) != 0

    def next(self) -> int:
        if self.has_next():
            node: Node = self.stack.pop()
            if not self.reverse:
                self.push_all(node.right)
            else:
                self.push_all(node.left)
            return node.data
        return 0


def tow_sum(root: Node, key: int) -> bool:
    if root is None:
        return False
    left = BSTIterator(root=root, is_reversed=False)
    right = BSTIterator(root=root, is_reversed=True)
    i: int = left.next()
    j: int = right.next()
    while i < j:
        if i + j == key:
            return True
        elif (i + j) < key:
            i = left.next()
        else:
            j = right.next()

    return False


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


if __name__ == "__main__":
    elements: list[int] = [8, 5, 1, 7, 10, 12]
    root: Node = build_tree(elements=elements)
    in_order(root)
    print("None")
    key: int = 14
    print(tow_sum(root=root, key=key))
