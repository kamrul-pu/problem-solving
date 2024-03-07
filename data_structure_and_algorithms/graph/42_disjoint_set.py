"""Disjoint Set Data Structure (Union-Find) with Path Compression and Union by Rank."""

from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        # Initialize the data structure with ranks and parent pointers.
        self.rank: List[int] = [0] * (n + 1)
        self.parent: List[int] = [0] * (n + 1)

        for i in range(n + 1):
            self.parent[i] = i

    def find_parent(self, node: int) -> int:
        # Find the representative (parent) of a set with path compression.
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u: int, v: int) -> None:
        # Perform union by rank to optimize the merging of sets.
        u_parent: int = self.find_parent(u)
        v_parent: int = self.find_parent(v)

        if u_parent == v_parent:
            return None

        if self.rank[u_parent] < self.rank[v_parent]:
            self.parent[u_parent] = v_parent
        elif self.rank[u_parent] > self.rank[v_parent]:
            self.parent[v_parent] = u_parent
        else:
            self.parent[u_parent] = v_parent
            self.rank[u_parent] += 1

    def display(self) -> None:
        # Display the current state of the DSU (for debugging purposes).
        print("Rank:", self.rank[1:])
        print("Parent:", self.parent[1:])


if __name__ == "__main__":
    # Example usage of the DSU data structure.
    dsu: DSU = DSU(n=7)
    dsu.display()

    paths: List[tuple[int]] = [(1, 2), (2, 3), (4, 5), (6, 7), (5, 6)]

    for path in paths:
        # Union by rank operation for each path.
        dsu.union_by_rank(u=path[0], v=path[1])
        dsu.display()

    if dsu.find_parent(3) == dsu.find_parent(7):
        print("Nodes 3 and 7 are in the same component.")
    else:
        print("Nodes 3 and 7 are not in the same component.")

    dsu.union_by_rank(3, 7)
    if dsu.find_parent(3) == dsu.find_parent(7):
        print("After merging, nodes 3 and 7 are in the same component.")
    else:
        print("After merging, nodes 3 and 7 are not in the same component.")
