"""Binary Tree Maximum Height."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == data:
            return  # duplicate not allowed
        if data < self.data:
            # add in the left subtree
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            # add in the right subtree
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def search(self, val) -> bool:
        if self.data == val:
            return True

        if val < self.data:
            # may be in the left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            # may be in the right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def max_depth(self) -> int:
        if self is None:
            return 0
        lh: int = 0
        rh: int = 0
        if self.left:
            lh = self.left.max_depth()
        if self.right:
            rh = self.right.max_depth()

        return 1 + max(lh, rh)

    def max_height(self, root) -> int:
        if root is None:
            return 0
        lh: int = self.max_height(root.left)
        rh: int = self.max_height(root.right)

        return 1 + max(lh, rh)


def tree_height(root: Node) -> int:
    if root is None:
        return 0
    lh: int = tree_height(root.left)
    rh: int = tree_height(root.right)

    return 1 + max(lh, rh)


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
    print(root.max_depth())
    print(tree_height(root))
    print(root.max_height(root))
