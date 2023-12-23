"""M - Coloring Problem."""


def is_safe(node: int, color: int, colors: list[int], G: list[list[int]]) -> bool:
    for it in G[node]:
        if colors[it] == color:
            return False
    return True


def solve(node: int, G: list[list[int]], colors: list[int], n: int, m: int) -> bool:
    if node == n:
        return True
    for i in range(1, m + 1):
        if is_safe(node=node, color=i, colors=colors, G=G):
            colors[node] = i
            if solve(node=node + 1, G=G, colors=colors, n=n, m=m):
                return True
            colors[node] = 0

    return False


if __name__ == "__main__":
    n: int = 4
    G: list[list[int]] = [
        [1, 2, 3],
        [0, 2, 3],
        [0, 1],
        [0, 1],
    ]
    colors: list[int] = [0] * n
    m: int = 3
    if solve(node=0, G=G, colors=colors, n=n, m=m):
        print(f"The graph can be color with {m} color")
    else:
        print(f"The graph can't be color with {m} color")
    print("colors", colors)
