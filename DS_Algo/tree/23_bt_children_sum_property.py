"""
Children sum property of a Binary Tree.
Node.val = Left.val + right.val
"""

from typing import Optional


class TreeNode:
    def __init__(self, data) -> None:
        """
        Initialize a tree node with the given data.

        Parameters:
            data: The data value for the node.
        """
        self.data = data
        self.left = None
        self.right = None


def changeTree(node: Optional[TreeNode]) -> bool:
    """
    Recursively updates the tree nodes to satisfy the children sum property.

    The children sum property states that the value of a node is equal to the sum
    of the values of its left and right children. If the value of a node is less
    than the sum of its children, it is updated to match the sum.

    Parameters:
        node (Optional[TreeNode]): The root of the subtree to be processed.

    Returns:
        None
    """
    if node is None:
        return

    # Calculate the sum of values of left and right children
    child_sum = 0
    if node.left:
        child_sum += node.left.data
    if node.right:
        child_sum += node.right.data

    # Update the node value to satisfy the children sum property
    if child_sum >= node.data:
        node.data = child_sum
    else:
        # If the sum of children is less than the node value,
        # update the children values to match the node value
        if node.left:
            node.left.data = node.data
        if node.right:
            node.right.data = node.data

    # Recursively update children nodes
    changeTree(node=node.left)
    changeTree(node=node.right)

    # Calculate the total sum of children values
    total_sum = 0
    if node.left:
        total_sum += node.left.data
    if node.right:
        total_sum += node.right.data

    # If the node has children, update its value with the total sum
    if node.left or node.right:
        node.data = total_sum


def pre_order(node: Optional[TreeNode]) -> None:
    """
    Perform a pre-order traversal of the binary tree and print node values.

    Parameters:
        node (Optional[TreeNode]): The root of the subtree to be traversed.

    Returns:
        None
    """
    if node is None:
        return
    print(node.data, end="->")
    pre_order(node=node.left)
    pre_order(node=node.right)


def build_tree() -> TreeNode:
    """
    Helper function to build a sample binary tree for testing.

    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    root: TreeNode = TreeNode(2)
    root.left = TreeNode(35)
    root.right = TreeNode(10)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(2)

    return root


if __name__ == "__main__":
    # Build the binary tree
    root: TreeNode = build_tree()

    # Print the original tree values in pre-order traversal
    print("Original Tree:")
    pre_order(node=root)
    print()

    # Update the tree nodes to satisfy the children sum property
    changeTree(node=root)

    # Print the updated tree values in pre-order traversal
    print("Tree after applying children sum property:")
    pre_order(node=root)
    print()
