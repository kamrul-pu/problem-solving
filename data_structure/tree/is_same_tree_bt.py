"""Is the both tree are identical?"""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def same_tree(self, node1, node2):
        if node1 is None or node2 is None:
            return node1 == node2
        return (
            (node1.data == node2.data)
            and self.same_tree(node1.left, node2.left)
            and self.same_tree(node1.right, node2.right)
        )


def build_tree():
    root = Node(-10)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    return root


def build_tree2():
    root = Node(-10)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    # root.right.right = Node(7)

    return root


if __name__ == "__main__":
    root1 = build_tree()
    root2 = build_tree2()
    print(root1.same_tree(root1, root2))
