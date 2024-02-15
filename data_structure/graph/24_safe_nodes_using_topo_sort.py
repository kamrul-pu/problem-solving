"""Find safe nodes in a directed graph using topological sort."""

from collections import deque


def find_safe_nodes(v: int, g: list[list[int]]) -> list[int]:
    # Create the reversed graph and initialize indegree array
    g_rev: list[list[int]] = [[] for _ in range(v)]
    indegree: list[int] = [0] * v
    safe_nodes: list[int] = []

    # Populate the reversed graph and calculate indegrees
    for i in range(v):
        for it in g[i]:
            g_rev[it].append(i)
            indegree[i] += 1

    # Initialize a queue and enqueue nodes with indegree 0 which is terminal node
    q: deque = deque()
    for i in range(v):
        if indegree[i] == 0:
            q.append(i)

    # Perform topological sort using BFS
    while q:
        node = q.popleft()
        safe_nodes.append(node)
        for it in g_rev[node]:
            indegree[it] -= 1
            if indegree[it] == 0:
                q.append(it)

    # Sort the result and return the list of safe nodes
    safe_nodes.sort()
    return safe_nodes


if __name__ == "__main__":
    # Example usage of the find_safe_nodes function with a directed graph represented as an adjacency list
    g: list[list[int]] = [
        [1],
        [2],
        [3],
        [4, 5],
        [6],
        [6],
        [7],
        [],
        [1, 9],
        [10],
        [8],
        [9],
    ]
    safe_nodes: list[int] = find_safe_nodes(v=len(g), g=g)
    print(safe_nodes)
