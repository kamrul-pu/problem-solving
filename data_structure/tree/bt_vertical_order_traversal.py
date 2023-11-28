"""Binary Tree Vertical Order Traversal."""

from collections import deque


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def vertical_order_trversal(self, root):
        ans: list[list[int]] = [0] * 5
        # declare a nodes
        nodes = dict()
        # Return null if the tree is empty
        if root is None:
            return ans
        # Initialize queue
        todo = deque()
        todo.append((root, 0, 0))

        # iterate the queue until it's empty
        while todo:
            # check the length of queue
            curr_node = todo.popleft()
            node = curr_node[0]
            x: int = curr_node[1]
            y: int = curr_node[2]
            key = (x, y)
            if key in nodes:
                nodes[key].append(node.data)
            else:
                nodes[key] = [node.data]

            if node.left:
                todo.append((node.left, x - 1, y + 1))
            if node.right:
                todo.append((node.right, x + 1, y + 1))

        print("nodes", nodes)

        for k, v in nodes.items():
            print("k", k[0] + 2, "val", v)
            if ans[k[0] + 2] == 0:
                ans[k[0] + 2] = v
            else:
                new_ls: list[int] = ans[k[0] + 2]
                new_ls += v
                ans[k[0] + 2] = new_ls
        print(ans)


def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.right = TreeNode(10)
    root.left.left = TreeNode(4)
    root.left.left.right = TreeNode(5)
    root.left.left.right.right = TreeNode(6)

    root.right.right = TreeNode(10)
    root.right.left = TreeNode(9)

    return root


if __name__ == "__main__":
    root = build_tree()
    root.vertical_order_trversal(root)
