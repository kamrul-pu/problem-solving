"""
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary.
Find the order of characters in the alien language.
Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1
if the order of string returned by the function is correct else 0 denoting incorrect string returned.
"""

from collections import deque
from typing import Deque, List


class Solution:

    def __topo_sort(self, g: List[List[int]], v: int) -> List[int]:
        """
        Perform topological sorting on a Directed Acyclic Graph (DAG) using BFS Kahn's Algorithm.

        :param g: Adjacency List representing the directed acyclic graph.
        :param v: Number of vertices in the graph.
        :return: List representing the topological ordering of nodes.
        """
        # Initialize indegree array for all vertices
        indegree: List[int] = [0] * v

        # Calculate indegrees for each vertex
        for i in range(v):
            for item in g[i]:
                indegree[item] += 1

        # Initialize a queue for BFS
        q: Deque = deque()

        # Add vertices with indegree 0 to the queue
        for i in range(v):
            if indegree[i] == 0:
                q.append(i)

        topo: List[int] = []

        # Perform BFS
        while q:
            node = q.popleft()
            topo.append(node)  # Add node to the topological ordering

            # Decrease indegree of adjacent vertices
            for it in g[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)  # If indegree becomes 0, add vertex to the queue

        return topo

    def findOrder(self, alien_dict: List[str], N: int, K: int) -> str:
        # Create adjacency list for the alien dictionary graph
        g: List[int] = [[] for _ in range(K)]
        for i in range(N - 1):
            s1: str = alien_dict[i]
            s2: str = alien_dict[i + 1]
            le: int = min(len(s1), len(s2))
            # Compare adjacent words and create edges based on the first differing character
            for j in range(le):
                if s1[j] != s2[j]:
                    g[ord(s1[j]) - ord("a")].append(ord(s2[j]) - ord("a"))
                    break

        # Perform topological sorting
        topo: List[int] = self.__topo_sort(g=g, v=K)

        # Convert the topological ordering to string
        ans: str = ""
        for item in topo:
            ans += chr(item + ord("a"))

        return ans


if __name__ == "__main__":
    N: int = 5
    K: int = 4
    alien_dict: List[str] = ["baa", "abcd", "abca", "cab", "cad"]
    solution: Solution = Solution()
    print(solution.findOrder(alien_dict=alien_dict, N=N, K=K))
