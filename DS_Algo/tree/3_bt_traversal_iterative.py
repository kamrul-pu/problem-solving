"""Binary Tree Pre order Traversal."""

from typing import List


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == data:
            return  # duplicate not allowed
        if data < self.data:
            # add in the left subtree
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            # add in the right subtree
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def search(self, val) -> bool:
        if self.data == val:
            return True

        if val < self.data:
            # may be in the left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            # may be in the right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def pre_order_traversal(self) -> None:
        # root left right
        if self == None:
            return
        stack: List[Node] = []
        stack.append(self)

        while stack:
            node = stack.pop()
            print(node.data, end="->")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        print()

    def in_order_traversal(self) -> None:
        # left root right
        if self is None:
            return

        current: Node = self
        stack: List[Node] = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.data, end="->")
                current = current.right
            else:
                break

        print()

    def post_order_traversal(self) -> None:
        # left right root
        if self is None:
            return

        stack1: List[Node] = []
        stack2: List[Node] = []
        stack1.append(self)
        while stack1:
            curr_node: Node = stack1.pop()
            stack2.append(curr_node)

            if curr_node.left:
                stack1.append(curr_node.left)
            if curr_node.right:
                stack1.append(curr_node.right)

        while stack2:
            curr_node: Node = stack2.pop()
            print(curr_node.data, end="->")

        print()

    def post_order_traversal_single_stack(self) -> None:
        # left right root
        if self is None:
            return

        curr: Node = self
        stack: List[Node] = []
        while curr or stack:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                temp: Node = stack[-1].right
                if temp is None:
                    temp = stack.pop()
                    print(temp.data, end="->")  # store the data if required

                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        print(temp.data, end="->")  # store the data if required
                else:
                    curr = temp
        print()


def build_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.left.right.left = Node(6)
    root.left.right.right = Node(7)

    return root


if __name__ == "__main__":
    root = build_tree()
    root.pre_order_traversal()
    root.in_order_traversal()
    root.post_order_traversal()
    root.post_order_traversal_single_stack()
