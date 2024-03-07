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

    def find_floor(self, key: int, floor: list[int]) -> int:
        if self.data <= key:
            floor[0] = max(floor[0], self.data)
            if self.right:
                self.right.find_floor(key, floor)
        else:
            if self.left:
                self.left.find_floor(key, floor)


def find_floor(root: Node, key: int) -> int:
    floor: int = -1
    while root:
        if root.data == key:
            floor = root.data
            return floor
        if root.data <= key:
            floor = root.data
            root = root.right
        else:
            root = root.left

    return floor


def in_order(root: Node) -> None:
    if root is None:
        return
    in_order(root.left)
    print(root.data, end="->")
    in_order(root.right)


if __name__ == "__main__":
    root = Node(8)
    nodes: list[int] = [10, 5, 2, 6, 15]
    for node in nodes:
        root.add_node(node)

    in_order(root=root)
    print()
    keys: list[int] = [7, 10, 15, 5, 3, 2, 1]

    for key in keys:
        floor: list[int] = [-1]
        root.find_floor(key=key, floor=floor)
        print(f"floor for {key} is {floor[0]} class method")
        print(f"floor for {key} is {find_floor(root=root, key=key)} func")
