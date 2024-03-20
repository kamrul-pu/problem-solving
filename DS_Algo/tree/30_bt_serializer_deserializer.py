"""Serialize and Deserialize Binary Tree."""

from collections import deque

from typing import Deque, List


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def serialize(root: TreeNode) -> List[int]:
    if root is None:
        return ""
    result = []
    q: Deque = deque()
    q.append(root)
    while q:
        node: TreeNode = q.popleft()
        if node == "#":
            result.append("#")
        else:
            result.append(node.data)
            if node.left:
                q.append(node.left)
            else:
                q.append("#")
            if node.right:
                q.append(node.right)
            else:
                q.append("#")

    return result


def de_serialize(serialized: List[int]) -> TreeNode:
    if len(serialized) == 0:
        return None
    root = TreeNode(serialized[0])
    q: Deque = deque()
    q.append(root)
    i: int = 1
    while q:
        cur_node: TreeNode = q.popleft()

        if serialized[i] == "#":
            cur_node.left = None
        else:
            data = TreeNode(serialized[i])
            cur_node.left = data
            q.append(data)
        i += 1

        if serialized[i] == "#":
            cur_node.right = None
        else:
            data = TreeNode(serialized[i])
            cur_node.right = data
            q.append(data)

        i += 1

    return root


def build_tree() -> TreeNode:
    root: TreeNode = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    return root


if __name__ == "__main__":
    root: TreeNode = build_tree()
    serialized = serialize(root=root)
    print(serialized)
    root1 = de_serialize(serialized)
    serialized = serialize(root1)
    print(serialized)
