"""Dia meter of a binary tree."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def find_max(self, node, maxi: list[int]) -> int:
        if node is None:
            return 0

        lh: int = self.find_max(node.left, maxi)
        rh: int = self.find_max(node.right, maxi)

        maxi[0] = max(maxi[0], lh + rh)

        return 1 + max(lh, rh)

    def diameter_of_bt(self, maxi: list[int]) -> int:
        self.find_max(self, maxi)
        return maxi[0]


def build_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.left.right.left = Node(6)
    root.left.right.right = Node(7)

    return root


if __name__ == "__main__":
    root = build_tree()
    # print(root.max_height(root))
    maxi: list[int] = [0]
    print(root.diameter_of_bt(maxi))
