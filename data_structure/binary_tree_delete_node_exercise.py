class BinarySearchTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # Binary search tree doesn't allow duplicated value
        if data == self.data:
            return
        if data < self.data:
            # add the data in left subtree.
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            # Add the data in right subtree.
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def find_max(self):
        if self.right is None:
            return self.data

        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data

        return self.left.find_min()

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # may be in the left tree
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            # May be in the right tree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []

        # Visit the left node
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit the base node
        elements.append(self.data)

        # Visit the right node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
            # Return None if not found by default
            # can write else:
            # return None
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            # find min value from right side and delte
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)
            # Option 2 find max value from left side and delete
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self


def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers = [87, 5, 100, 4, 90, 100, 20]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(87))
    print(numbers_tree.search(3))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    numbers_tree.delete(20)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(90)
    print(numbers_tree.in_order_traversal())
