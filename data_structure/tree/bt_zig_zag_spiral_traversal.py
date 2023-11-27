"""Zig Zag / Spiral Traversal."""

from collections import deque


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def zig_zag_traversal(self) -> list[list[int]]:
        ans: list[list[int]] = []
        if self is None:
            return ans
        # intialize an empty array
        q = deque()
        q.append(self)
        flag: bool = True
        while q:
            size: int = len(q)
            cur_list: list[int] = []
            while size > 0:
                cur_node: Node = q.popleft()
                cur_list.append(cur_node.data)
                size -= 1
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

            if flag:
                # insert as it is
                ans.append(cur_list)
            else:
                # reverse the current list and append
                ans.append(cur_list[::-1])
            flag = not flag

        return ans


def build_tree():
    root = Node(-10)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    return root


if __name__ == "__main__":
    root = build_tree()
    print(root.zig_zag_traversal())
