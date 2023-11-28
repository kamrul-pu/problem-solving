"""Top View of a Binary Tree."""

from collections import deque


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def top_view(self) -> list[int]:
        if self is None:
            return ans

        # line and node
        mp = {}
        queue = deque()
        queue.append([self, 0])
        # mp[0] = self.data

        while queue:
            cur_data = queue.popleft()
            node: TreeNode = cur_data[0]
            line: int = cur_data[1]
            if line not in mp:
                mp[line] = node.data

            if node.left:
                queue.append([node.left, line - 1])
            if node.right:
                queue.append([node.right, line + 1])

        ans: list[int] = [0] * len(mp.keys())
        for k, v in mp.items():
            ans[k + 2] = v
        return ans


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(7)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)

    return root


if __name__ == "__main__":
    root = build_tree()
    print(root.top_view())
