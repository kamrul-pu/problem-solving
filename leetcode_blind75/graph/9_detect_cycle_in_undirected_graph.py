"""Detect cycle in an undirected graph using dfs and bfs."""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def __detect_dfs(
        self, node: int, parent: int, graph: List[List[int]], visited: List[int]
    ) -> bool:
        # Mark the current node as visited
        visited[node] = True
        # Iterate through the neighbors of the current nodes
        for neighbor in graph[node]:
            # If the neighbor has not been visited, recursively check if there is a cycle
            if not visited[neighbor]:
                return self.__detect_dfs(
                    node=neighbor, parent=node, graph=graph, visited=visited
                )
            # If the neighbor has been visited and it's not the parent node (back edge), then a cycle is detected
            elif neighbor != parent:
                return True
        # If no cycle is detected, return False
        return False

    def __detect_bfs(
        self, src: int, graph: List[List[int]], visited: List[int]
    ) -> bool:
        # Mark the current node as visited
        visited[src] = True

        # Initialize a deque for BFS
        q: Deque = deque()
        q.append((src, -1))  # Tuple format: (current_node, parent_node)

        while q:
            front: Tuple = q.popleft()
            node, parent = front

            # Explore neighbors of the current node
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append((neighbor, node))
                elif neighbor != parent:
                    return True

        return False

    def has_cycle(self, v: int, graph: List[List[int]]) -> bool:
        # Initialize a List to track visited nodes
        visited: List[bool] = [False] * (v + 1)

        # Start the cycle detection from the first node (can be any node)
        # return detect(src=1, graph=graph, visited=visited)
        # for connected components
        for i in range(1, v + 1):
            # if not visited[i]:
            # if self.__detect_bfs(src=i, graph=graph, visited=visited):
            #     return True
            if not visited[i]:
                if self.__detect_dfs(node=i, parent=-1, graph=graph, visited=visited):
                    return True

        # checked all connected components no cycle founds.
        return False


if __name__ == "__main__":
    # Example usage of the is_cycle function with an undirected graph represented as an adjacency list
    graph: list[list[int]] = [
        [],
        [2, 3],
        [1, 5],
        [1, 4, 6],
        [3],
        [2, 7],
        [3, 7],
        [5, 6],
    ]
    solution: Solution = Solution()
    print("Does the graph contain a cycle?", solution.has_cycle(v=7, graph=graph))
