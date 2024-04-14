"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the
constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest
element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order
traversal when next() is called.
"""

from collections import deque
from typing import Deque, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        """
        Initializes an iterator over the in-order traversal of a binary search tree (BST).

        Parameters:
            root (Optional[TreeNode]): The root node of the BST.
        """
        self.q: Deque = deque()
        self.__push_all(root)

    def __push_all(self, node: Optional[TreeNode]) -> None:
        """
        Helper method to push all nodes of the binary tree rooted at the given node onto the queue.

        Parameters:
            node (Optional[TreeNode]): The root node of the binary tree.
        """
        if node is None:
            return
        self.__push_all(node=node.left)
        self.q.append(node.val)
        self.__push_all(node=node.right)

    def next(self) -> int:
        """
        Moves the pointer to the right, then returns the number at the pointer.

        Returns:
            int: The next number in the in-order traversal of the BST.
        """
        if self.q:
            return self.q.popleft()
        return None

    def hasNext(self) -> bool:
        """
        Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.

        Returns:
            bool: True if there exists a number in the traversal to the right of the pointer, otherwise False.
        """
        return len(self.q) != 0


def build_tree() -> TreeNode:
    """
    Helper method to build a sample binary tree for testing.

    Returns:
        TreeNode: The root node of the constructed binary tree.
    """
    root: TreeNode = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    return root


if __name__ == "__main__":
    # Build the binary search tree
    root: TreeNode = build_tree()

    # Create an instance of BSTIterator class
    bst_iter: BSTIterator = BSTIterator(root=root)

    # Test the iterator methods
    print(bst_iter.q)
    print(bst_iter.next())
    print(bst_iter.next())
    print(bst_iter.hasNext())
    print(bst_iter.next())
    print(bst_iter.hasNext())
    print(bst_iter.next())
    print(bst_iter.hasNext())
    print(bst_iter.next())
    print(bst_iter.hasNext())
    print(bst_iter.next())
    print(bst_iter.hasNext())
    print(bst_iter.next())
