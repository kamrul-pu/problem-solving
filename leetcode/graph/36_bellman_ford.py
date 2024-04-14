"""
Step 1: Initialize the distance to the source vertex as 0, and the distance to all other vertices as infinity.
Step 2: Relax all edges in the graph |V| – 1 times, where |V| is the number of vertices in the graph.
For each edge (u, v) with weight w, check if the distance from the source vertex to v can be reduced
by going through u. If so, update the distance to v to the new, shorter distance.
Step 3: Check for negative weight cycles. If there is a negative weight cycle in the graph,
the algorithm will never converge and will keep reducing the distance to some vertices with each iteration.
To detect such cycles, repeat step 2 one more time. If any distance is updated in this extra iteration,
there must be a negative weight cycle in the graph.
Step 4: If there is no negative weight cycle, the shortest distance to each vertex from the source vertex has been found.
"""

from typing import List, Tuple


class Solution:
    def __bellman_ford(self, edges: List[Tuple[int]], v: int) -> List[int]:
        # Initialize distances with infinity
        distance: List[int] = [float("inf")] * v
        # Distance from source vertex to itself is 0
        distance[0] = 0

        # Relax edges repeatedly to find shortest paths
        for i in range(v - 1):
            for edge in edges:
                u, v, wt = edge
                # If the current vertex (u) is reachable (distance[u] is not infinity)
                # and if the distance to v through u is shorter than current distance to v,
                # update the distance to v
                if u != float("inf") and distance[u] + wt < distance[v]:
                    distance[v] = distance[u] + wt

        # Check for negative weight cycles
        # If we can still relax edges, it means there is a negative weight cycle
        for edge in edges:
            u, v, wt = edge
            if u != float("inf") and distance[u] + wt < distance[v]:
                return [-1]  # Return -1 to indicate negative cycle detected

        return distance

    def shortest_path(self, edges: List[Tuple[int]], v: int) -> List[int]:
        return self.__bellman_ford(edges=edges, v=v)


if __name__ == "__main__":
    # Test case
    edges: List[Tuple[int]] = [
        (3, 2, 6),
        (5, 3, 1),
        (0, 1, 5),
        (1, 5, -3),
        (1, 2, -2),
        (3, 4, -2),
        (2, 4, 3),
    ]
    v: int = 6  # Number of vertices
    solution: Solution = Solution()
    distance: List[int] = solution.shortest_path(edges=edges, v=v)
    print(distance)  # Output shortest distances from source vertex
