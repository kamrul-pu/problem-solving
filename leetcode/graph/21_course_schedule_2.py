"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers,
return any of them. If it is impossible to finish all courses, return an empty array.
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
    numCourses: int = 4
    prerequisites: List[List[int]] = [[1, 0], [2, 0], [3, 1], [3, 2]]
    solution: Solution = Solution()
    print(solution.findOrder(numCourses=numCourses, prerequisites=prerequisites))
