"""Rat in a Maze."""


def solve(
    i: int,
    j: int,
    m: list[list[int]],
    n: int,
    ans: list[str],
    move: str,
    visited: list[list[bool]],
) -> None:
    if i == n - 1 and j == n - 1:
        ans.append(move)
        return
    # downward
    if i + 1 < n and not visited[i + 1][j] and m[i + 1][j] == 1:
        visited[i][j] = True
        solve(i=i + 1, j=j, m=m, n=n, ans=ans, move=move + "D", visited=visited)
        visited[i][j] = False
    # left
    if j - 1 >= 0 and not visited[i][j - 1] and m[i][j - 1] == 1:
        visited[i][j] = True
        solve(i=i, j=j - 1, m=m, n=n, ans=ans, move=move + "L", visited=visited)
        visited[i][j] = False

    # right
    if j + 1 < n and not visited[i][j + 1] and m[i][j + 1] == 1:
        visited[i][j] = True
        solve(i=i, j=j + 1, m=m, n=n, ans=ans, move=move + "R", visited=visited)
        visited[i][j] = False
    # upword
    if i - 1 >= 0 and not visited[i - 1][j] and m[i - 1][j] == 1:
        visited[i][j] = True
        solve(i=i - 1, j=j, m=m, n=n, ans=ans, move=move + "U", visited=visited)
        visited[i][j] = False


if __name__ == "__main__":
    m: list[list[int]] = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 1],
    ]
    n: int = 4
    visited: list[list[bool]] = [[False for col in range(n)] for row in range(n)]
    ans: list[str] = []
    if m[0][0] == 1:
        solve(i=0, j=0, m=m, n=n, ans=ans, move="", visited=visited)

    print(ans)
