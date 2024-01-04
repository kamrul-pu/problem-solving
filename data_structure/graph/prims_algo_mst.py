"""Prim's algorithm For Minimum Spanning Tree (MST)."""

import heapq


def mst_sum(adj_list: list[tuple[int]]) -> int:
    """Calculate the sum of weights in the MST using Prim's algorithm.

    Args:
        adj_list (list[tuple[int]]): Adjacency list representation of the graph.

    Returns:
        int: Sum of weights in the Minimum Spanning Tree.
    """
    n: int = len(adj_list)
    visited: list[bool] = [False] * n
    m_sum: int = 0
    pq: list[tuple[int]] = []

    # Start with the first node
    heapq.heappush(pq, (0, 0))

    while pq:
        wt, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        m_sum += wt

        # Add neighbors to the priority queue
        for edge in adj_list[node]:
            neighbour, edw = edge
            if not visited[neighbour]:
                heapq.heappush(pq, (edw, neighbour))

    return m_sum


def prims_algo_mst(adj_list: list[list[int]]) -> list[tuple[int]]:
    """Find the Minimum Spanning Tree (MST) using Prim's algorithm.

    Args:
        adj_list (list[list[int]]): Adjacency list representation of the graph.

    Returns:
        list[tuple[int]]: List of edges in the Minimum Spanning Tree.
    """
    n: int = len(adj_list)
    visited: list[bool] = [False] * n
    mst: list[tuple[int]] = []
    pq: list[tuple[int]] = []

    # Start with the first node, parent -1 to indicate it has no parent
    heapq.heappush(pq, (0, 0, -1))

    while pq:
        wt, node, parent = heapq.heappop(pq)
        if visited[node]:
            continue

        visited[node] = True
        if parent != -1:
            # Add the edge to the MST
            mst.append((parent, node))

        # Add neighbors to the priority queue
        for edge in adj_list[node]:
            neighbour, edw = edge
            if not visited[neighbour]:
                heapq.heappush(pq, (edw, neighbour, node))

    return mst


if __name__ == "__main__":
    # Example usage
    adj_list: list[list[int]] = [
        [(1, 2), (2, 1)],
        [(0, 2), (2, 1)],
        [(0, 1), (1, 1), (3, 2), (4, 2)],
        [(2, 2), (4, 1)],
        [(2, 2), (3, 1)],
    ]
    m_sum: int = mst_sum(adj_list=adj_list)
    print(m_sum)
    mst: list[tuple[int]] = prims_algo_mst(adj_list=adj_list)
    print(mst)
