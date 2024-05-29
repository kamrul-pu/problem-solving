"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel
times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node,
and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to
receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
"""

import heapq
from collections import defaultdict
from typing import DefaultDict, List, Tuple


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Create an adjacency list to represent the graph
        adj_list: DefaultDict[int, List[Tuple[int]]] = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((v, t))

        # Step 2: Initialize a distance list to store the minimum time to reach each node
        distance: List[int] = [float("inf")] * (n + 1)

        # Step 3: Initialize a priority queue (min heap) to process nodes in order of minimum distance
        q: List[Tuple[int]] = []
        heapq.heappush(q, (0, k))  # Push the starting node with distance 0
        distance[k] = 0  # Set the distance to the starting node as 0

        # Step 4: Perform Dijkstra's algorithm to find the minimum distance to all nodes
        while q:
            # Pop the node with the minimum distance from the priority queue
            time, node = heapq.heappop(q)

            # Check each neighbor of the current node
            for neighbor, neighbor_t in adj_list[node]:
                # Calculate the distance to the neighbor via the current node
                dist: int = time + neighbor_t
                # If the calculated distance is smaller than the stored distance to the neighbor,
                # update the distance and push the neighbor to the priority queue
                if distance[neighbor] > dist:
                    distance[neighbor] = dist
                    heapq.heappush(q, (dist, neighbor))

        # Step 5: Check if all nodes are reachable and return the maximum distance
        max_distance = max(distance[1:])  # Ignore the 0th index
        return max_distance if max_distance < float("inf") else -1


if __name__ == "__main__":
    times: List[List[int]] = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n: int = 4
    k: int = 2
    solution: Solution = Solution()
    print(solution.networkDelayTime(times=times, n=n, k=k))
