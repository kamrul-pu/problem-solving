from typing import List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __add_node(self, root: Optional[TreeNode], val: int) -> None:
        """
        Helper method to add a node to the binary search tree (BST).

        Parameters:
            root (Optional[TreeNode]): The root of the binary search tree.
            val (int): The value of the node to be added.

        Returns:
            None
        """
        if root.val == val:
            return
        while root:
            if root.val > val:
                # Add in the left subtree
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    break
            else:
                # Add in the right subtree
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    break

    def __build(self, preorder: List[int], i: List[int], upper_bound: int) -> TreeNode:
        """
        Helper method to build a binary search tree (BST) from a preorder traversal.

        Parameters:
            preorder (List[int]): The list representing the preorder traversal of the BST.
            i (List[int]): The index of the current node in the preorder traversal.
            upper_bound (int): The upper bound value for the current subtree.

        Returns:
            TreeNode: The root node of the constructed BST.
        """
        if i[0] == len(preorder) or preorder[i[0]] > upper_bound:
            return None

        root: TreeNode = TreeNode(preorder[i[0]])
        i[0] += 1
        root.left = self.__build(preorder=preorder, i=i, upper_bound=root.val)
        root.right = self.__build(preorder=preorder, i=i, upper_bound=upper_bound)
        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """
        Constructs a binary search tree (BST) from its preorder traversal.

        Parameters:
            preorder (List[int]): The preorder traversal of the BST.

        Returns:
            Optional[TreeNode]: The root node of the constructed BST.
        """
        i: List[int] = [0]
        return self.__build(preorder=preorder, i=i, upper_bound=float("inf"))

    # def __build(
    #     self, preorder: List[int], i: int, upper_bound: int
    # ) -> Tuple[TreeNode, int]:
    #     """
    #     Helper method to build a binary search tree (BST) from a preorder traversal.

    #     Parameters:
    #         preorder (List[int]): The list representing the preorder traversal of the BST.
    #         i (int): The index of the current node in the preorder traversal.
    #         upper_bound (int): The upper bound value for the current subtree.

    #     Returns:
    #         Tuple[TreeNode, int]: A tuple containing the root node of the constructed BST and the updated index.
    #     """
    #     if i == len(preorder) or preorder[i] > upper_bound:
    #         return None, i

    #     root: TreeNode = TreeNode(preorder[i])
    #     i += 1
    #     root.left, i = self.__build(preorder=preorder, i=i, upper_bound=root.val)
    #     root.right, i = self.__build(preorder=preorder, i=i, upper_bound=upper_bound)
    #     return root, i

    # def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
    #     """
    #     Constructs a binary search tree (BST) from its preorder traversal.

    #     Parameters:
    #         preorder (List[int]): The preorder traversal of the BST.

    #     Returns:
    #         Optional[TreeNode]: The root node of the constructed BST.
    #     """
    #     return self.__build(preorder=preorder, i=0, upper_bound=float("inf"))[0]
    # ============ Without passing list to maintain index

    def __in_order(self, root: TreeNode) -> None:
        """
        Perform in-order traversal of the binary tree rooted at the given node.

        Parameters:
            root (TreeNode): The root node of the binary tree.
        """
        if root is None:
            return
        self.__in_order(root.left)
        print(root.val, end="->")
        self.__in_order(root.right)

    def print_tree(self, root: TreeNode) -> None:
        """
        Print the binary tree rooted at the given node in in-order traversal.

        Parameters:
            root (TreeNode): The root node of the binary tree.
        """
        self.__in_order(root=root)
        print("Null")


if __name__ == "__main__":
    preorder: List[int] = [8, 5, 1, 7, 10, 12]
    solution: Solution = Solution()
    root: TreeNode = solution.bstFromPreorder(preorder=preorder)
    solution.print_tree(root=root)
