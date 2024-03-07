"""Binary Search Tree Delete a Node."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


def find_last_right(root: Node) -> Node:
    if root.right is None:
        return root
    return find_last_right(root.right)


def find_last_left(root: Node) -> Node:
    if root.left is None:
        return root
    return find_last_left(root.left)


def helper(root: Node) -> Node:
    if root.left is None:
        return root.right
    elif root.right is None:
        return root.left
    right_child: Node = root.right
    last_right: Node = find_last_right(root.left)
    last_right.right = right_child
    return root.left


def delete_node(root: Node, key: int) -> Node:
    if root is None:
        return None
    if root.data == key:
        return helper(root)
    dummy: Node = root
    while root:
        if root.data > key:
            if root.left is not None and root.left.data == key:
                root.left = helper(root.left)
                break
            else:
                root = root.left
        else:
            if root.right is not None and root.right.data == key:
                root.right = helper(root.right)
                break
            else:
                root = root.right
    return dummy


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
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.right.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)

    return root


if __name__ == "__main__":
    root: Node = build_tree()
    in_order(root=root)
    print("None")
    root = insert_node(root=root, data=5)
    root = insert_node(root=root, data=0)
    in_order(root=root)
    print("None")
    delete_node(root=root, key=3)
    in_order(root=root)
