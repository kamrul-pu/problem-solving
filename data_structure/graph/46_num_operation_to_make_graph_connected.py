"""Number of operation required to connect a graph network."""
"""Number of Provinces, graph using Disjoint Set."""


class DSU:
    def __init__(self, n: int) -> None:
        # Initialize the Disjoint Set data structure with size and parent pointers.
        self.size: list[int] = [1] * n
        self.parent: list[int] = [0] * n
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


def number_of_operation(adj_list: list[list[int]], n: int) -> list[int]:
    """Count the number of provinces using Disjoint Set."""
    ds: DSU = DSU(n=n)

    extra_edge: int = 0
    # Union by size for connected nodes in the matrix.
    for edge in adj_list:
        u, v = edge
        if ds.find_parent(u) == ds.find_parent(v):
            extra_edge += 1
        else:
            ds.union_by_size(u, v)
    cnt: int = 0
    # Collect unique parent nodes representing provinces.
    for i in range(n):
        # provinces.add(ds.parent[i])
        if ds.parent[i] == i:
            cnt += 1

    ans: int = cnt - 1
    if extra_edge >= ans:
        return ans
    return -1


if __name__ == "__main__":
    # Example usage
    n: int = 4
    adj_list: int = [[0, 1], [0, 2], [1, 2]]
    operation: set = number_of_operation(adj_list=adj_list, n=n)
    print(operation)
