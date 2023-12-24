from collections import deque


def bfs(i: int, j: int, visited: list[list[bool]], matrix: list[list[int]]) -> None:
    # Mark the current cell as visited
    visited[i][j] = True

    # Initialize a queue for BFS
    q = deque()
    q.append((i, j))

    n: int = len(matrix)
    m: int = len(matrix[0])

    # Perform BFS traversal
    while q:
        front: tuple = q.popleft()
        row: int = front[0]
        col: int = front[1]

        # Explore all neighboring cells
        for di in range(-1, 2):
            for dj in range(-1, 2):
                nrow: int = row + di
                ncol: int = col + dj

                # Check if the neighboring cell is within bounds and is land (matrix[nrow][ncol] == 1)
                if (
                    nrow >= 0
                    and nrow < n
                    and ncol >= 0
                    and ncol < m
                    and matrix[nrow][ncol] == 1
                    and not visited[nrow][ncol]
                ):
                    # Mark the neighboring cell as visited and add it to the queue for further exploration
                    visited[nrow][ncol] = True
                    q.append((nrow, ncol))


def number_of_island(matrix: list[list[int]], n: int, m: int) -> int:
    # Initialize a 2D array to keep track of visited cells
    visited: list[list[bool]] = [[False for _ in range(m)] for row in range(n)]

    # Counter for the number of islands
    cnt: int = 0

    # Iterate through each cell in the matrix
    for i in range(n):
        for j in range(m):
            # If the cell is land (matrix[i][j] == 1) and has not been visited, start BFS traversal
            if not visited[i][j] and matrix[i][j] == 1:
                bfs(i=i, j=j, visited=visited, matrix=matrix)
                cnt += 1  # Increment the island count

    return cnt


if __name__ == "__main__":
    n: int = 5  # number of rows
    m: int = 4  # number of columns
    matrix: list[list[int]] = [
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 1],
    ]
    print(number_of_island(matrix=matrix, n=n, m=m))
