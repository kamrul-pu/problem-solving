from typing import List, Optional


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:
    def add_node(self, root: Optional[Node], data) -> None:
        """Add a node to the binary search tree."""
        if root.data == data:
            return
        if data > root.data:
            # Add in the right subtree
            if root.right:
                self.add_node(root=root.right, data=data)
            else:
                root.right = Node(data=data)
        else:
            # Add in the left subtree
            if root.left:
                self.add_node(root=root.left, data=data)
            else:
                root.left = Node(data=data)

    def find(self, root: Optional[Node], data) -> Optional[Node]:
        """Find a node with the given data in the binary search tree."""
        if root.data == data:
            return root

        if data > root.data:
            # May be in the right subtree
            if root.right:
                return self.find(root=root.right, data=data)
            else:
                return None
        else:
            # May be in the left subtree
            if root.left:
                return self.find(root=root.left, data=data)
            else:
                return None

    def find_node(self, root: Optional[Node], data: int) -> bool:
        """Check if a node with the given data exists in the binary search tree."""
        while root and root.data != data:
            if root.data > data:
                root = root.left
            else:
                root = root.right

        if root and root.data == data:
            return True
        return False

    def inorder(self, root: Optional[Node]) -> None:
        """Perform inorder traversal of the binary search tree."""
        if root is None:
            return
        self.inorder(root=root.left)
        print(root.data, end="->")
        self.inorder(root=root.right)


if __name__ == "__main__":
    root: Node = Node(data=8)
    nodes: List[int] = [1, 3, 6, 4, 7, 14, 10, 13]
    bst: BST = BST()
    for node in nodes:
        bst.add_node(root=root, data=node)

    bst.inorder(root=root)
    print()
    node: Node = bst.find(root=root, data=8)
    # print(bst.find(root=root, data=-1))
    print(node.data)
    print(node.left.data)
    print(node.right.data)
    print(bst.find_node(root=root, data=10))
