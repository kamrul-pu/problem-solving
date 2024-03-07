"""Most stones removed with same row or column."""

from collections import defaultdict
from typing import DefaultDict, List


class DSU:
    def __init__(self, n: int) -> None:
        # Initialize the data structure with size and parent pointers.
        self.size: List[int] = [1] * (n)
        self.parent: List[int] = [0] * (n)
        for i in range(n):
            self.parent[i] = i

    def find_parent(self, node: int) -> int:
        # Find the parent of the node using path compression.
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u: int, v: int) -> None:
        # Union two nodes by size, ensuring the smaller tree is attached to the larger one.
        u_parent: int = self.find_parent(node=u)
        v_parent: int = self.find_parent(node=v)

        if u_parent == v_parent:
            return

        if self.size[u_parent] < self.size[v_parent]:
            self.parent[u_parent] = v_parent
            self.size[v_parent] += self.size[u_parent]
        elif self.size[u_parent] > self.size[v_parent]:
            self.parent[v_parent] = u_parent
            self.size[u_parent] += self.size[v_parent]
        else:
            self.parent[u_parent] = v_parent
            self.size[v_parent] += self.size[u_parent]


# TODO: the solution has some problem need to fix it


def max_remove(stones: List[tuple[int]], n: int) -> int:
    max_row: int = 0
    max_col: int = 0
    for item in stones:
        max_row = max(max_row, item[0])
        max_col = max(max_col, item[1])

    ds: DSU = DSU(n=max_row + max_col + 2)
    stone_nodes: DefaultDict = defaultdict(int)
    for item in stones:
        node_row: int = item[0]
        node_col: int = item[1] + max_row + 1
        ds.union_by_size(u=node_row, v=node_col)
        stone_nodes[node_row] = 1
        stone_nodes[node_col] = 1

    cnt: int = 0
    for key, val in stone_nodes.items():
        if ds.find_parent(node=key) == key:
            cnt += 1
    return n - cnt


if __name__ == "__main__":
    n: int = 6
    stones: List[tuple[int]] = [(0, 0), (0, 1), (1, 0), (1, 2), (2, 1), (2, 2)]
    # grid: List[List[int]] = [
    #     [1, 0, 1, 0],
    #     [0, 0, 0, 1],
    #     [0, 1, 1, 0],
    #     [0, 0, 0, 1],
    # ]
    print(max_remove(stones=stones, n=n))
