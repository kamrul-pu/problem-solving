"""Path With Minimum Effort."""
import heapq


def minimum_effort(g: list[list[int]]) -> int:
    # Priority queue to store efforts and corresponding cell coordinates
    pq: list[int] = []

    # Number of rows in the grid
    n: int = len(g)

    # Number of columns in the grid
    m: int = len(g[0])

    # Matrix to store the minimum effort to reach each cell
    difference: list[list[int]] = [
        [float("inf") for col in range(m)] for row in range(n)
    ]

    # Set the effort to reach the starting cell (0, 0) as 0
    difference[0][0] = 0

    # Push the starting cell and its effort to the priority queue
    heapq.heappush(pq, (0, (0, 0)))

    # Direction arrays for moving up, right, down, left
    dr: list[int] = [-1, 0, 1, 0]
    dc: list[int] = [0, 1, 0, -1]

    # Dijkstra's algorithm to find the minimum effort path
    while pq:
        diff, cell = heapq.heappop(pq)
        r, c = cell

        # Check if we reached the destination cell
        if r == n - 1 and c == m - 1:
            return diff

        # Explore neighbors in all four directions
        for i in range(len(dr)):
            n_r: int = r + dr[i]
            n_c: int = c + dc[i]

            # Check if the neighbor is within bounds
            if n_r >= 0 and n_r < n and n_c >= 0 and n_c < m:
                # Calculate the new effort to reach the neighbor
                new_effort: int = max(abs(g[r][c] - g[n_r][n_c]), diff)
                if new_effort < difference[n_r][n_c]:
                    difference[n_r][n_c] = new_effort
                    heapq.heappush(pq, (new_effort, (n_r, n_c)))

    return -1


if __name__ == "__main__":
    g: list[list[int]] = [
        [1, 2, 2],
        [3, 8, 2],
        [5, 3, 5],
    ]
    print(minimum_effort(g=g))
