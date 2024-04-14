"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.
"""

from typing import List, Set, Tuple


class DSU:
    def __init__(self, node: int) -> None:
        # Initialize DSU with parent array and size array
        self.parent: List[int] = [i for i in range(node)]  # Initialize parent array
        self.__size: List[int] = [1] * (node)  # Initialize size array

    def find_parent(self, node: int) -> int:
        # Find the parent of the set containing 'node' (with path compression)
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_parent(node=self.parent[node])  # Path Compression
        return self.parent[node]

    def union(self, u: int, v: int) -> None:
        # Union operation to merge two sets
        u_parent: int = self.find_parent(node=u)
        v_parent: int = self.find_parent(node=v)
        if u_parent == v_parent:
            return None
        if self.__size[u_parent] < self.__size[v_parent]:
            self.parent[u_parent] = v_parent
            self.__size[v_parent] += self.__size[u_parent]
        elif self.__size[u_parent] > self.__size[v_parent]:
            self.parent[v_parent] = u_parent
            self.__size[u_parent] += self.__size[v_parent]
        else:
            self.parent[u_parent] = v_parent
            self.__size[v_parent] += self.__size[u_parent]

    def get_size(self, node: int) -> int:
        return self.__size[node]


class Solution:
    def __is_valid(self, row: int, col: int, n: int, m: int) -> bool:
        # Check if a given cell is within the grid boundaries
        return n > row >= 0 and m > col >= 0

    def __f(self, grid: List[List[int]], n: int, m: int) -> int:
        # Internal function to find the largest island size
        ds: DSU = DSU(node=n * m)
        dr: Tuple[int] = (-1, 0, 1, 0)
        dc: Tuple[int] = (0, 1, 0, -1)

        # Connect adjacent 1s horizontally and vertically
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    continue
                node: int = row * m + col
                for ind in range(4):
                    adj_row: int = row + dr[ind]
                    adj_col: int = col + dc[ind]
                    if (
                        self.__is_valid(adj_row, adj_col, n, m)
                        and grid[adj_row][adj_col] == 1
                    ):
                        adj_node: int = adj_row * m + adj_col
                        ds.union(u=node, v=adj_node)

        # Find the size of the largest island after changing one 0 to 1
        mx: int = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    continue
                node: int = row * m + col
                components: Set = set()
                for ind in range(4):
                    adj_row: int = row + dr[ind]
                    adj_col: int = col + dc[ind]
                    if (
                        self.__is_valid(adj_row, adj_col, n, m)
                        and grid[adj_row][adj_col] == 1
                    ):
                        adj_node: int = adj_row * m + adj_col
                        components.add(ds.find_parent(node=adj_node))
                size: int = 0
                for item in components:
                    size += ds.get_size(node=item)
                mx = max(mx, size + 1)

        # Find the maximum island size
        for cell in range(n * m):
            mx = max(mx, ds.get_size(node=ds.find_parent(cell)))

        return mx

    def largestIsland(self, grid: List[List[int]]) -> int:
        n: int = len(grid)
        m: int = len(grid[0])
        return self.__f(grid=grid, n=n, m=m)


if __name__ == "__main__":
    grid: List[List[int]] = [
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 1],
    ]
    solution: Solution = Solution()
    ans: int = solution.largestIsland(grid=grid)
    print(ans)
