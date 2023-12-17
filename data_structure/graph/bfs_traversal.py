"""BFS Traversal"""

from collections import deque
import numpy as np


n: int = 8  # number of node
adj_list: list[list[int]] = [[], [], [], [], [], [], [], [], []]
adj_list[1] = [2, 6]
adj_list[2] = [1, 3, 4]
adj_list[3] = [2]
adj_list[4] = [2, 5]
adj_list[5] = [4, 7]
adj_list[6] = [1, 7, 8]
adj_list[7] = [6, 5]
adj_list[8] = [6]
print(adj_list)


def bfs(adj_list: list[list[int]], n: int, root: int) -> list[int]:
    visited = np.zeros(n + 1, dtype=np.bool_)
    ans: list[int] = []
    q = deque()
    q.append(root)
    visited[root] = True
    while q:
        node: int = q.popleft()
        ans.append(node)
        for item in adj_list[node]:
            if not visited[item]:
                q.append(item)
                visited[item] = True

    return ans


result: list[int] = bfs(adj_list=adj_list, n=n, root=1)
print(result)
