from collections import deque
from typing import Deque, List


def topo_sort(g: List[List[int]], v: int) -> List[int]:
    """
    Perform topological sorting on a Directed Acyclic Graph (DAG) using BFS Kahn's Algorithm.

    :param g: Adjacency List representing the directed acyclic graph.
    :param v: Number of vertices in the graph.
    :return: List representing the topological ordering of nodes.
    """
    # Step 1: Initialize the indegree list
    # indegree[i] will be the number of incoming edges to vertex i
    indegree: List[int] = [0] * v

    # Step 2: Compute the indegree of each vertex
    # Traverse each vertex's adjacency list and update the indegree of its adjacent vertices
    for i in range(v):
        for item in g[i]:
            indegree[item] += 1

    # Step 3: Initialize the queue with all vertices having indegree 0
    # These vertices have no incoming edges and can be considered starting points
    q: Deque = deque()
    for i in range(v):
        if indegree[i] == 0:
            q.append(i)

    # Step 4: Process the vertices in the queue
    topo: List[int] = []  # List to store the topological order

    # While the queue is not empty
    while q:
        node = q.popleft()  # Remove a vertex from the front of the queue
        topo.append(node)  # Add it to the topological order

        # Decrease the indegree of all adjacent vertices
        for it in g[node]:
            indegree[it] -= 1
            # If the indegree of an adjacent vertex becomes 0, add it to the queue
            if indegree[it] == 0:
                q.append(it)

    # Return the topological ordering
    return topo


if __name__ == "__main__":
    # Example usage:
    # Define the adjacency list for a sample DAG
    g: List[List[int]] = [[], [], [3], [1], [0, 1], [0, 2]]
    # Perform topological sort on the graph
    ans: List[int] = topo_sort(g=g, v=len(g))
    # Print the result
    print(ans)
