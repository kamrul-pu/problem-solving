"""
Detect cycle using topological sort and Kahn's Algorithm.
"""

from collections import deque
from typing import Deque, List


class Solution:
    def __f(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        # Initialize an adjacency list to represent the graph
        adj_list: List[List[int]] = [[] for _ in range(n)]

        # Populate the adjacency list based on the prerequisites
        for edge in prerequisites:
            adj_list[edge[0]].append(edge[1])

        # Initialize an array to store the in-degree of each course
        indegree: List[int] = [0] * n

        # Calculate the in-degree of each course
        for node in range(n):
            for neighbor in adj_list[node]:
                indegree[neighbor] += 1

        # Initialize a deque for topological sorting
        q: Deque = deque()

        # Enqueue courses with in-degree zero
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)

        # Initialize a list to store the topological ordering
        topo: List[int] = []

        # Perform BFS-based topological sorting
        while q:
            node: int = q.popleft()
            topo.append(node)
            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # If the length of the topological ordering is equal to the number of courses, return True
        return topo[::-1] if len(topo) == n else []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return self.__f(n=numCourses, prerequisites=prerequisites)


if __name__ == "__main__":
    # Example usage:
    g: List[List[int]] = [[1, 0], [2, 1], [3, 2]]
    n: int = 4
    solution: Solution = Solution()
    print(solution.findOrder(n, g))
