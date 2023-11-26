"""Maximum path sum in a binary tree."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def find_max(self, node, maxi: list[int]) -> int:
        if node is None:
            return 0

        left_sum: int = max(0, self.find_max(node.left, maxi))
        right_sum: int = max(0, self.find_max(node.right, maxi))

        maxi[0] = max(maxi[0], left_sum + right_sum + node.data)

        return node.data + max(left_sum, right_sum)

    def diameter_of_bt(self, maxi: list[int]) -> int:
        self.find_max(self, maxi)
        return maxi[0]


def build_tree():
    root = Node(-10)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    return root


if __name__ == "__main__":
    root = build_tree()
    # print(root.max_height(root))
    maxi: list[int] = [0]
    print(root.diameter_of_bt(maxi))
