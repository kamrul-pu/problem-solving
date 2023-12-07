"""Binary Search Tree Find Ceil value. i.e value>=key."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, data: int) -> None:
        if self.data == data:
            return

        if data > self.data:
            # insert in the right subtree
            if self.right:
                self.right.insert_node(data)
            else:
                self.right = Node(data)
        else:
            # insert in the left subtree
            if self.left:
                self.left.insert_node(data)
            else:
                self.left = Node(data)


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


def build_tree() -> None:
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)

    return root


if __name__ == "__main__":
    root: Node = build_tree()
    in_order(root=root)
    print("None")
    root.insert_node(data=5)
    in_order(root=root)
    print("None")

    root = insert_node(root=root, data=6)
    root = insert_node(root=root, data=0)
    in_order(root=root)
