"""Detect Cycle in an undirected graph. using dfs"""

from collections import deque
from typing import Deque, List, Tuple


def detect(node: int, parent: int, graph: List[List[int]], visited: List[int]) -> bool:
    # Mark the current node as visited
    visited[node] = True

    for item in graph[node]:
        if not visited[item]:
            return detect(node=item, parent=node, graph=graph, visited=visited)
        elif item != parent:
            return True

    return False  # No cycle found


def is_cycle(v: int, graph: List[List[int]]) -> bool:
    # Initialize a List to track visited nodes
    visited: List[bool] = [False] * (v + 1)

    # Start the cycle detection from the first node (can be any node)
    return detect(node=1, parent=-1, graph=graph, visited=visited)
    # # for connected components
    # for i in range(1, v + 1):
    #     if not visited[i]:
    #         if detect(node=i, parent=-1, graph=graph, visited=visited):
    #             return True

    # # checked all connected components no cycle founds.
    # return False


if __name__ == "__main__":
    # Example usage of the is_cycle function with an undirected graph represented as an adjacency List
    graph: List[List[int]] = [
        [],
        [2, 3],
        [1, 5],
        [1, 4, 6],
        [3],
        [2, 7],
        [3, 7],
        [5, 6],
    ]
    print("Does the graph contain a cycle?", is_cycle(v=7, graph=graph))
