"""Detect Cycle in an undirected graph."""

from collections import deque
from typing import Deque, List, Tuple


def detect(src: int, graph: List[List[int]], visited: List[int]) -> bool:
    # Mark the current node as visited
    visited[src] = True

    # Initialize a deque for BFS
    q: Deque = deque()
    q.append((src, -1))  # Tuple format: (current_node, parent_node)

    while q:
        front: Tuple = q.popleft()
        node: int = front[0]
        parent: int = front[1]

        # Explore neighbors of the current node
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(
                    (neighbor, node)
                )  # Add the neighbor to the queue with current node as parent
            elif neighbor != parent:
                return True  # If the neighbor is already visited and not the parent, a cycle is detected

    return False  # No cycle found


def is_cycle(v: int, graph: List[List[int]]) -> bool:
    # Initialize a List to track visited nodes
    visited: List[bool] = [False] * (v + 1)

    # Start the cycle detection from the first node (can be any node)
    # return detect(src=1, graph=graph, visited=visited)
    # for connected components
    for i in range(1, v + 1):
        if not visited[i]:
            if detect(src=i, graph=graph, visited=visited):
                return True

    # checked all connected components no cycle founds.
    return False


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
