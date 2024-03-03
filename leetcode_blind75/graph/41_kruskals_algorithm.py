"""
Kruskal's Algorithm - for Minimum Spanning Tree.
1. Sort all the edges from low weight to high
2. Take the edge with the lowest weight and add it to the spanning tree.
3. If adding the edge created a cycle, then reject this edge.
Keep adding edges until we reach all vertices.
"""

from typing import List, Tuple


class DSU:
    def __init__(self, n: int = 10) -> None:
        # Initialize arrays to keep track of parent, rank, and size of each set.
        self.__rank: List[int] = [0] * (n + 1)  # Initialize rank array
        self.__size: List[int] = [1] * (n + 1)  # Initialize size array
        self.__parent: List[int] = [i for i in range(n + 1)]  # Initialize parent array

    def make(self, node: int) -> None:
        # Make a new set with a single element 'node'
        self.__parent[node] = node
        self.__size[node] += 1

    def find(self, node: int) -> int:
        # Find the root of the set to which 'node' belongs (with path compression)
        if self.__parent[node] == node:
            return node
        self.__parent[node] = self.find(node=self.__parent[node])  # Path Compression
        return self.__parent[node]

    def union(self, u: int, v: int) -> None:
        # Find the parents of the sets containing 'u' and 'v'
        u_parent: int = self.find(node=u)
        v_parent: int = self.find(node=v)

        # If 'u' and 'v' belong to the same set, no need to union further
        if u_parent == v_parent:
            return None

        # Union by rank: Merge the smaller rank tree into the larger rank tree
        if self.__rank[u_parent] < self.__rank[v_parent]:
            self.__parent[u_parent] = v_parent
            self.__size[v_parent] += self.__size[u_parent]
        elif self.__rank[u_parent] > self.__rank[v_parent]:
            self.__parent[v_parent] = u_parent
            self.__size[u_parent] += self.__size[v_parent]
        else:
            # If ranks are equal, choose one as parent and increment its rank
            self.__parent[v_parent] = u_parent
            self.__size[u_parent] += self.__size[v_parent]
            self.__rank[u_parent] += 1

    def info(self) -> None:
        # Print information about parent, size, and rank arrays
        print("parent =", self.__parent[1:])
        print("size =", self.__size[1:])
        print("rank =", self.__rank[1:])


class Solution:
    def minimum_spanning_tree(
        self, v: int, adj_list: List[List[Tuple[int]]]
    ) -> List[Tuple[int]]:
        # Prepare a list of edges sorted by weight
        edges: List[Tuple[int]] = []
        for node in range(v):
            for neighbor in adj_list[node]:
                adj_node: int = neighbor[0]
                weight: int = neighbor[1]
                edges.append((weight, node, adj_node))
        edges.sort()  # Sort the edges by weight

        # Initialize empty list to store edges of the Minimum Spanning Tree (MST)
        mst: List[Tuple[int]] = []

        # Initialize Disjoint Set Union (DSU) data structure
        ds: DSU = DSU(n=v)

        # Iterate through the sorted edges
        for edge in edges:
            wt, u, v = edge
            # If the edge doesn't create a cycle, add it to the MST
            if ds.find(node=u) != ds.find(node=v):
                mst.append((u, v))
                ds.union(u=u, v=v)

        return mst

    def mst(self, v: int, adj_list: List[List[Tuple[int]]]) -> int:
        # Similar to `minimum_spanning_tree`, but instead of returning MST edges,
        # this function returns the total weight of the MST.
        edges: List[Tuple[int]] = []
        for node in range(v):
            for neighbor in adj_list[node]:
                adj_node: int = neighbor[0]
                weight: int = neighbor[1]
                edges.append((weight, node, adj_node))

        mst_weight: int = 0
        ds: DSU = DSU(n=v)
        for edge in edges:
            wt, u, v = edge
            # If the edge doesn't create a cycle, add its weight to the total MST weight
            if ds.find(node=u) != ds.find(node=v):
                mst_weight += wt
                ds.union(u=u, v=v)

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
    v: int = len(adj_list)
    solution: Solution = Solution()
    mst: List[Tuple[int]] = solution.minimum_spanning_tree(v=v, adj_list=adj_list)
    print(mst)  # Output MST edges
    mst_weight: int = solution.mst(v=v, adj_list=adj_list)
    print(mst_weight)  # Output total weight of the MST
