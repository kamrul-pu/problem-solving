"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from collections import deque
from typing import Deque, List


class Solution:
    def __f(self, n: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines whether it is possible to finish all courses given the prerequisites.

        Args:
        - n (int): The total number of courses.
        - prerequisites (List[List[int]]): The list of prerequisites, where each inner list contains two integers [ai, bi].

        Returns:
        - bool: True if it is possible to finish all courses, False otherwise.
        """
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
        return len(topo) == n

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines whether it is possible to finish all courses given the prerequisites.

        Args:
        - numCourses (int): The total number of courses.
        - prerequisites (List[List[int]]): The list of prerequisites, where each inner list contains two integers [ai, bi].

        Returns:
        - bool: True if it is possible to finish all courses, False otherwise.
        """
        return self.__f(n=numCourses, prerequisites=prerequisites)


if __name__ == "__main__":
    numCourses: int = 2
    prerequisites: List[List[int]] = [[1, 0], [0, 1]]
    solution: Solution = Solution()
    print(solution.canFinish(numCourses=numCourses, prerequisites=prerequisites))
