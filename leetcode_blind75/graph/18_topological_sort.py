"""
Topological sort in python.
Graph Must be DAG -> Directed Acyclic Graph.
"""

from typing import List


class Solution:
    def __dfs(
        self, node: int, g: List[List[int]], visited: List[int], st: List[int]
    ) -> None:
        # Mark the current node as visited
        visited[node] = 1

        # Traverse through all neighbors of the current node
        for neighbor in g[node]:
            # If the neighbor is not visited, recursively visit it
            if not visited[neighbor]:
                self.__dfs(node=neighbor, g=g, visited=visited, st=st)

        # Append the current node to the stack after all its neighbors have been visited
        st.append(node)

    def topological_sort(self, g: List[List[int]]) -> List[int]:
        # Number of vertices in the graph
        v: int = len(g)

        # List to track visited nodes
        visited: List[bool] = [False] * v

        # Stack to store the topological order
        st: List[int] = []

        # Perform DFS on each unvisited node to construct the topological order
        for node in range(v):
            if not visited[node]:
                self.__dfs(node=node, g=g, visited=visited, st=st)

        # Reverse the stack to obtain the topological order
        # st.reverse()
        low: int = 0
        high: int = len(st) - 1
        while low < high:
            st[low], st[high] = st[high], st[low]
            low += 1
            high -= 1

        return st


if __name__ == "__main__":
    # Example graph represented as an adjacency list
    g: List[List[int]] = [[], [], [3], [1], [0, 1], [0, 2]]

    # Create an instance of the Solution class
    solution: Solution = Solution()

    # Perform topological sort on the graph
    topo: List[int] = solution.topological_sort(g=g)

    # Print the topological order
    print(topo)
