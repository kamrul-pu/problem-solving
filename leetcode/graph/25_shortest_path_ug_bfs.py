"""
Shortest path in undirected graph using bfs.
NB: edge weight 1 unit.
"""

from collections import deque
from typing import Deque, List


class Solution:
    def shortest_path(self, graph: List[List[int]], src: int) -> List[int]:
        # Get the number of nodes in the graph
        n: int = len(graph)

        # Initialize the distance array with infinity for all nodes
        distance: List[int] = [float("inf")] * n

        # Initialize a queue for BFS traversal
        q: Deque = deque()

        # Add the source node to the queue and mark its distance as 0
        q.append(src)
        distance[src] = 0

        # Perform BFS traversal
        while q:
            # Dequeue a node from the queue
            node: int = q.popleft()

            # Traverse through the neighbors of the dequeued node
            for neighbor in graph[node]:
                # Calculate the new distance to the neighbor
                new_distance: int = distance[node] + 1

                # If the new distance is shorter than the current distance recorded for the neighbor
                if new_distance < distance[neighbor]:
                    # Update the distance of the neighbor
                    distance[neighbor] = new_distance

                    # Enqueue the neighbor for further traversal
                    q.append(neighbor)

        return distance


if __name__ == "__main__":
    # Example graph represented as an adjacency List
    graph: List[List[int]] = [
        [1, 3],
        [0, 2, 3],
        [1, 6],
        [0, 4],
        [3, 5],
        [4, 6],
        [2, 5, 7, 8],
        [6, 8],
        [6, 7],
    ]

    solution: Solution = Solution()
    print(solution.shortest_path(graph=graph, src=0))
