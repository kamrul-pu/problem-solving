"""Disjoint Set Data Structure (Union-Find) with Path Compression and Union by Rank."""

from typing import List


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


if __name__ == "__main__":
    dsu: DSU = DSU(n=5)
    dsu.info()
    # dsu.make(node=4)
    print(dsu.find(node=4))
    dsu.union(u=1, v=2)
    dsu.info()
    dsu.union(u=3, v=4)
    dsu.info()
    dsu.union(u=1, v=3)
    dsu.info()
    dsu.union(u=4, v=5)
    print(dsu.find(node=4))
    dsu.info()
