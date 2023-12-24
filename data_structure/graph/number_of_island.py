from collections import deque


def bfs(i: int, j: int, visited: list[list[bool]], matrix: list[list[int]]) -> None:
    visited[i][j] = True
    q = deque()
    q.append((i, j))
    n: int = len(matrix)
    m: int = len(matrix[0])
    while q:
        front: tuple = q.popleft()
        row: int = front[0]
        col: int = front[1]
        for di in range(-1, 2):
            for dj in range(-1, 2):
                nrow: int = row + di
                ncol: int = col + dj
                if (
                    nrow >= 0
                    and nrow < n
                    and ncol >= 0
                    and ncol < m
                    and matrix[nrow][ncol] == 1
                    and not visited[nrow][ncol]
                ):
                    visited[nrow][ncol] = True
                    q.append((nrow, ncol))


def number_of_island(matrix: list[list[int]], n: int, m: int) -> int:
    visited: list[list[bool]] = [[False for _ in range(m)] for row in range(n)]
    cnt: int = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and matrix[i][j] == 1:
                bfs(i=i, j=j, visited=visited, matrix=matrix)
                cnt += 1

    return cnt


if __name__ == "__main__":
    n: int = 5  # number of row
    m: int = 4  # number of column
    matrix: list[list[int]] = [
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 1],
    ]
    print(number_of_island(matrix=matrix, n=n, m=m))
