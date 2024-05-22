"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from collections import defaultdict
from typing import DefaultDict, List, Set


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a defaultdict to store prerequisites as a mapping of course to its prerequisites
        pre_map: DefaultDict[int, List] = defaultdict(list)
        for course, pre in prerequisites:
            pre_map[course].append(pre)

        # Set to keep track of visited courses during DFS traversal
        visit: Set[int] = set()

        # Define a recursive DFS function to check if it's possible to complete all courses
        def dfs(course: int) -> bool:
            # If the course is already visited, it indicates a cycle, so return False
            if course in visit:
                return False
            # If there are no prerequisites for the course, return True
            if pre_map[course] == []:
                return True
            # Mark the current course as visited
            visit.add(course)
            # Traverse through each prerequisite of the current course
            for pre in pre_map[course]:
                # Recursively check if it's possible to complete the prerequisite
                if not dfs(pre):
                    return False
            # Remove the current course from visited set to backtrack
            visit.remove(course)
            # Once all prerequisites are visited and processed, remove them from the pre_map
            pre_map[course] = []
            # Return True indicating completion of the current course
            return True

        # Iterate through each course and check if it's possible to complete it
        for course in range(numCourses):
            # If the course is not visited and it's not possible to complete it, return False
            if course not in visit and not dfs(course):
                return False

        # If all courses are visited and it's possible to complete them, return True
        return True


if __name__ == "__main__":
    numCourses: int = 5
    prerequisites: List[List[int]] = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
    solution: Solution = Solution()
    print(solution.canFinish(numCourses=numCourses, prerequisites=prerequisites))
