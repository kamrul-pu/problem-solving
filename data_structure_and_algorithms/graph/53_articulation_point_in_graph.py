"""Articulation points in Graph."""

from typing import List

TIMER: int = 0


def dfs(
    node: int,
    parent: int,
    visited: List[int],
    adj_list: List[List[int]],
    tin: List[int],
    low: List[int],
    mark: List[int],
) -> None:
    global TIMER
    visited[node] = True
    tin[node] = TIMER
    low[node] = TIMER
    TIMER += 1
    for item in adj_list[node]:
        if item == parent:
            continue
        if not visited[item]:
            dfs(
                node=item,
                parent=node,
                visited=visited,
                adj_list=adj_list,
                tin=tin,
                low=low,
                mark=mark,
            )
            low[node] = min(low[node], low[item])
            if low[item] >= tin[node] and parent != -1:
                mark[node] = 1
        else:
            low[node] = min(low[node], tin[item])


def articulation_points(n: int, connections: List[List[int]]) -> List[int]:
    adj_list: List[List[int]] = [[] for _ in range(n)]
    for item in connections:
        adj_list[item[0]].append(item[1])
        adj_list[item[1]].append(item[0])
    visited: List[bool] = [False] * n
    tin: List[int] = [0] * n
    low: List[int] = [0] * n
    mark: List[int] = [0] * n
    for i in range(n):
        if not visited[i]:
            dfs(
                node=i,
                parent=-1,
                visited=visited,
                adj_list=adj_list,
                tin=tin,
                low=low,
                mark=mark,
            )
    ans: List[int] = []
    for i in range(n):
        if mark[i] == 1:
            ans.append(i)
    return ans if len(ans) > 0 else [-1]


if __name__ == "__main__":
    n: int = 4
    connections: List[List[int]] = [[0, 1], [1, 2], [2, 0], [1, 3]]
    points: List[int] = articulation_points(n=n, connections=connections)
    print(points)
