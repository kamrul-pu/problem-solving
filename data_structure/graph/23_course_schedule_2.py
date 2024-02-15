"""
Detect cycle using topological sort and Kahn's Algorithm.
"""

from collections import deque


def find_order(n: int, prerequisities: list[list[int]]) -> list[int]:
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

    return topo if len(topo) == n else []


if __name__ == "__main__":
    # Example usage:
    g: list[list[int]] = [[1, 0], [2, 1], [3, 2]]
    print(find_order(n=4, prerequisities=g))
