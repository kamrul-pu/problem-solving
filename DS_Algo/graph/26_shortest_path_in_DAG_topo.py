"""Shortest path using topo sort in DAG."""

from typing import List, Tuple


def dfs(
    node: int, vis: List[bool], st: List[int], g: List[List[Tuple[int, int]]]
) -> None:
    vis[node] = True
    for neighbor, _ in g[node]:
        if not vis[neighbor]:
            dfs(neighbor, vis, st, g)
    st.append(node)


def topological_sort(g: List[List[Tuple[int, int]]], n: int) -> List[int]:
    """
    Compute the shortest paths from the source node to all other nodes in a Directed Acyclic Graph (DAG)
    using topological sorting.

    :param g: Graph represented as an adjacency list where each node has a list of tuples.
              Each tuple represents an edge (destination_node, weight).
    :param n: Number of nodes in the graph.
    :return: List of shortest distances from the source node (node 0) to all other nodes.
    """
    # Initialize visited list and stack for topological sort
    vis: List[bool] = [False] * n
    st: List[int] = []

    # Perform DFS to get the topological ordering of the nodes
    for i in range(n):
        if not vis[i]:
            dfs(i, vis, st, g)

    # Initialize distances with infinity and set distance to the source node (0) as 0
    dist: List[int] = [float("inf")] * n
    dist[6] = 0

    # Process nodes in topological order to find shortest paths
    while st:
        node = st.pop()
        for neighbor, weight in g[node]:
            dist[neighbor] = min(dist[neighbor], dist[node] + weight)

    return dist


if __name__ == "__main__":
    # Define the graph as an adjacency list
    g: List[List[Tuple[int, int]]] = [
        [(1, 2)],  # Node 0 has an edge to Node 1 with weight 2
        [(3, 1)],  # Node 1 has an edge to Node 3 with weight 1
        [(3, 3)],  # Node 2 has an edge to Node 3 with weight 3
        [],  # Node 3 has no outgoing edges
        [
            (0, 3),
            (2, 1),
        ],  # Node 4 has edges to Node 0 with weight 3 and Node 2 with weight 1
        [(4, 1)],  # Node 5 has an edge to Node 4 with weight 1
        [
            (4, 2),
            (5, 3),
        ],  # Node 6 has edges to Node 4 with weight 2 and Node 5 with weight 3
    ]

    # Compute shortest paths from source node (0)
    dist: List[int] = topological_sort(g=g, n=7)
    print(dist)
