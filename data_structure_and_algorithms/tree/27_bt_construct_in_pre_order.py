"""Constract Binary tree from inorder and pre order."""

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def build_tree(
    pre_order: list[int],
    pre_start: int,
    pre_end: int,
    in_order: list[int],
    in_start: int,
    in_end: int,
    mp: defaultdict,
) -> TreeNode:
    if pre_start > pre_end or in_start > in_end:
        return None

    root: TreeNode = TreeNode(pre_order[pre_start])

    in_root = mp[root.data]
    nums_left: int = in_root - in_start

    root.left = build_tree(
        pre_order,
        pre_start + 1,
        pre_start + nums_left,
        in_order,
        in_start,
        in_root - 1,
        mp,
    )
    root.right = build_tree(
        pre_order,
        pre_start + nums_left + 1,
        pre_end,
        in_order,
        in_root + 1,
        in_end,
        mp,
    )

    return root


def build_tree_util(in_order: list[int], pre_order: list[int]) -> TreeNode:
    mp: defaultdict = defaultdict(int)

    for i in range(len(in_order)):
        mp[in_order[i]] = i

    root: TreeNode = build_tree(
        pre_order, 0, len(pre_order) - 1, in_order, 0, len(in_order) - 1, mp
    )

    return root


if __name__ == "__main__":
    in_order: list[int] = [9, 3, 15, 20, 7]
    pre_order: list[int] = [3, 9, 20, 15, 7]

    root: TreeNode = build_tree_util(in_order=in_order, pre_order=pre_order)
