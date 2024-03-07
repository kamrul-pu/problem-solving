"""Constract Binary tree from inorder and post order."""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def build_tree(
    in_order: list[int],
    in_start: int,
    in_end: int,
    post_order: list[int],
    p_start: int,
    p_end: int,
    mp: defaultdict,
) -> TreeNode:
    if p_start > p_end or in_start > in_end:
        return None

    root: TreeNode = TreeNode(post_order[p_end])

    in_root = mp[post_order[p_end]]
    nums_left: int = in_root - in_start

    root.left = build_tree(
        in_order,
        in_start,
        in_root - 1,
        post_order,
        p_start,
        p_start + nums_left - 1,
        mp,
    )
    root.right = build_tree(
        in_order,
        in_root + 1,
        in_end,
        post_order,
        p_start + nums_left,
        p_end - 1,
        mp,
    )

    return root


def build_tree_util(in_order: list[int], post_order: list[int]) -> TreeNode:
    if len(in_order) != len(post_order):
        return None
    mp: defaultdict = defaultdict(int)

    for i in range(len(in_order)):
        mp[in_order[i]] = i

    root: TreeNode = build_tree(
        in_order, 0, len(in_order) - 1, post_order, 0, len(post_order) - 1, mp
    )

    return root


if __name__ == "__main__":
    in_order: list[int] = [40, 20, 50, 10, 60, 30]
    post_order: list[int] = [40, 50, 20, 60, 30, 10]

    root: TreeNode = build_tree_util(in_order=in_order, post_order=post_order)
