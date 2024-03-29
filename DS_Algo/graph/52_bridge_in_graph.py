"""Bridge in Graph."""

from typing import List

TIMER: int = 1


def dfs(
    node: int,
    parent: int,
    visited: List[int],
    adj_list: List[List[int]],
    tin: List[int],
    low: List[int],
    bridges: List[List[int]],
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
                bridges=bridges,
            )
            low[node] = min(low[node], low[item])
            if low[item] > tin[node]:
                bridges.append([item, node])
        else:
            low[node] = min(low[node], low[item])


def critical_connections(n: int, connections: List[List[int]]) -> List[List[int]]:
    adj_list: List[List[int]] = [[] for _ in range(n)]
    for item in connections:
        adj_list[item[0]].append(item[1])
        adj_list[item[1]].append(item[0])
    visited: List[bool] = [False] * n
    tin: List[int] = [0] * n
    low: List[int] = [0] * n
    bridges: List[List[int]] = []
    dfs(
        node=0,
        parent=-1,
        visited=visited,
        adj_list=adj_list,
        tin=tin,
        low=low,
        bridges=bridges,
    )
    return bridges


if __name__ == "__main__":
    n: int = 4
    connections: List[List[int]] = [[0, 1], [1, 2], [2, 0], [1, 3]]
    critical: List[List[int]] = critical_connections(n=n, connections=connections)
    print(critical)
