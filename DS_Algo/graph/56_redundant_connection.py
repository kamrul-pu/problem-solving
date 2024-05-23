"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
he added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there
is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.
"""

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Number of nodes
        n: int = len(edges)
        # Initialize parent array with each node as its own parent
        parent: List[int] = [i for i in range(n + 1)]
        # Initialize rank array to keep track of the depth of each node's subtree
        rank: List[int] = [1] * (n + 1)

        # Find function to find the parent of a node
        def find(n: int):
            # If the parent of the node is not itself, keep searching until the parent is found
            p: int = parent[n]
            while p != parent[p]:
                # Path compression: Set the parent of the current node to its grandparent
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        # Union function to merge two nodes into the same set
        def union(n1: int, n2: int):
            # Find the parent of each node
            p1: int = find(n1)
            p2: int = find(n2)
            # If they have the same parent, they are already in the same set, so return False
            if p1 == p2:
                return False
            # Merge the smaller rank tree into the larger rank tree
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        # Iterate through the edges
        for n1, n2 in edges:
            # If merging the nodes fails (i.e., they are already in the same set), return the edge
            if not union(n1, n2):
                return [n1, n2]


if __name__ == "__main__":
    # Example input
    edges: List[List[int]] = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    solution: Solution = Solution()
    # Find and print the redundant connection
    print(solution.findRedundantConnection(edges=edges))
