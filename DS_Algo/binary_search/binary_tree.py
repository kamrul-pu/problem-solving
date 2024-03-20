"""
Binary Tree / Binary Search Tree BST.
Each Node has atmost 2 nodes.
"""


class BinarySearchTree:
    def __init__(self, data: int) -> None:
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

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            # Value might be in left subtree.
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            # Valuse might be in right subtree.
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        # Visit the left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # Visit the base node.
        elements.append(self.data)

        # Visit the right Tree.
        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())

    print(numbers_tree.search(55))

    # Binary Search in String
    countries = [
        "India",
        "Pakistan",
        "Germany",
        "USA",
        "China",
        "India",
        "Bangladesh",
        "UK",
        "USA",
    ]
    countries_tree = build_tree(countries)
    print(countries_tree.in_order_traversal())
    print("UK is in the list?", countries_tree.search("UK"))
    print("Sweden is in the list?", countries_tree.search("Sweden"))
