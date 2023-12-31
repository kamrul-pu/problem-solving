"""Alien Dictionary using topo sort."""

from collections import deque


def topo_sort(g: list[list[int]], v: int) -> list[int]:
    """
    Perform topological sorting on a Directed Acyclic Graph (DAG) using BFS Kahn's Algorithm.

    :param g: Adjacency list representing the directed acyclic graph.
    :param v: Number of vertices in the graph.
    :return: List representing the topological ordering of nodes.
    """
    indegree: list[int] = [0] * v
    for i in range(v):
        for item in g[i]:
            indegree[item] += 1
    q: deque = deque()
    for i in range(v):
        if indegree[i] == 0:
            q.append(i)

    topo: list[int] = []
    while q:
        node = q.popleft()
        topo.append(node)

        for it in g[node]:
            indegree[it] -= 1
            if indegree[it] == 0:
                q.append(it)

    return topo


def find_order(strings: list[str], n: int, k: int) -> str:
    g: list[int] = [[] for _ in range(k)]
    for i in range(n - 1):
        s1: str = strings[i]
        s2: str = strings[i + 1]
        le: int = min(len(s1), len(s2))
        for j in range(le):
            if s1[j] != s2[j]:
                g[ord(s1[j]) - ord("a")].append(ord(s2[j]) - ord("a"))
                # print(s1[j], s2[j])
                break

    topo: list[int] = topo_sort(g=g, v=k)
    ans: str = ""
    for item in topo:
        ans += chr(item + ord("a"))
    return ans


if __name__ == "__main__":
    strings: list[str] = [
        "baa",
        "abcd",
        "abca",
        "cab",
        "cad",
    ]
    n: int = len(strings)  # Number of strings.
    k: int = 4  # number of alphabet
    ans: str = find_order(strings=strings, n=n, k=k)
    print(ans)
