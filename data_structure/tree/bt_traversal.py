"""Binary Tree Pre order Traversal."""


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

    def pre_order_traversal(self):
        # root left right
        if self == None:
            return
        print(self.data, end="->")
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def in_order_traversal(self):
        # left Root Right
        elements: list[int] = []
        # visit left sybtree
        if self.left:
            elements += self.left.in_order_traversal()
        print(self.data, end="->")
        # visit base node
        elements.append(self.data)
        # visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        # left -> right -> root
        elements: list[int] = []
        # visit the left subtree
        if self.left:
            elements += self.left.post_order_traversal()
        # visit the right subtree
        if self.right:
            elements += self.right.post_order_traversal()
        # visit the base node
        print(self.data, end="->")
        elements.append(self.data)

        return elements


def build_tree():
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(13)
    root.insert(15)
    root.insert(5)

    return root


if __name__ == "__main__":
    root = build_tree()
    root.pre_order_traversal()
    print(root.search(14))
    print(root.search(0))
    sorted_elements = root.in_order_traversal()
    print()
    post_elements = root.post_order_traversal()
    print()
    print("post ele list", post_elements)
