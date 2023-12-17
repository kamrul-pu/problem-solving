"""DFS Traversal"""

from collections import deque
import numpy as np


n: int = 8  # number of node
adj_list: list[list[int]] = [[] for _ in range(n + 1)]
adj_list[1] = [2, 3]
adj_list[2] = [1, 5, 6]
adj_list[3] = [1, 4, 7]
adj_list[4] = [3, 8]
adj_list[5] = [2]
adj_list[6] = [2]
adj_list[7] = [3, 8]
adj_list[8] = [4, 7]
print(adj_list)


def dfs(
    node: int, adj_list: list[list[int]], visited: [list[int]], ans: list[int]
) -> None:
    visited[node] = 1
    ans.append(node)
    for item in adj_list[node]:
        if not visited[item]:
            dfs(item, adj_list, visited, ans)


visited = np.zeros(n + 1, dtype=np.bool_)
ans: list[int] = []
starting_node: int = 1
visited[starting_node] = 1

dfs(starting_node, adj_list, visited, ans)
print(ans)
