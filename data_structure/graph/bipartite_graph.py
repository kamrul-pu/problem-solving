"""Check if the graph is bipartite or not."""

from collections import deque


def is_bipartite(g: list[list[int]], n: int) -> bool:
    color: list[int] = [-1] * n
    q: deque = deque()
    # start with node 0 and color it to zero.
    q.append(0)
    color[0] = 0
    while q:
        node: int = q.popleft()

        for item in g[node]:
            # not yet colored
            if color[item] == -1:
                color[item] = int(not color[node])
                q.append(item)
            elif color[item] == color[node]:
                return False

    return True


if __name__ == "__main__":
    g: list[list[int]] = [
        [1],
        [0, 2, 6],
        [1, 3],
        [2, 5, 4],
        [3, 6],
        [3],
        [1, 4],
    ]
    n: int = len(g)
    print(is_bipartite(g=g, n=n))
