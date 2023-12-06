"""Binary Search Tree Left<Root<Right."""


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

    def find_node(self, data: int) -> bool:
        if self.data == data:
            return True
        if self.data > data:
            # may be in the left subtree
            if self.left:
                return self.left.find_node(data)
            else:
                return False
        else:
            # may be in the right subtree
            if self.right:
                return self.right.find_node(data)
            else:
                return False


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
    print(root.find_node(7))
