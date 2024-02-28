"""Number of ways to arrive destination."""

import heapq
from typing import List, Tuple

# Define a constant for modulo operation
MOD: int = 10000007


def find_num_ways(g: List[List[int]], n: int) -> int:
    # set number of ways zero to all nodes
    ways: List[int] = [0] * n
    # set the source node ways to 1
    ways[0] = 1
    # create a distance array with infinity and set src distance zero
    dist: List[int] = [float("inf")] * n
    dist[0] = 0
    # declare a priority queue
    pq: Tuple[int] = []
    heapq.heappush(pq, (0, 0))
    while pq:
        # pop the front element of the priority q
        dis, node = heapq.heappop(pq)
        # traverse all the neighbour node calculate distance
        for neighbor in g[node]:
            n_node: int = neighbor[0]
            e_w: int = neighbor[1]
            new_dist: int = dis + e_w
            # if new distance is lesser than old then update distance and insert in pq
            if new_dist < dist[n_node]:
                dist[n_node] = new_dist
                heapq.heappush(pq, (new_dist, n_node))
                # copy the way of parent node
                ways[n_node] = ways[node]
            # if new distance is same as old distance then increase the number of ways
            elif new_dist == dist[n_node]:
                ways[n_node] += ways[node]

    # return the ways of destination node in this case n-1 % 1e7+10
    return ways[n - 1] % MOD


if __name__ == "__main__":
    n: int = 7
    m: int = 10
    edges: List[int] = [
        [0, 6, 7],
        [0, 1, 2],
        [1, 2, 3],
        [1, 3, 3],
        [6, 3, 3],
        [3, 5, 1],
        [6, 5, 1],
        [2, 5, 1],
        [0, 4, 5],
        [4, 6, 2],
    ]
    # generate graph from edges
    g: List[List[int]] = [[] for _ in range(n)]
    for item in edges:
        g[item[0]].append((item[1], item[2]))
        g[item[1]].append((item[0], item[2]))

    num_ways: int = find_num_ways(g=g, n=n)
    print(num_ways)
