"""
There are n cities connected by some number of flights. You are given an array flights where
flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi
with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price
from src to dst with at most k stops. If there is no such route, return -1.
"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def __f(self, g: List[List[Tuple[int]]], n: int, src: int, dst: int, k: int) -> int:
        # Initialize distances to all nodes as infinity
        distances: List[int] = [float("inf")] * n
        distances[src] = 0  # Distance from source to source is 0

        # Initialize a deque for BFS
        q: Deque = deque()
        q.append((0, (src, 0)))  # Tuple: (number of stops, (node, distance))

        # Perform BFS
        while q:
            stops, node_distance = q.popleft()
            node, distance = node_distance

            # If the number of stops exceeds the limit, skip this path
            if stops > k:
                continue

            # Explore all neighbors of the current node
            for neighbor in g[node]:
                n_node, edge_wt = neighbor
                new_cost: int = distance + edge_wt

                # If the new cost to reach the neighbor is less than recorded cost, update the distance
                if new_cost < distances[n_node]:
                    distances[n_node] = new_cost
                    q.append(
                        (stops + 1, (n_node, new_cost))
                    )  # Increment stops and add neighbor to queue

        # Return the distance to the destination node
        return distances[dst]

    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # Construct graph from flights
        g: List[List[Tuple[int]]] = [[] for _ in range(n)]
        for edge in flights:
            g[edge[0]].append((edge[1], edge[2]))

        # Call the private function to compute the cheapest price
        ans: int = self.__f(g=g, n=n, src=src, dst=dst, k=k)

        # If no route found, return -1
        return -1 if ans == float("inf") else ans


if __name__ == "__main__":
    # Example inputs
    n = 4
    flights: List[List[int]] = [
        [0, 1, 100],
        [1, 2, 100],
        [2, 0, 100],
        [1, 3, 600],
        [2, 3, 200],
    ]
    src = 0
    dst = 3
    k = 1

    # Create an instance of the Solution class
    solution: Solution = Solution()

    # Print the cheapest price to reach the destination with at most k stops
    print(solution.findCheapestPrice(n=n, flights=flights, src=src, dst=dst, k=k))
