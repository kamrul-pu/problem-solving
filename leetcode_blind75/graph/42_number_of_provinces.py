"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are
directly connected, and isConnected[i][j] = 0 otherwise.
"""

from typing import List


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


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n: int = len(isConnected)
        ds: DSU = DSU(n=n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    ds.union_by_size(u=i, v=j)

        cnt: int = 0
        for i in range(n):
            if ds.parent[i] == i:
                cnt += 1

        return cnt


if __name__ == "__main__":
    is_connected: List[List[int]] = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    solution: Solution = Solution()
    print(solution.findCircleNum(isConnected=is_connected))
