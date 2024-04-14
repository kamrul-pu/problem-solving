"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from typing import List
from collections import deque


class Solution:
    def __is_possible(self, n: int, prerequisities: list[list[int]]) -> bool:
        adj: list[list[int]] = [[] for _ in range(n)]
        for item in prerequisities:
            adj[item[0]].append(item[1])

        # Initialize indegree array for each vertex
        indegree: list[int] = [0] * n

        # Calculate indegree for each vertex
        for i in range(n):
            for item in adj[i]:
                indegree[item] += 1

        # Initialize a queue for BFS
        q: deque = deque()

        # Enqueue vertices with indegree 0
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        # List to store the topological ordering
        topo: list[int] = []

        # BFS
        while q:
            node = q.popleft()
            topo.append(node)

            # Update indegree for adjacent vertices
            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)

        return len(topo) == n

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.__is_possible(n=numCourses, prerequisities=prerequisites)


if __name__ == "__main__":
    numCourses: int = 2
    prerequisites: List[int] = [[1, 0], [0, 1]]
    solution: Solution = Solution()
    print(solution.canFinish(numCourses=numCourses, prerequisites=prerequisites))
