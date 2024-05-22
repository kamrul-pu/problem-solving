"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1]
is the same as [1, 0] and thus will not appear together in edges.
"""

from typing import Dict, List, Set


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If there are no nodes, it's considered a valid tree
        if not n:
            return True

        # Initialize an adjacency list to represent the graph
        adj: Dict[int, List] = {i: [] for i in range(n)}

        # Populate the adjacency list with the given edges
        # Since the graph is undirected, we add edges in both directions
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Initialize a set to keep track of visited nodes during DFS
        visit: Set[int] = set()

        # Define a depth-first search (DFS) function to traverse the graph
        # node: current node being visited
        # parent: parent of the current node in the DFS traversal
        def dfs(node: int, parent: int) -> bool:
            # If the current node has already been visited, there's a cycle
            if node in visit:
                return False

            # Mark the current node as visited
            visit.add(node)

            # Traverse neighbors of the current node
            for neighbor in adj[node]:
                # Skip the parent node to avoid revisiting it (prevents cycling)
                if neighbor == parent:
                    continue
                # Recursively call DFS for each unvisited neighbor
                if not dfs(node=neighbor, parent=node):
                    return False

            # If DFS traversal completes without detecting a cycle, return True
            return True

        # Start DFS traversal from the first node (0) with an arbitrary parent (-1)
        loop: bool = dfs(0, -1)

        # Check if all nodes were visited and there's no disconnected component
        # If there's not a loop (cycle) and all nodes are visited, it's a valid tree
        return loop and len(visit) == n


if __name__ == "__main__":
    # Test inputs
    n: int = 5
    edges: List[List[int]] = [[0, 1], [0, 2], [0, 3], [1, 4]]
    # Create an instance of the Solution class
    solution: Solution = Solution()
    # Call the validTree function and print the result
    print(solution.validTree(n=n, edges=edges))
