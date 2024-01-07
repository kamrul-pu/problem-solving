"""Strongly connected component using Kosaraju's algorithm."""


def dfs(node: int, visited: list[bool], adj: list[list[int]], st: list[int]) -> None:
    visited[node] = True

    for item in adj[node]:
        if not visited[item]:
            dfs(node=item, visited=visited, adj=adj, st=st)

    st.append(node)


def kosaraju(v: int, adj: list[list[int]]) -> int:
    visited: list[bool] = [False] * v
    st: list[int] = []

    for i in range(v):
        if not visited[i]:
            dfs(node=i, visited=visited, adj=adj, st=st)

    # reverse the graph
    adj_t: list[list[int]] = [[] for _ in range(v)]
    for i in range(v):
        visited[i] = False
        for item in adj[i]:
            adj_t[item].append(i)

    # run dfs on nodes based on finishing time
    ans: list[list[int]] = []
    scc: int = 0
    while st:
        node: int = st.pop()
        scc_list: list[int] = []
        if not visited[node]:
            scc += 1
            dfs(node=node, visited=visited, adj=adj_t, st=scc_list)
            ans.append(scc_list)

    print(ans)

    return scc


if __name__ == "__main__":
    adj: list[list[int]] = [[1], [2], [0, 3], [4], [5, 7], [6], [4, 7], []]
    scc: int = kosaraju(v=len(adj), adj=adj)
    print(scc)
