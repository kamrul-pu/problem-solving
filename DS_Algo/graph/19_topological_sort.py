"""
Topological sort in python.
Graph Must be DAG -> Directed Acyclic Graph.
"""

from typing import List


def dfs(i: int, vis: List[bool], st: List[int], g: List[List[int]]) -> None:
    vis[i] = True

    for item in g[i]:
        if not vis[item]:
            dfs(i=item, vis=vis, st=st, g=g)
    st.append(i)


def topological_sort(g: List[List[int]], v: int) -> List[int]:
    vis: List[bool] = [False] * v
    st: List[int] = []
    for i in range(v):
        if not vis[i]:
            dfs(i=i, vis=vis, st=st, g=g)

    low: int = 0
    high: int = len(st) - 1
    while low < high:
        st[low], st[high] = st[high], st[low]
        low += 1
        high -= 1

    return st


if __name__ == "__main__":
    g: List[List[int]] = [[], [], [3], [1], [0, 1], [0, 2]]
    ans: List[int] = topological_sort(g=g, v=len(g))
    print(ans)
