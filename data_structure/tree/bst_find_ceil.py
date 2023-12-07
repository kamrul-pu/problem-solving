"""Binary Search Tree Find Ceil value. i.e value>=key."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data: int) -> None:
        if self.data == data:
            return
        if data > self.data:
            # add in the right subtree.
            if self.right:
                self.right.add_node(data)
            else:
                self.right = Node(data)
        else:
            # add in the left subtree
            if self.left:
                self.left.add_node(data)
            else:
                self.left = Node(data)

    def in_order(self) -> None:
        if self is None:
            print("None")
            return
        if self.left:
            self.left.in_order()
        print(self.data, end="->")
        if self.right:
            self.right.in_order()

    def find_ceil(self, key: int, ceil: list[int]) -> int:
        if self.data >= key:
            ceil[0] = min(ceil[0], self.data)
            if self.left:
                self.left.find_ceil(key, ceil)
        else:
            if self.right:
                self.right.find_ceil(key, ceil)


def find_ceil(root: Node, key: int) -> int:
    ceil: int = -1
    while root:
        if root.data == key:
            ceil = root.data
            return ceil

        if root.data > key:
            ceil = root.data
            root = root.left
        else:
            root = root.right

    return ceil


def in_order(root: Node) -> None:
    if root is None:
        return
    in_order(root.left)
    print(root.data, end="->")
    in_order(root.right)


if __name__ == "__main__":
    root = Node(8)
    nodes: list[int] = [1, 3, 6, 4, 7, 14, 10, 13]
    for node in nodes:
        root.add_node(node)

    root.in_order()
    in_order(root=root)
    print()
    ceil: list[int] = [99999]
    root.find_ceil(key=11, ceil=ceil)
    print("ceil", ceil)
    print(find_ceil(root=root, key=11))
