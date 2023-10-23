"""Exercise of Binary Search Tree."""


class BinarySearchTree:
    def __init__(self, data: int | str) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data: int | str):
        if data == self.data:
            return
        if data < self.data:
            # Add in the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            # add in the right subtree.
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, val):
        if val == self.data:
            return True
        if val < self.data:
            # The value may be in the left
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            # THe value may be in the right sub tree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min_element(self):
        if self.left:
            return self.left.find_min_element()

        return self.data

    def find_max_element(self):
        if self.right:
            return self.right.find_max_element()

        return self.data

    def calculate_sum(self):
        sum = 0
        # add the left element
        if self.left:
            sum += self.left.calculate_sum()

        # add the root data
        sum += self.data

        # Add the righ tree elements
        if self.right:
            sum += self.right.calculate_sum()

        return sum

    def in_order_traversal(self):
        elements = []
        # Visit the left elements
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit the base node
        elements.append(self.data)

        # Visit the right elements
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        # Visit the root first
        elements.append(self.data)

        # visit the left subtree
        if self.left:
            elements += self.left.pre_order_traversal()

        # Visit the right sub tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_taversal(self):
        elements = []
        # Traverse the left subtree first
        if self.left:
            elements += self.left.post_order_taversal()

        # traverse the righ sub tree
        if self.right:
            elements += self.right.post_order_taversal()

        # Visit the root
        elements.append(self.data)

        return elements


def build_tree(elements: list):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20))
    print(numbers_tree.search(36))
    print(numbers_tree.find_min_element())
    print(numbers_tree.find_max_element())
    print(numbers_tree.calculate_sum())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_taversal())
