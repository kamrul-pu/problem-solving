"""Tree Data structure in Python."""

from typing import List


class TreeNode:
    def __init__(self, data) -> None:
        """
        Initialize a TreeNode with data and an empty list of children.
        """
        self.data: int = data
        self.children: List[int] = []
        self.parent = None

    def add_child(self, child) -> None:
        """
        Add a child TreeNode to the current TreeNode.
        """
        child.parent = self
        self.children.append(child)

    def __get_level(self) -> int:
        """
        Get the level of the TreeNode in the tree.
        """
        level: int = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self) -> None:
        """
        Print the tree structure starting from the current TreeNode.
        """
        spaces = " " * self.__get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    """
    Build a sample product tree and return the root node.
    """
    root = TreeNode("Electronic")
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Xiomi"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Philips"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
