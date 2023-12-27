"""Check if the graph is bipartite or not using dfs."""


def dfs(i: int, col: int, color: list[int], g: list[list[int]]) -> bool:
    color[i] = col
    for item in g[i]:
        if color[item] == -1:
            if not dfs(i=item, col=not col, color=color, g=g):
                return False
        elif color[item] == col:
            return False

    return True


def is_bipartite(g: list[list[int]], n: int) -> bool:
    color: list[int] = [-1] * n

    for i in range(n):
        if color[i] == -1:
            if not dfs(i=i, col=0, color=color, g=g):
                return False

    return True


if __name__ == "__main__":
    g: list[list[int]] = [
        [1],
        [0, 2, 4],
        [1, 3],
        [2, 5, 4],
        [1, 3],
        [3],
    ]
    n: int = len(g)
    print(is_bipartite(g=g, n=n))
