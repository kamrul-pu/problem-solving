"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns,
where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell,
(0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed).
You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
"""

import heapq
from typing import List


class Solution:
    def __f(self, heights: List[List[int]], n: int, m: int) -> int:
        # Priority queue to store cells to be visited, initialized with top-left cell (0, 0)
        pq = []
        # Matrix to store differences in efforts for each cell
        differences: List[List[int]] = [[float("inf")] * m for _ in range(n)]
        differences[0][0] = 0  # Effort to reach top-left cell is 0

        heapq.heappush(pq, (0, (0, 0)))  # Push initial cell into priority queue

        # Direction arrays for moving up, right, down, left
        dr: List[int] = [-1, 0, 1, 0]
        dc: List[int] = [0, 1, 0, -1]

        # Perform Dijkstra's algorithm
        while pq:
            difference, cell = heapq.heappop(pq)
            row, col = cell
            if row == n - 1 and col == m - 1:
                return difference  # If we reached the bottom-right cell, return the difference

            # Explore all four directions
            for i in range(4):
                n_row: int = row + dr[i]
                n_col: int = col + dc[i]

                # Check if the neighbor cell is within bounds
                if n > n_row >= 0 and m > n_col >= 0:
                    # Calculate the new effort by taking maximum difference between current and neighbor cell
                    new_effort: int = max(
                        abs(heights[row][col] - heights[n_row][n_col]), difference
                    )
                    # If new effort is less than recorded effort, update the difference and push into queue
                    if new_effort < differences[n_row][n_col]:
                        differences[n_row][n_col] = new_effort
                        heapq.heappush(pq, (new_effort, (n_row, n_col)))
        return -1  # If no path found, return -1

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Get the number of rows and columns in the matrix
        n: int = len(heights)
        m: int = len(heights[0])

        # Call the private function to compute the minimum effort
        return self.__f(heights=heights, n=n, m=m)


if __name__ == "__main__":
    # Example heights matrix
    heights: List[List[int]] = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    solution: Solution = Solution()
    print(solution.minimumEffortPath(heights=heights))
