"""Detect Cycle in an directed graph. using dfs"""
from collections import deque


def detect(
    node: int,
    graph: list[list[int]],
    visited: list[int],
    path_visited: list[bool],
) -> bool:
    # Mark the current node as visited
    visited[node] = True
    path_visited[node] = True

    for item in graph[node]:
        if not visited[item]:
            if detect(
                node=item,
                graph=graph,
                visited=visited,
                path_visited=path_visited,
            ):
                return True
        elif path_visited[item]:
            return True

    path_visited[node] = False
    return False  # No cycle found


def is_cycle(v: int, graph: list[list[int]]) -> bool:
    # Initialize a list to track visited nodes
    visited: list[bool] = [False] * (v + 1)
    path_visited: list[bool] = [False] * (v + 1)

    # for connected components
    for i in range(1, v + 1):
        if not visited[i]:
            if detect(
                node=i,
                graph=graph,
                visited=visited,
                path_visited=path_visited,
            ):
                return True

    # checked all connected components no cycle founds.
    return False


if __name__ == "__main__":
    # Example usage of the is_cycle function with an undirected graph represented as an adjacency list
    graph: list[list[int]] = [
        [],
        [2],
        [3],
        [4, 7],
        [5],
        [6],
        [],
        [5],
        [9],
        [10],
        [8],
    ]
    print("Does the graph contain a cycle?", is_cycle(v=10, graph=graph))
