"""
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional
roads between some intersections.The inputs are generated such that you can reach any intersection
from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that
there is a road between intersections ui and vi that takes timei minutes to travel. You want to know
in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time.
Since the answer may be large, return it modulo 109 + 7.
"""

import heapq
from typing import List, Tuple

# Define a constant for modulo operation
MOD: int = 1000000007


class Solution:
    def __f(self, n: int, g: List[List[Tuple[int]]]) -> int:
        # Initialize an array to store the number of ways to reach each intersection
        ways: List[int] = [0] * n
        # There is one way to reach the starting intersection (0)
        ways[0] = 1

        # Initialize an array to store the shortest distance to each intersection
        distance: List[int] = [float("inf")] * n
        distance[0] = 0

        # Priority queue to store intersections by their shortest distance from the start
        pq: List[Tuple[int]] = []
        heapq.heappush(pq, (0, 0))  # Push the starting intersection (0) with distance 0

        # Perform Dijkstra's algorithm
        while pq:
            dist, node = heapq.heappop(
                pq
            )  # Pop the intersection with the shortest distance so far
            for neighbor in g[node]:  # Explore neighbors of the current intersection
                n_node, edge_w = neighbor
                new_dist: int = edge_w + dist  # Calculate new distance to neighbor
                if (
                    new_dist < distance[n_node]
                ):  # If new distance is shorter than recorded
                    distance[n_node] = new_dist  # Update shortest distance to neighbor
                    heapq.heappush(
                        pq, (new_dist, n_node)
                    )  # Push neighbor to priority queue
                    ways[n_node] = ways[
                        node
                    ]  # Update the number of ways to reach neighbor
                elif (
                    new_dist == distance[n_node]
                ):  # If new distance is equal to recorded
                    ways[n_node] += ways[
                        node
                    ]  # Add the number of ways to reach neighbor

        # Return the number of ways to reach the destination (last intersection) modulo MOD
        return ways[n - 1] % MOD
        # return ways[n - 1] % (pow(10, 9) + 7)

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Create adjacency list representation of the graph
        g: List[List[int]] = [[] for _ in range(n)]
        for edge in roads:
            g[edge[0]].append((edge[1], edge[2]))  # Add neighbor and edge weight
            g[edge[1]].append(
                (edge[0], edge[2])
            )  # Undirected graph, add edge in both directions
        # Call the private function to compute the number of ways
        return self.__f(n=n, g=g)


if __name__ == "__main__":
    n: int = 7
    roads: List[List[int]] = [
        [0, 6, 7],
        [0, 1, 2],
        [1, 2, 3],
        [1, 3, 3],
        [6, 3, 3],
        [3, 5, 1],
        [6, 5, 1],
        [2, 5, 1],
        [0, 4, 5],
        [4, 6, 2],
    ]
    solution: Solution = Solution()
    print(solution.countPaths(n=n, roads=roads))
