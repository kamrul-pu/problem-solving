"""Kth Smallest element in BST."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


def insert_node(root: Node, data: int) -> Node:
    """Iterative approach."""
    if root is None:
        return Node(data)

    cur: Node = root
    while True:
        if cur.data <= data:
            # insert in the right
            if cur.right:
                cur = cur.right
            else:
                cur.right = Node(data)
                break
        else:
            # insert in the left subtree
            if cur.left:
                cur = cur.left
            else:
                cur.left = Node(data)
                break

    return root


def find_kth_smallest_optimal(root: Node, k: int, ans: list[int]) -> int:
    if root is None:
        return
    find_kth_smallest_optimal(root.left, k, ans)
    ans[0] += 1
    if ans[0] == k:
        ans.append(root.data)
    find_kth_smallest_optimal(root.right, k, ans)


def find_kth_smallest(k: int, in_order_list) -> int:
    return in_order_list[k - 1]


def in_order(root: Node, in_order_list) -> None:
    if root is None:
        return
    in_order(root.left, in_order_list)
    in_order_list.append(root.data)
    print(root.data, end="->")
    in_order(root.right, in_order_list)


def build_tree(elements: list[int]) -> Node:
    root = Node(elements[0])
    for i in range(1, len(elements)):
        insert_node(root=root, data=elements[i])

    return root


if __name__ == "__main__":
    elements: list[int] = [5, 7, 8, 1, 2, 4, 3, 6]
    root: Node = build_tree(elements=elements)
    in_order_list: list[int] = []
    in_order(root, in_order_list)
    print()
    print(in_order_list, sep="->")
    k: int = 5
    print(find_kth_smallest(k=k, in_order_list=in_order_list))
    ans: list[int] = [0]
    find_kth_smallest_optimal(root, k, ans)
    print(ans[1])
