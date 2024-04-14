"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where
connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other
computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected
computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected.
If it is not possible, return -1.
"""

from typing import List


class DSU:
    def __init__(self, node: int) -> None:
        # Initialize DSU with parent array and size array
        self.parent: List[int] = [i for i in range(node + 1)]  # Initialize parent array
        self.__size: List[int] = [1] * (node + 1)  # Initialize size array

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


class Solution:
    def __f(self, n: int, connections: List[List[int]]) -> int:
        # Helper function to calculate the minimum number of extra edges required
        ds: DSU = DSU(node=n)
        extra_edge: int = 0
        for connection in connections:
            u, v = connection
            # If both nodes are already connected, increment extra_edge count
            if ds.find_parent(node=u) == ds.find_parent(node=v):
                extra_edge += 1
            else:
                ds.union(u=u, v=v)  # Union the two nodes
        cnt: int = 0
        for node in range(n):
            if ds.parent[node] == node:
                cnt += 1
        ans: int = cnt - 1  # Number of connected components - 1
        if extra_edge >= ans:
            return ans
        return -1

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # Main function to check if it's possible to connect all computers
        # If number of connections is less than n - 1, it's not possible
        if len(connections) < n - 1:
            return -1
        return self.__f(n=n, connections=connections)


if __name__ == "__main__":
    n: int = 6
    connections: List[List[int]] = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
    solution: Solution = Solution()
    print(solution.makeConnected(n=n, connections=connections))
