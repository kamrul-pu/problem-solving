"""Print all nodes at a distance of k from given node."""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def mark_parents(root: TreeNode, parent_track: defaultdict, target: TreeNode) -> None:
    q = deque()
    q.append(root)
    while q:
        current: TreeNode = q.popleft()
        if current.left:
            parent_track[current.left.data] = current
            q.append(current.left)
        if current.right:
            parent_track[current.right.data] = current
            q.append(current.right)


def distance_k(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    parent_track: defaultdict = defaultdict()
    mark_parents(root, parent_track, target)

    visited: defaultdict = defaultdict(bool)
    q = deque()
    q.append(target)
    visited[target.data] = True
    curr_level: int = 0
    while q:
        size: int = len(q)
        if curr_level == k:
            break
        curr_level += 1

        for i in range(size):
            current: TreeNode = q.popleft()
            if current.left and not visited[current.left.data]:
                q.append(current.left)
                visited[current.left.data] = True
            if current.right and not visited[current.right.data]:
                q.append(current.right)
                visited[current.right.data] = True

            if (
                current.data in parent_track
                and not visited[parent_track[current.data].data]
            ):  # Fix here
                q.append(parent_track[current.data])
                visited[parent_track[current.data].data] = True  # Fix here

    result: list[int] = []
    while q:
        curr: TreeNode = q.popleft()
        result.append(curr.data)

    return result


def build_tree():
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    return root


if __name__ == "__main__":
    root = build_tree()
    result: list[int] = distance_k(root, root.left, 2)
    print(result)
