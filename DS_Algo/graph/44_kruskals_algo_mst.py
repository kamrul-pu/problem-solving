"""Kruskal's Algorithm - for Minimum Spanning Tree."""

from typing import List, Tuple


class DSU:
    def __init__(self, n: int) -> None:
        # Initialize the data structure with size and parent pointers.
        self.size: List[int] = [1] * n
        self.parent: List[int] = [0] * n
        for i in range(n):
            self.parent[i] = i

    def find_parent(self, node: int) -> int:
        """Find the parent of a node with path compression."""
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u: int, v: int) -> None:
        """Union by size to optimize the disjoint-set union operation."""
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

    def display(self) -> None:
        """Display the current state of the DSU (for debugging purposes)."""
        print("Size:", self.size)
        print("Parent:", self.parent)


def spanning_tree(v: int, adj_list: List[List[int]]) -> int:
    """Find the Minimum Spanning Tree using Kruskal's Algorithm."""
    edges: List[tuple[int]] = []
    for i in range(v):
        for item in adj_list[i]:
            adj_node: int = item[0]
            weight: int = item[1]
            node: int = i
            edges.append((weight, node, adj_node))

    ds: DSU = DSU(n=v)

    edges.sort()
    mst_weight: int = 0
    mst: List[tuple[int]] = []
    for edge in edges:
        wt, u, v = edge
        if ds.find_parent(node=u) != ds.find_parent(v):
            mst_weight += wt
            mst.append((u, v))
            ds.union_by_size(u=u, v=v)
            print("wt", wt)

    print(mst)
    return mst_weight


if __name__ == "__main__":
    # Example usage
    adj_list: List[List[Tuple[int]]] = [
        [(1, 2), (3, 1), (4, 4)],
        [(0, 2), (2, 3), (3, 3), (5, 7)],
        [(1, 3), (3, 5), (5, 8)],
        [(0, 1), (1, 3), (2, 5), (4, 9)],
        [(0, 4), (3, 9)],
        [(1, 7), (2, 8)],
    ]

    mst: int = spanning_tree(v=6, adj_list=adj_list)
    print(mst)
