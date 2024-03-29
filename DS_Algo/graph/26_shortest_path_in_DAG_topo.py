"""Shortest path using topo sort in DAG."""

from typing import List, Tuple


def dfs(node: int, vis: List[bool], st: List[int], g: List[Tuple[int]]) -> None:
    vis[node] = True

    for item in g[node]:
        if not vis[item[0]]:
            dfs(node=item[0], vis=vis, st=st, g=g)
    st.append(node)


def topological_sort(g: List[Tuple[int]], n: int) -> List[int]:
    vis: List[bool] = [False] * n
    st: List[int] = []
    for i in range(n):
        if not vis[i]:
            dfs(node=i, vis=vis, st=st, g=g)

    dist: List[int] = [float("inf")] * n
    dist[len(st) - 1] = 0
    while st:
        node: int = st.pop()
        for item in g[node]:
            v: int = item[0]
            wt: int = item[1]

            if dist[node] + wt < dist[v]:
                dist[v] = dist[node] + wt

    return dist


if __name__ == "__main__":
    g: List[Tuple[int]] = [
        [(1, 2)],
        [(3, 1)],
        [(3, 3)],
        [],
        [(0, 3), (2, 1)],
        [(4, 1)],
        [(4, 2), (5, 3)],
    ]
    dist: List[int] = topological_sort(g=g, n=7)
    print(dist)
