"""Disjoint Set Data Structure (Union-Find) with Path Compression and Union by Size."""


class DSU:
    def __init__(self, n: int) -> None:
        # Initialize the data structure with size and parent pointers.
        self.size: list[int] = [1] * (n + 1)
        self.parent: list[int] = [0] * (n + 1)
        for i in range(1, n + 1):
            self.parent[i] = i

    def find_parent(self, node: int) -> int:
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u: int, v: int) -> None:
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
        # Display the current state of the DSU (for debugging purposes).
        print("Size:", self.size[1:])
        print("Parent:", self.parent[1:])


if __name__ == "__main__":
    # Example usage of the DSU data structure.
    dsu: DSU = DSU(n=7)
    dsu.display()

    paths: list[tuple[int]] = [(1, 2), (2, 3), (4, 5), (6, 7), (5, 6)]

    for path in paths:
        # Union by rank operation for each path.
        dsu.union_by_size(u=path[0], v=path[1])
        dsu.display()

    if dsu.find_parent(3) == dsu.find_parent(7):
        print("Nodes 3 and 7 are in the same component.")
    else:
        print("Nodes 3 and 7 are not in the same component.")

    dsu.union_by_size(3, 7)
    if dsu.find_parent(3) == dsu.find_parent(7):
        print("After merging, nodes 3 and 7 are in the same component.")
    else:
        print("After merging, nodes 3 and 7 are not in the same component.")

    for i in range(7):
        print(dsu.find_parent(i + 1))
        dsu.display()
