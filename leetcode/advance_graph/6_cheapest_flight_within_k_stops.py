"""
There are n cities connected by some number of flights. You are given an array flights where
flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.
"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # Create an adjacency list representation of the graph
        # Each node has a list of tuples (neighbor, weight)
        graph: List[List[Tuple[int]]] = [[] for _ in range(n)]
        for edge in flights:
            graph[edge[0]].append((edge[1], edge[2]))

        # Initialize a list to store the minimum distance from src to each node
        distance: List[int] = [float("inf")] * n

        # Initialize a deque for BFS traversal
        queue: Deque[Tuple[int]] = deque()
        distance[src] = 0
        queue.append((0, src, 0))  # (stops, node, distance)

        # Perform BFS traversal to find the shortest path
        while queue:
            stops, node, dist = queue.popleft()
            # If the number of stops exceeds k, continue to the next iteration
            if stops > k:
                continue
            # Iterate through neighbors of the current node
            for neighbor, weight in graph[node]:
                # Calculate the total cost to reach the neighbor node
                total_cost: int = dist + weight
                # Update the distance if the new cost is smaller
                if total_cost < distance[neighbor]:
                    distance[neighbor] = total_cost
                    # Add the neighbor to the queue with increased number of stops
                    queue.append((stops + 1, neighbor, total_cost))

        # If the distance to the destination is still infinity, return -1
        return -1 if distance[dst] == float("inf") else distance[dst]


if __name__ == "__main__":
    n: int = 4
    flights: List[List[int]] = [
        [0, 1, 100],
        [1, 2, 100],
        [2, 0, 100],
        [1, 3, 600],
        [2, 3, 200],
    ]
    src: int = 0
    dst: int = 3
    k: int = 1
    solution: Solution = Solution()
    print(solution.findCheapestPrice(n=n, flights=flights, src=src, dst=dst, k=k))
