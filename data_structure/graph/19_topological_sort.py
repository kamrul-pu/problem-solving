"""
Topological sort in python.
Graph Must be DAG -> Directed Acyclic Graph.
"""


def dfs(i: int, vis: list[bool], st: list[int], g: list[list[int]]) -> None:
    vis[i] = True

    for item in g[i]:
        if not vis[item]:
            dfs(i=item, vis=vis, st=st, g=g)
    st.append(i)


def topological_sort(g: list[list[int]], v: int) -> list[int]:
    vis: list[bool] = [False] * v
    st: list[int] = []
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
    g: list[list[int]] = [[], [], [3], [1], [0, 1], [0, 2]]
    ans: list[int] = topological_sort(g=g, v=len(g))
    print(ans)
