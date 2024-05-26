"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|,
where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
"""

import heapq
from collections import defaultdict
from typing import DefaultDict, List, Set, Tuple


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Number of points
        n: int = len(points)

        # Create an adjacency list to store distances between points
        adj_list: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

        # Calculate distances and populate the adjacency list
        for i in range(n):
            x1, y1 = points[i]
            for j in range(
                i + 1, n
            ):  # Avoid recalculating distances for already calculated pairs
                x2, y2 = points[j]
                # Manhattan distance between two points
                dist = abs(x1 - x2) + abs(y1 - y2)
                # Add the distance and the index of the other point to the adjacency list
                adj_list[i].append((dist, j))
                adj_list[j].append((dist, i))

        # Initialize variables
        res: int = 0  # Total cost
        visit: Set[int] = set()  # Set to track visited nodes
        min_heap: List[Tuple[int]] = []  # Min heap to store edges by cost

        # Start with the first point (index 0)
        heapq.heappush(min_heap, (0, 0))

        # Prim's algorithm to find minimum spanning tree
        while len(visit) < n:  # Loop until all points are visited
            cost, node = heapq.heappop(min_heap)  # Pop the edge with the minimum cost
            if node in visit:  # Skip if the node has already been visited
                continue
            res += cost  # Add the cost to the total cost
            visit.add(node)  # Mark the node as visited
            # Explore neighbors of the current node
            for neighbor_cost, neighbor in adj_list[node]:
                if (
                    neighbor not in visit
                ):  # Add neighbors to the heap if they are not visited
                    heapq.heappush(min_heap, (neighbor_cost, neighbor))

        return res  # Return the total cost


if __name__ == "__main__":
    # Example usage
    points: List[List[int]] = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    solution: Solution = Solution()
    print(solution.minCostConnectPoints(points=points))
