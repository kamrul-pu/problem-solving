"""Two Sum in Binary Search Tree."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def __init__(self, root: Node) -> None:
        self.root = root
        self.first: Node = None
        self.prev: Node = None
        self.middle: Node = None
        self.last: Node = None

    def inorder(self, root: Node) -> None:
        if root is None:
            return
        self.inorder(root.left)
        if self.prev is not None and root.data < self.prev.data:
            # this is the first violation mark these two nodes as first and middle
            if self.first is None:
                self.first = self.prev
                self.middle = root
            # If this is second violation mark this node as last
            else:
                self.last = root
        # mark this node as previous
        self.prev = root
        self.inorder(root.right)

    def recover_bst(self) -> None:
        self.prev: Node = Node(float("-inf"))
        self.inorder(root=self.root)
        if self.first and self.last:
            self.first.data, self.last.data = self.last.data, self.first.data
        elif self.first and self.middle:
            self.first.data, self.middle.data = self.middle.data, self.first.data


def in_order(root: Node) -> None:
    if root is None:
        return
    in_order(root.left)
    print(root.data, end="->")
    in_order(root.right)


def build_tree() -> Node:
    root: Node = Node(3)
    root.left: Node = Node(1)
    root.right: Node = Node(4)
    root.right.right: Node = Node(2)
    return root


if __name__ == "__main__":
    root: Node = build_tree()
    in_order(root=root)
    print("None")
    solution = Solution(root=root)
    solution.recover_bst()
    in_order(root=root)
    print("None")
