"""Number of Islands 2 using DSU."""

from typing import List


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


def num_of_island(n: int, m: int, operators: List[List[int]]) -> List[int]:
    ds: DSU = DSU(n=n * m)
    visited: List[List[bool]] = [[False for col in range(m)] for row in range(n)]
    ans: List[int] = []
    cnt: int = 0
    dr: tuple[int] = (-1, 0, 1, 0)
    dc: tuple[int] = (0, 1, 0, -1)

    for item in operators:
        row, col = item
        if visited[row][col]:
            # If the cell is already visited, append the current count to the result.
            ans.append(cnt)
            continue
        visited[row][col] = True
        cnt += 1

        for ind in range(4):
            adj_row: int = row + dr[ind]
            adj_col: int = col + dc[ind]

            if is_valid(row=adj_row, col=adj_col, n=n, m=m):
                if visited[adj_row][adj_col] == 1:
                    # If the adjacent cell is visited, union the current cell and the adjacent cell.
                    node: int = row * m + col
                    adj_node: int = adj_row * m + adj_col
                    if ds.find_parent(node=node) != ds.find_parent(node=adj_node):
                        ds.union_by_size(u=node, v=adj_node)
                        cnt -= 1

        ans.append(cnt)

    return ans


if __name__ == "__main__":
    operators: List[List[int]] = [
        [0, 0],
        [0, 0],
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 3],
        [1, 3],
        [0, 4],
        [3, 2],
        [2, 2],
        [1, 2],
        [0, 2],
    ]
    n: int = 4
    m: int = 5
    ans: List[int] = num_of_island(n=n, m=m, operators=operators)
    print(ans)
