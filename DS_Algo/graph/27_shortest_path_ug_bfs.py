# Importing the necessary module
from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def shortestPath(
        self, edges: List[List[int]], n: int, m: int, src: int
    ) -> List[int]:
        """
        Finds the shortest path from the source node to all other nodes in an undirected graph
        using Breadth-First Search (BFS).

        :param edges: List of edges in the graph, where each edge is represented as [u, v] indicating
                      an undirected edge between nodes u and v.
        :param n: Number of nodes in the graph.
        :param m: Number of edges in the graph.
        :param src: The source node from which to calculate shortest paths.
        :return: A list of shortest distances from the source node to all other nodes.
                 If a node is unreachable, its distance is -1.
        """
        # Create an adjacency list to represent the graph
        g: List[List[int]] = [[] for _ in range(n)]

        # Populate the adjacency list with the given edges
        for edge in edges:
            u, v = edge
            g[u].append(v)  # Add an edge from u to v
            g[v].append(u)  # Add an edge from v to u (since the graph is undirected)

        # Initialize the distance array with infinity, and set the distance to the source node to 0
        dist: List[int] = [float("inf")] * n
        dist[src] = 0

        # Use a queue for BFS, starting with the source node
        q: Deque[Tuple[int, int]] = deque()
        q.append((src, 0))  # (node, distance_from_src)

        # Perform BFS to find the shortest path
        while q:
            node, ds = q.popleft()  # Dequeue the front node and its distance
            for neighbor in g[node]:  # Iterate over all neighbors of the current node
                n_d = ds + 1  # Compute the new distance for the neighbor
                if n_d < dist[neighbor]:  # If the new distance is shorter, update it
                    dist[neighbor] = n_d
                    q.append(
                        (neighbor, n_d)
                    )  # Enqueue the neighbor with its new distance

        # Replace distances that are still infinity with -1 to indicate unreachable nodes
        for i in range(n):
            if dist[i] == float("inf"):
                dist[i] = -1

        return dist


# Main block to test the function
if __name__ == "__main__":
    n: int = 9  # Number of nodes in the graph
    m: int = 10  # Number of edges in the graph
    edges: List[List[int]] = [
        [0, 1],  # Edge between node 0 and 1
        [0, 3],  # Edge between node 0 and 3
        [3, 4],  # Edge between node 3 and 4
        [4, 5],  # Edge between node 4 and 5
        [5, 6],  # Edge between node 5 and 6
        [1, 2],  # Edge between node 1 and 2
        [2, 6],  # Edge between node 2 and 6
        [6, 7],  # Edge between node 6 and 7
        [7, 8],  # Edge between node 7 and 8
        [6, 8],  # Edge between node 6 and 8
    ]
    src: int = 0  # Source node from which shortest paths are to be calculated

    # Create an instance of the Solution class
    solution: Solution = Solution()
    # Find the shortest path from the source node (0)
    ans: List[int] = solution.shortestPath(edges, n, m, src)
    # Print the result which shows the shortest distance from source node to all other nodes
    print(ans)
