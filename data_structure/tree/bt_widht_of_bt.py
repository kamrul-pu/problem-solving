"""Widht of a Binary Tree."""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"Node: {self.data} left: {self.left} right: {self.right}"


def width_of_bt(root: TreeNode) -> int:
    if root is None:
        return 0
    ans: int = 0
    q = deque()
    q.append((root, 0))
    while q:
        cur_size: int = len(q)
        mmin: int = q[0][1]
        first: int = 0
        last: int = 0
        for i in range(cur_size):
            front = q.popleft()
            cur_id: int = front[1] - mmin
            node: TreeNode = front[0]
            if i == 0:
                first = cur_id
            if i == cur_size - 1:
                last = cur_id
            if node.left:
                q.append((node.left, cur_id * 2 + 1))
            if node.right:
                q.append((node.right, cur_id * 2 + 2))
        ans = max(ans, last - first + 1)

    return ans


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(8)
    root.right.right = TreeNode(4)

    return root


if __name__ == "__main__":
    root = build_tree()
    print(width_of_bt(root=root))
