"""Making Larger Island DSU."""

from typing import List, Tuple, Set


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


def is_valid(row: int, col: int, n: int, m: int) -> bool:
    # Check if the given row and column indices are within valid bounds.
    return row >= 0 and row < n and col >= 0 and col < m


def max_connection(n: int, m: int, grid: List[List[int]]) -> int:
    ds: DSU = DSU(n=n * m)
    dr: Tuple[int] = (-1, 0, 1, 0)
    dc: Tuple[int] = (0, 1, 0, -1)
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 0:
                continue
            for ind in range(4):
                adj_row: int = row + dr[ind]
                adj_col: int = col + dc[ind]
                if (
                    is_valid(row=adj_row, col=adj_col, n=n, m=m)
                    and grid[adj_row][adj_col] == 1
                ):
                    node: int = row * m + col
                    adj_node: int = adj_row * m + adj_col
                    ds.union_by_size(u=node, v=adj_node)
    mx: int = 0
    for row in range(n):
        for col in range(m):
            if grid[row][col] == 1:
                continue
            components: Set = set()
            for ind in range(4):
                adj_row: int = row + dr[ind]
                adj_col: int = col + dc[ind]

                if is_valid(row=adj_row, col=adj_col, n=n, m=m):
                    if grid[adj_row][adj_col] == 1:
                        components.add(ds.find_parent(node=adj_row * m + adj_col))
            size: int = 0
            for item in components:
                size += ds.size[item]
            mx = max(mx, size + 1)

    for cell in range(n * m):
        mx = max(mx, ds.size[ds.find_parent(cell)])

    return mx


if __name__ == "__main__":
    grid: List[List[int]] = [
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 1],
    ]
    n: int = 6
    m: int = 5
    ans: int = max_connection(n=n, m=m, grid=grid)
    print(ans)
