"""
Prim's Algorithm for MST -> Minimum Spanning Tree.
Step 1: Determine the arbitrary starting vertex.
Step 2: Keep repeating steps 3 and 4 until the fringe vertices (vertices not included in MST)remain. 
Step 3: Select an edge connecting the tree vertex and fringe vertex having the minimum weight.
Step 4: Add the chosen edge to MST if it doesn’t form any closed cycle.
Step 5: Exit
"""

import heapq
from typing import List, Tuple


class Solution:

    def __mst_sum(self, adj_list: List[List[Tuple[int]]]) -> int:
        """
        Calculates the sum of the minimum spanning tree (MST) using Prim's algorithm.

        Args:
            adj_list (List[List[Tuple[int]]]): Adjacency list representation of the graph.

        Returns:
            int: Sum of the weights of the edges in the MST.
        """
        n: int = len(adj_list)  # Number of vertices
        visited: List[bool] = [False] * n  # Mark visited vertices
        mst_sum: int = 0  # Initialize MST sum
        pq: List[Tuple[int]] = []  # Priority queue to store edges
        heapq.heappush(pq, (0, 0, -1))  # Push starting vertex with weight 0
        while pq:
            weight, node, parent = heapq.heappop(pq)  # Pop edge with minimum weight
            if visited[node]:  # Skip if already visited
                continue
            visited[node] = True  # Mark as visited
            if parent != -1:  # Exclude the starting vertex
                mst_sum += weight  # Add edge weight to MST sum
            for neighbor in adj_list[node]:  # Explore neighbors
                n_node, edge_weight = neighbor
                if not visited[n_node]:  # Add unvisited neighbors to the priority queue
                    heapq.heappush(pq, (edge_weight, n_node, node))

        return mst_sum

    def __prims_algo(self, adj_list: List[List[Tuple[int]]]) -> List[Tuple[int]]:
        """
        Finds the minimum spanning tree (MST) using Prim's algorithm.

        Args:
            adj_list (List[List[Tuple[int]]]): Adjacency list representation of the graph.

        Returns:
            List[Tuple[int]]: List of edges in the MST.
        """
        n: int = len(adj_list)  # Number of vertices
        visited: List[bool] = [False] * n  # Mark visited vertices
        mst: List[Tuple[int]] = []  # Initialize MST
        pq: List[Tuple[int]] = []  # Priority queue to store edges
        heapq.heappush(pq, (0, 0, -1))  # Push starting vertex with weight 0
        while pq:
            weight, node, parent = heapq.heappop(pq)  # Pop edge with minimum weight
            if visited[node]:  # Skip if already visited
                continue
            visited[node] = True  # Mark as visited
            if parent != -1:  # Exclude the starting vertex
                mst.append((parent, node))  # Add edge to MST
            for neighbor in adj_list[node]:  # Explore neighbors
                n_node, edge_weight = neighbor
                if not visited[n_node]:  # Add unvisited neighbors to the priority queue
                    heapq.heappush(pq, (edge_weight, n_node, node))

        return mst

    def mst(self, adj_list: List[List[Tuple[int]]]) -> List[Tuple[int]]:
        """
        Finds the minimum spanning tree (MST) of the given graph.

        Args:
            adj_list (List[List[Tuple[int]]]): Adjacency list representation of the graph.

        Returns:
            List[Tuple[int]]: List of edges in the MST.
        """
        mst_sum = self.__mst_sum(adj_list=adj_list)  # Calculate MST sum
        print(mst_sum)  # Print MST sum
        return self.__prims_algo(adj_list=adj_list)  # Return MST


if __name__ == "__main__":
    # Test case
    adj_list: List[List[Tuple[int]]] = [
        [(1, 2), (2, 1)],
        [(0, 2), (2, 1)],
        [(0, 1), (1, 1), (3, 2), (4, 2)],
        [(2, 2), (4, 1)],
        [(2, 2), (3, 1)],
    ]
    solution: Solution = Solution()
    mst: List[Tuple[int]] = solution.mst(adj_list=adj_list)
    print(mst)
