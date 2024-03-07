"""Binary Tree Traversal in pre post combined."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.pre_order: list[int] = []
        self.in_order: list[int] = []
        self.post_order: list[int] = []

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

    def traverse(self) -> None:
        if self is None:
            return  # there is nothing in the tree
        stack: list[list[Node, int]] = []
        stack.append([self, 1])

        while stack:
            top: list[Node, int] = stack[-1]
            num: int = top[1]
            if num == 1:
                # pre order
                self.pre_order.append(top[0].data)
                stack[-1][1] += 1
                if top[0].left:
                    stack.append([top[0].left, 1])
            if num == 2:
                # in order
                self.in_order.append(top[0].data)
                stack[-1][1] += 1
                if top[0].right:
                    stack.append([top[0].right, 1])
            if num == 3:
                # post order
                self.post_order.append(top[0].data)
                stack.pop()
        print("traverse completed")


def build_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)

    root.left.left = Node(3)
    root.left.right = Node(4)

    root.right.left = Node(6)
    root.right.right = Node(7)

    return root


if __name__ == "__main__":
    root = build_tree()
    root.traverse()
    print(root.pre_order, sep="->", end="\n")
    print(root.in_order, sep="->", end="\n")
    print(root.post_order, sep="->", end="\n")
