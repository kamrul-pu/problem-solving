"""Number of Provinces, graph using Disjoint Set."""

from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        # Initialize the Disjoint Set data structure with size and parent pointers.
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


def number_of_provinces(matrix: List[List[int]]) -> List[int]:
    """Count the number of provinces using Disjoint Set."""
    n: int = len(matrix)
    ds: DSU = DSU(n=n)

    # Union by size for connected nodes in the matrix.
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                ds.union_by_size(i, j)

    provinces: List[int] = []
    p_cnt: int = 0

    # Collect unique parent nodes representing provinces.
    for i in range(n):
        # provinces.add(ds.parent[i])
        if ds.parent[i] == i:
            provinces.append(i)
            p_cnt += 1

    return provinces


if __name__ == "__main__":
    # Example usage
    matrix: List[List[int]] = [
        [0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0],
    ]
    provinces: set = number_of_provinces(matrix=matrix)
    print(provinces)
    print(len(provinces))
