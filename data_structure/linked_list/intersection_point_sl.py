"""Intersaction point of two single linked list."""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def print_list(self) -> None:
        cur: Node = self.head
        while cur:
            print(cur.data, end="->")
            cur = cur.next
        print("Null")


def collision_point(temp1: Node, temp2: Node, d) -> Node | None:
    while d:
        temp1 = temp1.next
        d -= 1

    while temp1 != temp2:
        temp1 = temp1.next
        temp2 = temp2.next

    return temp1


def intersection_point(head1: Node, head2: Node) -> Node | None:
    # count the number of nodes in each list
    n1: int = 0
    n2: int = 0
    temp1: Node = head1
    while temp1:
        n1 += 1
        temp1 = temp1.next

    temp2: Node = head2
    while temp2:
        n2 += 1
        temp2 = temp2.next

    print(n1, n2)
    # if n2 is larger then smaller is head1
    if n1 < n2:
        return collision_point(temp1=head2, temp2=head1, d=n2 - n1)
    # head2 is smaller
    else:
        return collision_point(temp1=head1, temp2=head2, d=n1 - n2)


def intersection_point_optimal(head1: Node, head2: Node) -> Node | None:
    if head1 is None or head2 is None:
        return None
    t1: Node = head1
    t2: Node = head2
    while t1 != t2:
        t1 = t1.next
        t2 = t2.next

        if t1 == t2:
            return t1

        if t1 is None:
            t1 = head2
        if t2 is None:
            t2 = head1

    return t1


if __name__ == "__main__":
    llist: SingleLinkedList = SingleLinkedList()
    node1: Node = Node(3)
    node2: Node = Node(1)
    node3: Node = Node(4)
    node4: Node = Node(6)
    node5: Node = Node(2)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    llist.head = node1
    llist.print_list()
    node6: Node = Node(1)
    node7: Node = Node(2)
    node8: Node = Node(4)
    node9: Node = Node(5)
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node3
    llist2: SingleLinkedList = SingleLinkedList()
    llist2.head = node6
    llist2.print_list()
    collide_node: Node = intersection_point(head1=llist.head, head2=llist2.head)
    print(collide_node)
    print(collide_node.data if collide_node else None)

    collide_node: Node = intersection_point_optimal(head1=llist.head, head2=llist2.head)
    print(collide_node)
    print(collide_node.data if collide_node else None)
