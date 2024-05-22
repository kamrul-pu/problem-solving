"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers,
return any of them. If it is impossible to finish all courses, return an empty array.
"""

from collections import defaultdict
from typing import DefaultDict, List, Set


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a defaultdict to store prerequisites as a mapping of course to its prerequisites
        pre_map: DefaultDict[int, List] = defaultdict(list)
        for course, pre in prerequisites:
            pre_map[course].append(pre)

        ans: List[int] = []

        # Set to keep track of visited courses during DFS traversal
        visit: Set[int] = set()
        cycle: Set[int] = set()

        # Define a recursive DFS function to check if it's possible to complete all courses
        def dfs(course: int) -> bool:
            # If the course is already visited, it indicates a cycle, so return False
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            # Traverse through each prerequisite of the current course
            for pre in pre_map[course]:
                # Recursively check if it's possible to complete the prerequisite
                if not dfs(pre):
                    return False
            # Remove the current course from cycle set to backtrack
            cycle.remove(course)
            # Mark the current course as visited
            visit.add(course)
            ans.append(course)

            # Return True indicating completion of the current course
            return True

        # Iterate through each course and check if it's possible to complete it
        for course in range(numCourses):
            # If the course is not visited and it's not possible to complete it, return False
            if not dfs(course):
                return []

        # If all courses are visited and it's possible to complete them, return answer in order
        return ans


if __name__ == "__main__":
    numCourses: int = 4
    prerequisites: List[List[int]] = [[1, 0], [2, 0], [3, 1], [3, 2]]
    solution: Solution = Solution()
    print(solution.findOrder(numCourses=numCourses, prerequisites=prerequisites))
