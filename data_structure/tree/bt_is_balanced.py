"""Binary Tree Maximum Height."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def max_height(self, root) -> int:
        if root is None:
            return 0
        lh: int = self.max_height(root.left)
        rh: int = self.max_height(root.right)
        if lh == -1 or rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)

    def is_balance(self) -> bool:
        return self.max_height(root=self) != -1


def is_balanced(root: Node) -> int:
    if root is None:
        return 0
    lh: int = is_balanced(root.left)
    rh: int = is_balanced(root.right)

    if lh == -1 or rh == -1:
        return -1

    if abs(lh - rh) > 1:
        return -1

    return max(lh, rh) + 1


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
    print(is_balanced(root))
    print(root.is_balance())
