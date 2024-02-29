"""
Step 1: Initialize the shortest paths between any 2 vertices with Infinity.

Step 2: Find all pair shortest paths that use 0 intermediate vertices, then find the shortest paths
that use 1 intermediate vertex and so on.. until using all N vertices as intermediate nodes.

Step 3: Minimize the shortest paths between any 2 pairs in the previous operation.

Step 4: For any 2 vertices (i,j) , one should actually minimize the distances between this pair
using the first K nodes, so the shortest path will be: min(dist[i][k]+dist[k][j],dist[i][j]).

"""

from typing import List, Tuple

INF: int = float("inf")


class Solution:
    def __floyd_warshal(self, matrix: List[List[int]], v: int) -> None:
        # Floyd-Warshall algorithm for finding shortest paths
        # Iterate through all vertices as intermediate points
        for k in range(v):
            # Iterate through all pairs of vertices (i, j)
            for i in range(v):
                for j in range(v):
                    # Update the shortest path from vertex i to vertex j passing through vertex k
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    def shortest_path(self, edges: List[Tuple[int]], v: int) -> List[List[int]]:
        # Initialize adjacency matrix with INF for all pairs of vertices
        matrix: List[List[int]] = [
            [0 if col == row else INF for col in range(v)] for row in range(v)
        ]
        # Populate adjacency matrix with edge weights
        for edge in edges:
            matrix[edge[0]][edge[1]] = edge[2]

        # Call the Floyd-Warshall algorithm to compute shortest paths
        self.__floyd_warshal(matrix=matrix, v=v)
        return matrix


if __name__ == "__main__":
    # Test case
    edges: List[Tuple[int]] = [
        (0, 2, -3),
        (1, 0, 5),
        (1, 2, 4),
        (2, 3, 3),
        (3, 1, -2),
    ]
    v: int = 4  # Number of vertices
    solution: Solution = Solution()
    distance: List[List[int]] = solution.shortest_path(edges=edges, v=v)
    print(distance, sep="\n")  # Output shortest paths between all pairs of vertices
