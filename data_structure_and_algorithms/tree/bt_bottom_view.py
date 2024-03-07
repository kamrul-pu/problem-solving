"""Bottom View of a Binary Tree."""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def bottom_view(self) -> list[int]:
        if self is None:
            return []

        q = deque()
        q.append((self, 0))
        mp: dict = defaultdict(int)

        while q:
            data = q.popleft()
            node: TreeNode = data[0]
            line: int = data[1]
            mp[line] = node.data

            if node.left:
                q.append((node.left, line - 1))
            if node.right:
                q.append((node.right, line + 1))

        ans: list[int] = [mp[key] for key in sorted(mp.keys())]
        return ans


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.right.left = TreeNode(8)
    root.left.right.right = TreeNode(9)

    return root


if __name__ == "__main__":
    root = build_tree()
    print(root.bottom_view())
