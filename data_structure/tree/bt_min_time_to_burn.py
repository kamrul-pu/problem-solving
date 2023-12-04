"""Minumum time taken to burn a BT from a node/leef node."""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def mark_parents(root: TreeNode, parent_track: defaultdict) -> None:
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


def time_to_burn(root: TreeNode, target: TreeNode) -> int:
    time: int = 0
    if target is None:
        return time
    q = deque()
    visited: defaultdict = defaultdict(bool)
    visited[target.data] = True
    q.append(target)
    while q:
        cur_size = len(q)
        while cur_size > 0:
            burned: bool = False
            curr_node: TreeNode = q.popleft()
            if curr_node.left and not visited[curr_node.left.data]:
                q.append(curr_node.left)
                visited[curr_node.left.data] = True
                burned = True
            if curr_node.right and not visited[curr_node.right.data]:
                q.append(curr_node.right)
                visited[curr_node.right.data] = True
                burned = True

            if (
                curr_node.data in parent_track
                and not visited[parent_track[curr_node.data].data]
            ):
                visited[parent_track[curr_node.data].data] = True
                burned = True

            if burned:
                time += 1

            cur_size -= 1

    return time


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.right = TreeNode(7)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    return root


if __name__ == "__main__":
    root = build_tree()
    parent_track: defaultdict = defaultdict()
    mark_parents(root, parent_track)
    # print(parent_track)
    print(time_to_burn(root=root, target=root.left))
