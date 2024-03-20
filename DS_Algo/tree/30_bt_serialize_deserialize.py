"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can
be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
"""

from collections import deque
from typing import Deque, List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        """
        Initialize a tree node with the given value and optional left and right children.

        Parameters:
            x: The value of the node.
        """
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.

        Parameters:
            root (TreeNode): The root of the binary tree.

        Returns:
            str: The serialized string representation of the binary tree.
        """
        if root is None:
            return ""
        result: List[str] = []
        q: Deque = deque()
        q.append(root)
        while q:
            node: TreeNode = q.popleft()
            if node is None:
                result.append("#")
            else:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(result)

    def deserialize(self, data) -> TreeNode:
        """
        Decodes your encoded data to tree.

        Parameters:
            data (str): The serialized string representation of the binary tree.

        Returns:
            TreeNode: The root of the deserialized binary tree.
        """
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if nodes[i] != "#":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1
            if nodes[i] != "#":
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1
        return root


def build_tree() -> TreeNode:
    """
    Helper function to build a sample binary tree for testing.

    Returns:
        TreeNode: The root of the constructed binary tree.
    """
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    return root


if __name__ == "__main__":
    # Build the binary tree
    root: TreeNode = build_tree()
    # Create an instance of the Codec class
    ser: Codec = Codec()
    deser: Codec = Codec()
    # Deserialize the serialized tree and print the result
    ans = deser.deserialize(ser.serialize(root=root))
    print(ans)
